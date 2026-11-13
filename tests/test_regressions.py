"""Run after building: python -m unittest discover -s tests -v.

Uses installed Microsoft Edge by default; set BROWSER_CHANNEL=chromium to use
the Chromium installed by `python -m playwright install chromium`.
"""
import os
import base64
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest

import openpyxl
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
HEADERS = ['Vị trí ghế', 'Số ghế', 'Họ tên', 'Trình độ', 'Loại ghế', 'Khen thưởng']


def rows_for(count):
    return [dict(zip(HEADERS, [i, str(i), f'Tân khoa {i}', 'Đại học', '', '']))
            for i in range(1, count + 1)]


class BrowserRegressions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runtime = sync_playwright().start()
        channel = os.environ.get('BROWSER_CHANNEL', 'msedge')
        cls.browser = cls.runtime.chromium.launch(
            headless=True, **({'channel': channel} if channel != 'chromium' else {}))
        cls.page = cls.browser.new_page(viewport={'width': 1920, 'height': 1080})
        cls.errors = []
        cls.page.on('pageerror', lambda e: cls.errors.append(str(e)))
        cls.page.goto((ROOT / 'index.html').as_uri())
        cls.page.wait_for_function('window.dueGraduationApp')
        cls.page.keyboard.press('Space')
        cls.page.evaluate('dueGraduationApp.toggleEffects()')

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.runtime.stop()

    def tearDown(self):
        self.assertEqual(self.errors, [])

    def apply(self, rows, config=None):
        return self.page.evaluate('''({rows, config}) => {
          const parsed = dueGraduationApp.parseRows(rows);
          dueGraduationApp.applyData(parsed.list, parsed.issues,
            config || {vipRows:4, familyRows:5, ncsSpec:'4-R'});
          dueGraduationApp.updateHonors(0);
          return {list:parsed.list, issues:parsed.issues};
        }''', {'rows': rows, 'config': config})

    def test_special_labels_and_negative_award(self):
        rows = rows_for(3)
        for row, label in zip(rows, ['constructor', '__proto__', 'toString']):
            row['Số ghế'] = label
            row['Khen thưởng'] = 'Không khen thưởng'
        parsed = self.apply(rows)
        self.assertEqual(parsed['issues'], [])
        self.assertTrue(all(not r['isAward'] for r in parsed['list']))
        for pos, row in enumerate(rows, 1):
            self.page.evaluate('label => dueGraduationApp.focusSeat(label)', row['Số ghế'])
            self.assertEqual(self.page.evaluate('HONORS_STATE.list[HONORS_STATE.currentIndex].pos'), pos)

    def test_nine_seats_per_side_and_row_boundaries(self):
        self.apply(rows_for(36))
        positions = self.page.evaluate('''() => [...document.querySelectorAll('.seat[data-pos]')].map(el => {
          const rect = el.querySelector('rect');
          return {pos:Number(el.dataset.pos),x:Number(rect.getAttribute('x')),
            y:Number(rect.getAttribute('y')),width:Number(rect.getAttribute('width'))};
        })''')
        by_pos = {seat['pos']: seat for seat in positions}
        for start in [1, 19]:
            row = [by_pos[pos] for pos in range(start, start + 18)]
            self.assertEqual(sum(seat['x'] < 960 for seat in row), 9)
            self.assertEqual(sum(seat['x'] > 960 for seat in row), 9)
            self.assertEqual(len({seat['y'] for seat in row}), 1)
            self.assertAlmostEqual(by_pos[start]['x'], 520)
            self.assertAlmostEqual(by_pos[start + 8]['x'] + by_pos[start + 8]['width'], 920)
            self.assertAlmostEqual(by_pos[start + 9]['x'] + by_pos[start + 9]['width'], 1400)
            self.assertAlmostEqual(by_pos[start + 17]['x'], 1000)
        self.assertGreater(by_pos[19]['y'], by_pos[18]['y'])
        for pos, row, side in [(9,5,'Trái'), (10,5,'Phải'), (18,5,'Phải'), (19,6,'Trái')]:
            self.page.evaluate('pos => dueGraduationApp.jumpTo(String(pos))', pos)
            location = self.page.locator('#honorsSeatLocation').text_content()
            self.assertIn(f'Dãy {row}', location)
            self.assertIn(side, location)
            self.page.evaluate('pos => dueGraduationApp.focusSeat(String(pos))', pos)
            self.assertIn(side, self.page.locator('#toast').text_content())

    def test_template_download_uses_current_seating_instructions(self):
        with self.page.expect_download() as download:
            self.page.get_by_role('button', name='Tải mẫu Excel').click()
        data = download.value.path().read_bytes()
        self.assertEqual(data, (ROOT / 'Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx').read_bytes())
        import io
        workbook = openpyxl.load_workbook(io.BytesIO(data))
        self.assertIn('18 ghế/dãy', workbook['HuongDan']['B14'].value)

    def test_sparse_duplicate_and_capacity(self):
        rows = rows_for(360)
        rows.pop(16)
        rows += [dict(rows[0]), dict(zip(HEADERS, [361, '361', 'Ngoài sức chứa', '', '', '']))]
        result = self.apply(rows)
        self.assertEqual(self.page.locator('.seat[data-pos]').count(), 359)
        self.assertEqual(self.page.locator('.seat-empty').count(), 1)
        self.assertIsNone(result['list'][-1]['pos'])
        self.assertIsNone(result['list'][-2]['pos'])
        self.assertGreaterEqual(len(result['issues']), 3)

    def test_dynamic_rows_and_invalid_config(self):
        for count in [18, 19, 232, 255, 260, 280]:
            with self.subTest(count=count):
                self.apply(rows_for(count))
                state = self.page.evaluate('dueGraduationApp.state.layout')
                self.assertEqual(state['rows'], (count + 17) // 18)
                self.assertEqual(self.page.locator('.seat-empty').count(), (-count) % 18)
        self.apply(rows_for(20), {'vipRows': 'invalid', 'familyRows': 2.7})
        self.assertEqual(self.page.evaluate('APP_STATE.config.vipRows'), 4)
        self.assertEqual(self.page.evaluate('APP_STATE.config.familyRows'), 2)
        self.assertEqual(self.page.locator('[y="NaN"]').count(), 0)
        self.page.evaluate('dueGraduationApp.updateHonors(NaN)')
        self.assertEqual(self.page.evaluate('HONORS_STATE.currentIndex'), 0)
        self.assertEqual(self.page.evaluate('dueGraduationApp.parseRows([null,42,[]]).list'), [])

    def test_png_export(self):
        self.apply(rows_for(20))
        self.page.evaluate('''() => {
          const create = URL.createObjectURL.bind(URL);
          URL.createObjectURL = blob => {
            if (blob.type.startsWith('image/svg+xml')) window.exportedSvg = blob.text();
            return create(blob);
          };
        }''')
        with self.page.expect_download(timeout=30000) as download:
            self.page.evaluate('dueGraduationApp.exportPng()')
        target = ROOT / 'test-results' / 'export.png'
        target.parent.mkdir(exist_ok=True)
        download.value.save_as(target)
        image = target.read_bytes()
        self.assertEqual(image[:8], b'\x89PNG\r\n\x1a\n')
        self.assertEqual(struct.unpack('>II', image[16:24]), (1920, 1080))
        svg = self.page.evaluate('window.exportedSvg')
        self.assertIn('data:font/otf;base64,', svg)
        self.assertIn('honorsPlaqueName1', svg)

    def test_config_change_keeps_selected_honoree(self):
        self.apply(rows_for(40))
        self.page.evaluate('dueGraduationApp.updateHonors(25)')
        self.page.locator('#btnToggleConfig').click()
        self.page.locator('#btnVipPlus').click()
        self.assertEqual(self.page.evaluate('HONORS_STATE.currentIndex'), 25)
        self.assertIn('26', self.page.locator('#honorsSeatPillText').text_content())
        self.assertEqual(self.page.locator('.seat.highlight').get_attribute('data-pos'), '26')
        self.page.locator('#btnToggleConfig').click()

    def test_disabled_effects_do_not_redraw_canvas(self):
        self.page.evaluate('''() => {
          const ctx = document.getElementById('fireworksCanvas').getContext('2d');
          const clear = ctx.clearRect.bind(ctx);
          window.canvasClears = 0;
          ctx.clearRect = (...args) => { window.canvasClears++; clear(...args); };
        }''')
        self.page.wait_for_timeout(150)
        self.assertLessEqual(self.page.evaluate('window.canvasClears'), 1)

    def test_fireworks_align_with_svg_after_rotation_and_fullscreen(self):
        page = self.browser.new_page(viewport={'width': 1920, 'height': 1080})
        try:
            page.goto((ROOT / 'index.html').as_uri())
            page.wait_for_function('window.dueGraduationApp')
            page.keyboard.press('Space')
            page.evaluate('dueGraduationApp.toggleEffects()')
            # Let the disabled animation loop clear its previous frame once.
            page.wait_for_timeout(100)
            for fullscreen, width, height in [(False,1920,1080), (False,1080,1920),
                                              (True,1080,1920), (True,2560,1080),
                                              (True,1920,1080)]:
                with self.subTest(fullscreen=fullscreen, width=width, height=height):
                    page.set_viewport_size({'width': width, 'height': height})
                    if fullscreen and not page.evaluate('!!document.fullscreenElement'):
                        page.keyboard.press('f')
                        page.wait_for_function('!!document.fullscreenElement')
                    point = page.evaluate('''async () => {
                      await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
                      const canvas = document.getElementById('fireworksCanvas');
                      const ctx = canvas.getContext('2d');
                      ctx.clearRect(0,0,1920,1080);
                      ctx.globalCompositeOperation = 'source-over';
                      ctx.fillStyle = '#ff00ff';
                      ctx.fillRect(199,170,20,20);
                      // Use SVG's actual screen transform as the independent reference.
                      const svg = document.getElementById('masterSvg');
                      const p = new DOMPoint(209,180).matrixTransform(svg.getScreenCTM());
                      return {x:Math.round(p.x), y:Math.round(p.y)};
                    }''')
                    screenshot = base64.b64encode(page.screenshot()).decode('ascii')
                    pixel = page.evaluate('''async ({screenshot,point}) => {
                      const image = new Image();
                      image.src = 'data:image/png;base64,' + screenshot;
                      await image.decode();
                      const sample = document.createElement('canvas');
                      sample.width = sample.height = 1;
                      const ctx = sample.getContext('2d');
                      ctx.drawImage(image,point.x,point.y,1,1,0,0,1,1);
                      return [...ctx.getImageData(0,0,1,1).data];
                    }''', {'screenshot': screenshot, 'point': point})
                    self.assertEqual(pixel, [255,0,255,255], (point,pixel))
        finally:
            page.close()

    def test_seat_click_is_handled_once(self):
        self.apply(rows_for(20))
        self.page.evaluate('''() => {
          window.toastWrites = 0;
          window.toastObserver = new MutationObserver(records => {
            window.toastWrites += records.length;
          });
          toastObserver.observe(document.getElementById('toast'), {childList:true});
        }''')
        self.page.locator('.seat[data-pos="3"]').click(force=True)
        self.assertEqual(self.page.evaluate('window.toastWrites'), 1)
        self.assertEqual(self.page.evaluate('HONORS_STATE.currentIndex'), 2)
        self.page.evaluate('toastObserver.disconnect()')


class BuildRegressions(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        for path in [ROOT / 'build_due_html.py', *ROOT.glob('*.b64.txt'),
                     ROOT / 'Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx']:
            shutil.copy2(path, self.folder / path.name)
        shutil.copytree(ROOT / 'sources', self.folder / 'sources')

    def build(self):
        # Deliberately invoke from a different working directory.
        return subprocess.run([sys.executable, str(self.folder / 'build_due_html.py')],
                              cwd=ROOT, capture_output=True)

    def test_corrupt_workbook_preserves_existing_page(self):
        (self.folder / 'danhsach.xlsx').write_bytes(b'not an Excel file')
        target = self.folder / 'index.html'
        target.write_text('previous working page', encoding='utf-8')
        self.assertNotEqual(self.build().returncode, 0)
        self.assertEqual(target.read_text(), 'previous working page')

    def test_excel_text_cannot_close_script(self):
        workbook = openpyxl.Workbook()
        workbook.active.append(HEADERS)
        name = '</script><script>window.injected=true</script>'
        workbook.active.append([1, '1', name, 'Đại học', '', ''])
        workbook.save(self.folder / 'danhsach.xlsx')
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        html = (self.folder / 'index.html').read_text(encoding='utf-8')
        self.assertNotIn(name, html)
        self.assertIn(r'\u003c/script\u003e', html)


if __name__ == '__main__':
    unittest.main()
