import base64
import json
import os
from pathlib import Path
import openpyxl

# Resolve inputs beside this script, including when invoked from another folder.
os.chdir(Path(__file__).resolve().parent)


def _cell_to_str(v):
    if v is None:
        return ''
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return str(v).strip()


def get_default_honors_rows_json():
    """Doc sheet dau tien cua danhsach.xlsx (uu tien) hoac file mau.
    Tra ve JSON cac dong tho {tieu de cot: gia tri chuoi}. Phan tich nghiep vu do JS (parseHonorRows)
    dam nhiem de dung CHUNG 1 logic voi nut 'Nhap Excel'."""
    candidates = ['danhsach.xlsx', 'Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx']
    for file_path in candidates:
        if not os.path.exists(file_path):
            continue
        try:
            wb = openpyxl.load_workbook(file_path, data_only=True)
            sheet = wb.worksheets[0]
            rows = list(sheet.iter_rows(values_only=True))
            if len(rows) < 2:
                continue
            headers = [_cell_to_str(h) for h in rows[0]]
            out = []
            for r in rows[1:]:
                if not any(_cell_to_str(c) for c in r):
                    continue
                rec = {}
                for h, c in zip(headers, r):
                    if h:
                        rec[h] = _cell_to_str(c)
                out.append(rec)
            if out:
                print(f"Loaded {len(out)} default rows from {file_path}")
                return json.dumps(out, ensure_ascii=False, separators=(',', ':'))
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    demo = [
        {"Vị trí ghế": "", "Số ghế": "TS1", "Họ tên": "TS. NGUYỄN VĂN AN", "Trình độ": "Tiến sĩ", "Loại ghế": "", "Khen thưởng": "x", "Ghi chú": ""},
        {"Vị trí ghế": "1", "Số ghế": "1", "Họ tên": "TRẦN MINH ĐỨC", "Trình độ": "Đại học", "Loại ghế": "", "Khen thưởng": "x", "Ghi chú": ""},
    ]
    return json.dumps(demo, ensure_ascii=False, separators=(',', ':'))


default_honors_rows_json = get_default_honors_rows_json()

with open('sources/xlsx.full.min.js', 'r', encoding='utf-8') as f:
    js_xlsx = f.read()


with open('logo_due.b64.txt', 'r', encoding='utf-8') as f:
    b64_logo = f.read().strip()
with open('art_fireworks.b64.txt', 'r', encoding='utf-8') as f:
    b64_fw = f.read().strip()
with open('art_campus.b64.txt', 'r', encoding='utf-8') as f:
    b64_campus = f.read().strip()
with open('art_congrats.b64.txt', 'r', encoding='utf-8') as f:
    b64_congrats = f.read().strip()
with open('art_cap.b64.txt', 'r', encoding='utf-8') as f:
    b64_cap = f.read().strip()
with open('plaque_tiensi.b64.txt', 'r', encoding='utf-8') as f:
    b64_plaque_tiensi = f.read().strip()
with open('plaque_thacsi.b64.txt', 'r', encoding='utf-8') as f:
    b64_plaque_thacsi = f.read().strip()
with open('plaque_cunhan.b64.txt', 'r', encoding='utf-8') as f:
    b64_plaque_cunhan = f.read().strip()
with open('Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx', 'rb') as f:
    b64_template_xlsx = base64.b64encode(f.read()).decode('ascii')

template = f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sơ Đồ Chỗ Ngồi | Lễ Tốt Nghiệp Đợt 3 Năm 2026 - DUE</title>
<style>
/* ==========================================================================
   TRƯỜNG ĐẠI HỌC KINH TẾ - ĐẠI HỌC ĐÀ NẴNG (DUE)
   OFFICIAL GRADUATION SEATING CEREMONY — DIGITAL SIGNAGE (1920 × 1080)
   100% Offline Single File • Native 16:9 Full HD Presentation
   ========================================================================== */

@font-face {{
  font-family: 'SVN-Gilroy';
  src: url('sources/brand-assets/fonts/SVN-Gilroy Bold.otf') format('opentype');
  font-weight: 700;
  font-style: normal;
}}
@font-face {{
  font-family: 'SVN-Gilroy';
  src: url('sources/brand-assets/fonts/SVN-Gilroy XBold.otf') format('opentype');
  font-weight: 800;
  font-style: normal;
}}
@font-face {{
  font-family: 'SVN-Gilroy';
  src: url('sources/brand-assets/fonts/SVN-Gilroy Heavy.otf') format('opentype');
  font-weight: 900;
  font-style: normal;
}}
@font-face {{
  font-family: 'SVN-Gilroy';
  src: url('sources/brand-assets/fonts/SVN-Gilroy SemiBold.otf') format('opentype');
  font-weight: 600;
  font-style: normal;
}}
@font-face {{
  font-family: 'SVN-Gilroy';
  src: url('sources/brand-assets/fonts/SVN-Gilroy Medium.otf') format('opentype');
  font-weight: 500;
  font-style: normal;
}}
@font-face {{
  font-family: 'SVN-Gilroy';
  src: url('sources/brand-assets/fonts/SVN-Gilroy Regular.otf') format('opentype');
  font-weight: 400;
  font-style: normal;
}}

:root {{
  --font-main: 'SVN-Gilroy', 'Montserrat', 'Be Vietnam Pro', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
  --due-blue: #005EA3;
  --due-green: #058E47;
  --due-orange: #EE6323;
  --due-yellow: #FFB612;
  --bg-deep-navy: #02091c;
  --gold-primary: #f2c355;
  --gold-light: #ffea9f;
}}

* {{ box-sizing: border-box; }}
html, body {{
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow-x: hidden;
  background-color: var(--bg-deep-navy);
  font-family: var(--font-main);
  color: #fff;
  user-select: none;
  -webkit-font-smoothing: antialiased;
}}

/* Management Header Toolbar */
.toolbar {{
  position: relative;
  z-index: 100;
  height: 60px;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  background: linear-gradient(180deg, rgba(6, 21, 51, 0.98), rgba(2, 9, 28, 0.95));
  backdrop-filter: blur(14px);
  border-bottom: 1px solid rgba(242, 195, 85, 0.35);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.6);
}}

.brand-title {{
  display: flex;
  align-items: center;
  gap: 12px;
}}
.brand-badge {{
  background: linear-gradient(135deg, var(--due-blue), #043869);
  color: #ffffff;
  font-size: 11.5px;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 6px;
  letter-spacing: 0.05em;
  border: 1px solid rgba(255, 255, 255, 0.3);
}}
.brand-text {{
  font-size: 14.5px;
  font-weight: 700;
  color: var(--gold-light);
  letter-spacing: 0.02em;
}}
.brand-sub {{
  font-size: 12px;
  color: #9cb5db;
  margin-left: 6px;
}}

.toolbar-controls {{
  display: flex;
  align-items: center;
  gap: 10px;
}}

/* Quick Seat Search */
.seat-finder {{
  display: flex;
  align-items: center;
  background: rgba(4, 18, 44, 0.85);
  border: 1px solid rgba(135, 175, 235, 0.35);
  border-radius: 8px;
  padding: 4px 8px 4px 12px;
  transition: all 0.2s ease;
}}
.seat-finder:focus-within {{
  border-color: var(--gold-primary);
  box-shadow: 0 0 0 2px rgba(242, 195, 85, 0.3);
}}
.seat-finder span {{
  font-size: 12px;
  font-weight: 700;
  color: var(--gold-light);
  margin-right: 6px;
}}
.seat-finder input {{
  width: 90px;
  background: transparent;
  border: 0;
  outline: 0;
  color: #fff;
  font-size: 13.5px;
  font-weight: 700;
  font-family: var(--font-main);
  font-variant-numeric: tabular-nums;
}}
.seat-finder input::placeholder {{ color: #6e8bb5; font-weight: 500; }}
.btn-clear-search {{
  background: rgba(255, 255, 255, 0.12);
  border: 0;
  color: #e2eeff;
  border-radius: 5px;
  padding: 2px 7px;
  font-size: 11px;
  font-weight: 700;
  cursor: pointer;
  display: none;
}}
.btn-clear-search.show {{ display: inline-block; }}

.btn-ui {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 13px;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  border: 1px solid rgba(132, 172, 230, 0.35);
  background: linear-gradient(180deg, #133363 0%, #0a1f42 100%);
  color: #f0f6ff;
  transition: all 0.18s ease;
}}
.btn-ui:hover {{
  background: linear-gradient(180deg, #1c4585 0%, #102d5e 100%);
  border-color: var(--gold-light);
  transform: translateY(-1px);
}}
.btn-ui.primary {{
  border-color: #ffe699;
  background: linear-gradient(180deg, #f7d268 0%, #d89f31 100%);
  color: #071938;
  font-weight: 800;
  box-shadow: 0 4px 14px rgba(216, 159, 49, 0.4);
}}
.btn-ui.primary:hover {{
  background: linear-gradient(180deg, #ffde85 0%, #e2ab3d 100%);
}}

/* Main Display Viewport Area */
.display-wrapper {{
  position: relative;
  width: 100%;
  min-height: calc(100vh - 60px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 14px;
  background: radial-gradient(ellipse at 50% 15%, #0d2854 0%, #051433 55%, #020712 100%);
}}

.aspect-container {{
  position: relative;
  width: 100%;
  max-width: calc((100vh - 88px) * 16 / 9);
  aspect-ratio: 16 / 9;
  box-shadow: 0 24px 80px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(242, 195, 85, 0.45);
  border-radius: 12px;
  overflow: hidden;
  background: #020817;
}}

.aspect-container:fullscreen {{
  max-width: none;
  width: 100vw;
  height: 100vh;
  border-radius: 0;
  border: 0;
  background: #000;
}}
.aspect-container:-webkit-full-screen {{
  max-width: none;
  width: 100vw;
  height: 100vh;
  border-radius: 0;
}}

.aspect-container svg {{
  display: block;
  width: 100%;
  height: 100%;
  font-family: var(--font-main);
}}

/* Floating Mini-Dock for TV 43" & LED Interactive Access */
.fullscreen-dock {{
  display: none;
  position: absolute;
  top: 18px;
  right: 24px;
  z-index: 150;
  align-items: center;
  gap: 10px;
  background: rgba(6, 21, 51, 0.92);
  backdrop-filter: blur(14px);
  border: 1px solid rgba(242, 195, 85, 0.45);
  padding: 6px 14px;
  border-radius: 12px;
  box-shadow: 0 10px 32px rgba(0, 0, 0, 0.7);
  opacity: 0;
  transform: translateY(-10px);
  transition: opacity 0.3s ease, transform 0.3s ease;
  pointer-events: none;
}}
.aspect-container:fullscreen .fullscreen-dock,
.aspect-container:-webkit-full-screen .fullscreen-dock {{
  display: flex;
}}
.aspect-container:fullscreen .fullscreen-dock:hover,
.aspect-container:-webkit-full-screen .fullscreen-dock:hover,
.fullscreen-dock:hover {{
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}}

/* Configuration Slide Drawer */
.config-drawer {{
  position: fixed;
  top: 72px;
  right: 24px;
  width: 360px;
  max-height: calc(100vh - 96px);
  overflow-y: auto;
  background: linear-gradient(165deg, rgba(8, 25, 58, 0.96), rgba(4, 15, 36, 0.98));
  backdrop-filter: blur(18px);
  border: 1px solid rgba(242, 195, 85, 0.4);
  border-radius: 14px;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.7);
  padding: 22px 20px;
  z-index: 200;
  display: none;
}}
.config-drawer.open {{ display: block; animation: drawerFade 0.25s ease-out; }}
@keyframes drawerFade {{
  from {{ opacity: 0; transform: translateY(-10px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}

.config-drawer h2 {{
  font-size: 16px;
  font-weight: 800;
  color: var(--gold-light);
  margin: 0 0 8px;
}}
.config-note {{
  font-size: 12px;
  color: #92b1dc;
  line-height: 1.5;
  margin: 0 0 16px;
}}
.stat-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin-bottom: 18px;
}}
.stat-box {{
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(135, 175, 235, 0.2);
  border-radius: 9px;
  padding: 8px 4px;
  text-align: center;
}}
.stat-box strong {{
  font-size: 18px;
  display: block;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}}
.stat-box.gold strong {{ color: var(--due-yellow); }}
.stat-box.purple strong {{ color: #e19dff; }}
.stat-box.orange strong {{ color: var(--due-orange); }}
.stat-box span {{
  font-size: 10px;
  color: #8da9d0;
  font-weight: 700;
}}

.form-group {{ margin-bottom: 14px; }}
.form-group label {{
  display: flex;
  justify-content: space-between;
  font-size: 12.5px;
  font-weight: 700;
  color: #dbe8fa;
  margin-bottom: 6px;
}}
.form-group input {{
  width: 100%;
  background: rgba(3, 12, 28, 0.9);
  border: 1px solid rgba(135, 175, 235, 0.4);
  border-radius: 8px;
  padding: 9px 12px;
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  font-family: var(--font-main);
}}
.form-group input:focus {{
  outline: 2px solid var(--gold-primary);
  border-color: transparent;
}}
.form-group input:disabled {{
  opacity: 0.65;
  background: rgba(255, 255, 255, 0.04);
}}
.btn-drawer-row {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-top: 14px;
}}
.btn-sub {{
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(135, 175, 235, 0.3);
  color: #e2edfd;
  border-radius: 8px;
  padding: 8px;
  font-size: 12px;
  font-weight: 700;
  font-family: var(--font-main);
  cursor: pointer;
  transition: all 0.15s;
}}
.btn-sub:hover {{
  background: rgba(242, 195, 85, 0.2);
  border-color: var(--gold-light);
  color: #fff;
}}

/* Toast Message */
#toast {{
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: linear-gradient(135deg, #0d2856, #061530);
  border: 1px solid var(--gold-primary);
  color: #fff8e7;
  padding: 12px 20px;
  border-radius: 10px;
  font-size: 13.5px;
  font-weight: 700;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.7);
  z-index: 300;
  opacity: 0;
  transform: translateY(10px);
  pointer-events: none;
  transition: all 0.25s ease;
}}
#toast.show {{ opacity: 1; transform: translateY(0); }}

/* SVG Dynamic Animations & Interactive Highlights */
.seat, .vip-row.phd-row {{
  cursor: pointer;
  transition: filter 0.15s ease;
}}
.seat rect, .vip-row.phd-row rect {{
  cursor: pointer;
}}
.seat:hover rect {{
  stroke: #ffffff !important;
  stroke-width: 2.4px !important;
  filter: brightness(1.15);
}}
.vip-row.phd-row:hover rect {{
  stroke: #ffea9f !important;
  stroke-width: 2.2px !important;
  filter: brightness(1.15);
}}
.seat text {{
  pointer-events: none;
  font-variant-numeric: tabular-nums;
  user-select: none;
}}

@keyframes seatPulseGlow {{
  0%, 100% {{
    transform: scale(1);
    filter: drop-shadow(0 0 0 rgba(255, 220, 0, 0));
  }}
  50% {{
    transform: scale(1.35);
    filter: drop-shadow(0 0 14px rgba(255, 230, 0, 1)) drop-shadow(0 0 24px rgba(255, 160, 0, 0.9));
  }}
}}
.seat.highlight {{
  transform-box: fill-box;
  transform-origin: center;
  animation: seatPulseGlow 0.85s ease-in-out infinite;
}}
.seat.highlight rect {{
  stroke: #ffffff !important;
  stroke-width: 3.2px !important;
}}

/* Motion Graphics: Animated Glowing Flow Stream */
.flow-stream {{
  fill: none;
  stroke: #ffeaa7;
  stroke-width: 3.2;
  stroke-dasharray: 12 28;
  stroke-linecap: round;
  opacity: 0.95;
  filter: drop-shadow(0 0 4px #ffb300) drop-shadow(0 0 8px #ff7b00);
  animation: streamAnim 1.6s linear infinite;
}}
@keyframes streamAnim {{
  to {{ stroke-dashoffset: -80; }}
}}

/* Subtle Stage Spotlight Cones Animation */
@keyframes spotSwayLeft {{
  0%, 100% {{ opacity: 0.28; transform: rotate(0deg); }}
  50% {{ opacity: 0.42; transform: rotate(1.8deg); }}
}}
@keyframes spotSwayRight {{
  0%, 100% {{ opacity: 0.28; transform: rotate(0deg); }}
  50% {{ opacity: 0.42; transform: rotate(-1.8deg); }}
}}
.spotlight-left {{
  transform-origin: 800px 0px;
  animation: spotSwayLeft 6s ease-in-out infinite;
}}
.spotlight-right {{
  transform-origin: 1120px 0px;
  animation: spotSwayRight 6s ease-in-out infinite;
}}


/* Pulsing PhD Row Highlight on Diagram */
.vip-row.phd-row.highlight rect {{
  stroke: #ffea9f !important;
  stroke-width: 4px !important;
  animation: phdRowGlow 1.2s ease-in-out infinite alternate !important;
}}
@keyframes phdRowGlow {{
  0% {{
    filter: drop-shadow(0 0 6px #ffcc00);
  }}
  100% {{
    filter: drop-shadow(0 0 24px #ff2222) drop-shadow(0 0 10px #ffe599);
  }}
}}
.vip-row.phd-row.highlight text {{
  fill: #fffdf5 !important;
  filter: drop-shadow(0 0 4px #ffd700);
}}

/* Fireworks above honors plaque animation */
.honors-fireworks-anim {{
  animation: honorsFwBreathe 3.5s ease-in-out infinite alternate;
  transform-origin: 200px 180px;
}}
@keyframes honorsFwBreathe {{
  0% {{
    opacity: 0.85;
    filter: drop-shadow(0 0 6px rgba(255, 215, 0, 0.45));
    transform: scale(0.98);
  }}
  50% {{
    opacity: 1;
    filter: drop-shadow(0 0 16px rgba(255, 230, 120, 0.85));
    transform: scale(1.02);
  }}
  100% {{
    opacity: 0.9;
    filter: drop-shadow(0 0 8px rgba(255, 200, 50, 0.6));
    transform: scale(1);
  }}
}}



/* Real Particle Canvas Fireworks Overlay */
.fireworks-canvas {{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 10;
}}

/* Top Honors Plaque & Name Card Overlay (Floating on top of fireworks) */
.top-honors-svg {{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 20;
}}

/* Luxury 3D Award Ribbon Pulse Animation */
@keyframes awardRibbonGlow {{
  0%, 100% {{
    filter: drop-shadow(0 0 4px rgba(255, 215, 0, 0.6));
  }}
  50% {{
    filter: drop-shadow(0 0 12px rgba(255, 220, 80, 0.95)) drop-shadow(0 0 20px rgba(255, 180, 0, 0.5));
  }}
}}
.award-ribbon-active {{
  animation: awardRibbonGlow 2.2s infinite ease-in-out;
}}

/* Turn off all effects toggle */
.effects-off .flow-stream,
.effects-off .spotlight-left,
.effects-off .spotlight-right {{
  display: none !important;
}}
</style>
</head>
<body>

<!-- TOP MANAGEMENT TOOLBAR -->
<header class="toolbar" id="mainToolbar">
  <div class="brand-title">
    <span class="brand-badge">DUE 2026</span>
    <div>
      <span class="brand-text">LỄ TRAO BẰNG TỐT NGHIỆP — ĐỢT 3 NĂM 2026</span>
      <span class="brand-sub">Đại học Kinh tế - ĐHĐN • Màn hình 1920×1080</span>
    </div>
  </div>

  <div class="toolbar-controls">
    <!-- Quick Seat Search -->
    <div class="seat-finder">
      <span>📍 Ghế số:</span>
      <input type="text" id="quickSeatInput" placeholder="Số ghế" autocomplete="off">
      <button class="btn-clear-search" id="btnClearQuickSeat" title="Xóa tìm kiếm">✕</button>
    </div>

    <!-- Honors Presentation Quick Actions -->
    <input type="file" id="honorsExcelInput" accept=".xlsx, .xls, .csv" style="display:none">
    <button class="btn-ui" id="btnToolbarImportExcel" title="Nhập danh sách tân khoa từ file Excel / CSV">📥 Nhập Excel</button>
    <button class="btn-ui" id="btnToolbarDownloadTemplate" title="Tải file Excel mẫu (.xlsx)">📄 Tải mẫu Excel</button>
    <button class="btn-ui" id="btnToolbarToggleHonors" title="Bật / Tạm dừng trình chiếu vinh danh">⏯ Vinh danh: Đang chạy</button>

    <button class="btn-ui" id="btnToggleConfig" title="Mở bảng chỉnh số lượng ghế">⚙ Cấu hình</button>
    <button class="btn-ui" id="btnToggleFx" title="Bật / Tắt hiệu ứng chuyển động">✦ Hiệu ứng: Bật</button>
    <button class="btn-ui" id="btnExportPng" title="Xuất ảnh PNG 1920 × 1080 cực nét">📷 Xuất PNG</button>
    <button class="btn-ui primary" id="btnFullscreen" title="Bật toàn màn hình phát trên TV / LED (Phím F)">⛶ Trình chiếu</button>
  </div>
</header>

<!-- MAIN VIEWPORT CONTAINER (16:9 PROPORTION FOR 1920×1080 TV / LED) -->
<main class="display-wrapper">
  <div class="aspect-container" id="stageWrapper">

    <!-- Fullscreen Floating Mini-Dock for TV 43" & LED Interactive Access -->
    <div class="fullscreen-dock" id="fsDock">
      <div class="seat-finder">
        <span>📍 Tìm ghế:</span>
        <input type="text" id="fsSeatInput" placeholder="Số ghế" autocomplete="off">
      </div>
      <button class="btn-ui" id="btnFsToggleFx">✦ Hiệu ứng</button>
      <button class="btn-ui" id="btnFsExit" title="Thoát chế độ toàn màn hình (ESC hoặc F)">✕ Thoát</button>
    </div>

    <!-- 1. MASTER SVG SEATING CHART (1920 × 1080 NATIVE COORDINATES - BASE LAYER) -->
    <svg id="masterSvg" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Canvas Background Gradients -->
        <radialGradient id="navyCanvas" cx="50%" cy="30%" r="75%">
          <stop offset="0%" stop-color="#082352"/>
          <stop offset="45%" stop-color="#051739"/>
          <stop offset="85%" stop-color="#020a1c"/>
          <stop offset="100%" stop-color="#010612"/>
        </radialGradient>

        <linearGradient id="innerCardBg" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#ffffff"/>
          <stop offset="60%" stop-color="#fdfbf7"/>
          <stop offset="100%" stop-color="#f5efe2"/>
        </linearGradient>

        <!-- Red Carpet Gradient (Thảm đỏ hoàng gia) -->
        <linearGradient id="redCarpetGrad" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="#8a040f"/>
          <stop offset="10%" stop-color="#b60d1b"/>
          <stop offset="50%" stop-color="#db1c2b"/>
          <stop offset="90%" stop-color="#b60d1b"/>
          <stop offset="100%" stop-color="#8a040f"/>
        </linearGradient>

        <!-- Gold Metal Foil Gradients -->
        <linearGradient id="goldTextGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#fff5cf"/>
          <stop offset="25%" stop-color="#ffd875"/>
          <stop offset="50%" stop-color="#eaac3e"/>
          <stop offset="75%" stop-color="#ffd875"/>
          <stop offset="100%" stop-color="#b87b1a"/>
        </linearGradient>

        <linearGradient id="goldBorderGrad" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="#b88328"/>
          <stop offset="20%" stop-color="#ffe699"/>
          <stop offset="50%" stop-color="#d49532"/>
          <stop offset="80%" stop-color="#fff1be"/>
          <stop offset="100%" stop-color="#996310"/>
        </linearGradient>

        <!-- Continuous Royal Gold Header Ribbon Gradient (Luminous 3D Metallic) -->
        <linearGradient id="headerRibbonGoldGrad" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="#d49b32"/>
          <stop offset="15%" stop-color="#ffe8a3"/>
          <stop offset="30%" stop-color="#ffd54f"/>
          <stop offset="50%" stop-color="#fff7d6"/>
          <stop offset="70%" stop-color="#ffd54f"/>
          <stop offset="85%" stop-color="#ffe8a3"/>
          <stop offset="100%" stop-color="#c98a20"/>
        </linearGradient>

        <filter id="headerRibbonShadow" x="-5%" y="-20%" width="110%" height="200%">
          <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#020a1c" flood-opacity="0.45"/>
        </filter>

        <!-- Stage DUE Royal Blue Gradient -->
        <linearGradient id="stageGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#005EA3"/>
          <stop offset="50%" stop-color="#004378"/>
          <stop offset="100%" stop-color="#002b52"/>
        </linearGradient>

        <!-- Spotlight Cones Gradient -->
        <linearGradient id="spotlightConeGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#fff4cf" stop-opacity="0.35"/>
          <stop offset="65%" stop-color="#ffe494" stop-opacity="0.1"/>
          <stop offset="100%" stop-color="#ffdc73" stop-opacity="0"/>
        </linearGradient>

        <!-- OFFICIAL DUE BRAND SEATING GRADIENTS (ENHANCED TEXTURE & HARMONY) -->
        <!-- VIP / Delegates Green (DUE Xanh Lá #058E47) -->
        <linearGradient id="vipGreen" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#0aa855"/>
          <stop offset="55%" stop-color="#058E47"/>
          <stop offset="100%" stop-color="#036331"/>
        </linearGradient>

        <!-- PhD / Doctor Red (#B90C1A) -->
        <linearGradient id="phdRed" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#d91829"/>
          <stop offset="55%" stop-color="#B90C1A"/>
          <stop offset="100%" stop-color="#8a040f"/>
        </linearGradient>

        <!-- Awards / Khen Thuong Yellow (DUE Vàng #FFB612) -->
        <linearGradient id="awardYellow" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#ffd466"/>
          <stop offset="55%" stop-color="#FFB612"/>
          <stop offset="100%" stop-color="#e59f00"/>
        </linearGradient>

        <!-- Master / Thac Si Purple (#7C1FA3) -->
        <linearGradient id="masterPurple" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#9c32c9"/>
          <stop offset="55%" stop-color="#7C1FA3"/>
          <stop offset="100%" stop-color="#550978"/>
        </linearGradient>

        <!-- Bachelor / Cu Nhan Orange (DUE Cam #EE6323) -->
        <linearGradient id="bachelorOrange" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#ff7c3b"/>
          <stop offset="55%" stop-color="#EE6323"/>
          <stop offset="100%" stop-color="#c74708"/>
        </linearGradient>

        <!-- Family Guest Light Gray (#DCE5F0) -->
        <linearGradient id="familyGray" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#f5f8fc"/>
          <stop offset="100%" stop-color="#d8e3ef"/>
        </linearGradient>

        <!-- Shadows & Filters -->
        <filter id="goldGlow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="3" stdDeviation="3.5" flood-color="#010714" flood-opacity="0.85"/>
        </filter>
        <filter id="softCardDrop" x="-10%" y="-10%" width="120%" height="120%">
          <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#02091c" flood-opacity="0.6"/>
        </filter>

        <!-- Shadow filter for crisp white text on royal navy plaque -->
        <filter id="nameGlowDrop" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#010614" flood-opacity="0.95"/>
        </filter>



        <!-- Multi-stop luxury metallic gold gradient for Awards -->
        <linearGradient id="royalAwardGoldGrad" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#fff9d6"/>
          <stop offset="25%" stop-color="#ffd54f"/>
          <stop offset="50%" stop-color="#ffb300"/>
          <stop offset="75%" stop-color="#ff8f00"/>
          <stop offset="100%" stop-color="#ffca28"/>
        </linearGradient>

        <linearGradient id="ribbonTailDarkGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#d48800"/>
          <stop offset="100%" stop-color="#8f5700"/>
        </linearGradient>

        <filter id="awardMedalDrop" x="-30%" y="-30%" width="160%" height="160%">
          <feDropShadow dx="0" dy="2.5" stdDeviation="3" flood-color="#4a2a00" flood-opacity="0.5"/>
        </filter>
        <filter id="carpetShadow" x="-20%" y="-5%" width="140%" height="110%">
          <feDropShadow dx="0" dy="2" stdDeviation="3.5" flood-color="#010817" flood-opacity="0.45"/>
        </filter>
        <filter id="stageDrop" x="-10%" y="-10%" width="120%" height="130%">
          <feDropShadow dx="0" dy="6" stdDeviation="7" flood-color="#000000" flood-opacity="0.6"/>
        </filter>

        <!-- Red Flow Arrow Marker -->
        <marker id="markerArrowRed" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
          <path d="M1 1.5 L10.5 6 L1 10.5 Z" fill="#e01623" stroke="#ffcccc" stroke-width="0.6"/>
        </marker>
      </defs>

      <!-- ================= BACKGROUND CANVAS ================= -->
      <rect x="0" y="0" width="1920" height="1080" fill="url(#navyCanvas)"/>

      <!-- Stage Spotlight Cones Lighting (Projecting Down to Stage) -->
      <g id="spotlightsGroup" pointer-events="none">
        <polygon class="spotlight-left" points="800,0 560,260 980,260" fill="url(#spotlightConeGrad)"/>
        <polygon class="spotlight-right" points="1120,0 940,260 1360,260" fill="url(#spotlightConeGrad)"/>
      </g>

      <!-- ================= MAIN AUDITORIUM INNER CARD ================= -->
      <!-- Expanded Horizontally: Symmetrical 28px margins on Left, Right & Bottom (X = 28, Width = 1864) -->
      <g filter="url(#softCardDrop)">
        <rect x="28" y="134" width="1864" height="918" rx="20" fill="url(#innerCardBg)" stroke="url(#goldBorderGrad)" stroke-width="3.2"/>
        <rect x="34" y="140" width="1852" height="906" rx="16" fill="none" stroke="#d5be8a" stroke-width="1.2" opacity="0.55"/>
      </g>

      <!-- ================= HIGH-QUALITY TRANSPARENT ARTWORK LAYERS ================= -->
      <!-- 2. Transparent Campus Building & Foliage (Bottom Right - 3x larger, flush with bottom border) -->
      <image href="{b64_campus}" x="1160" y="915" width="832" height="200" preserveAspectRatio="xMidYMid meet" pointer-events="none"/>

      <!-- 4. Congratulations Graduates Typography Graphic (Bottom Right - below GHI CHÚ box) -->
      <image href="{b64_congrats}" x="-60" y="915" width="570" height="190" preserveAspectRatio="xMidYMid meet" filter="url(#goldGlow)" pointer-events="none"/>

      <!-- ================= HEADER SECTION ================= -->
      <!-- 1. Top Royal Blue Arc Banner Background -->
      <path d="M 0,0 L 1920,0 L 1920,86 C 1560,108 1240,128 960,128 C 680,128 360,108 0,86 Z" fill="url(#stageGrad)"/>

      <!-- OFFICIAL DUE LOGO (Top Left Header, placed neatly above ribbon) -->
      <image href="{b64_logo}" x="75" y="6" width="82" height="82" filter="url(#goldGlow)" pointer-events="none"/>

      <!-- 3D Graduation Cap & Diploma Scroll (Next to Logo, sits gracefully in banner) -->
      <image href="{b64_cap}" x="175" y="4" width="148" height="110" filter="url(#goldGlow)" pointer-events="none"/>

      <!-- Continuous 3D Royal Gold Ribbon & Accents (Luminous, unbroken vector curve across all 1920px) -->
      <g filter="url(#headerRibbonShadow)">
        <!-- Main Golden Ribbon Body (14px thickness, smooth cubic bezier C1 continuous) -->
        <path d="M 0,86 C 360,108 680,128 960,128 C 1240,128 1560,108 1920,86 L 1920,100 C 1560,122 1240,142 960,142 C 680,142 360,122 0,100 Z" fill="url(#headerRibbonGoldGrad)"/>

        <!-- Upper Highlight Rim (Bright Gold 1.8px) -->
        <path d="M 0,86 C 360,108 680,128 960,128 C 1240,128 1560,108 1920,86" fill="none" stroke="#fffce6" stroke-width="1.8"/>

        <!-- Lower Shading Contour Rim (Deep Gold 1.5px) -->
        <path d="M 0,100 C 360,122 680,142 960,142 C 1240,142 1560,122 1920,100" fill="none" stroke="#b37e1b" stroke-width="1.5"/>

        <!-- Delicate Secondary Floating Accent Arc (4px below main ribbon) -->
        <path d="M 40,106 C 380,127 690,147 960,147 C 1230,147 1540,127 1880,106" fill="none" stroke="url(#headerRibbonGoldGrad)" stroke-width="1.3" opacity="0.8"/>
      </g>

      <!-- Fireworks Artwork (Top Right - Rendered ON TOP of the golden ribbon per user request) -->
      <image href="{b64_fw}" x="1260" y="-10" width="660" height="495" preserveAspectRatio="xMidYMid meet" pointer-events="none"/>

      <!-- Laurel Leaves framing Main Title (Shifted down to Y=68 for balanced top margin) -->
      <g id="laurelLeafSet" transform="translate(605, 68)" filter="url(#goldGlow)">
        <path d="M 0,20 Q -20,5 -16,-28" stroke="#f2c355" stroke-width="3" fill="none"/>
        <path d="M -5,8 Q -24,12 -28,0 Q -12,-3 -5,8 Z" fill="#ffdf7e"/>
        <path d="M -11,-3 Q -30,-4 -28,-16 Q -14,-13 -11,-3 Z" fill="#f5be46"/>
        <path d="M -15,-16 Q -28,-24 -22,-35 Q -11,-29 -15,-16 Z" fill="#ffdf7e"/>
        <path d="M -13,-20 Q 0,-25 -2,-38 Q -15,-34 -13,-20 Z" fill="#e5a832"/>
      </g>
      <!-- Symmetrical Mirror Laurel Leaf Set for Right Side (Center X = 960) -->
      <use href="#laurelLeafSet" transform="translate(1920, 0) scale(-1, 1)"/>

      <!-- Main Header Typography (Centered at X = 960, balanced vertical spacing) -->
      <text x="960" y="68" font-size="50" font-weight="900" letter-spacing="2.5" fill="url(#goldTextGrad)" stroke="#52320b" stroke-width="0.8" text-anchor="middle" filter="url(#goldGlow)">SƠ ĐỒ CHỖ NGỒI</text>
      <text x="960" y="112" font-size="22" font-weight="700" fill="#ffffff" letter-spacing="1.2" text-anchor="middle" filter="url(#goldGlow)">LỄ TRAO BẰNG TỐT NGHIỆP TIẾN SĨ, THẠC SĨ, CỬ NHÂN ĐỢT 3 NĂM 2026</text>


      <!-- ================= SÂN KHẤU (PERFECTLY CENTERED AT X = 960, NO ARROWS ON STAGE) ================= -->
      <!-- Centered Stage Box (Width = 800, X: 560 to 1360, Center = 960) -->
      <g filter="url(#stageDrop)">
        <rect x="560" y="152" width="800" height="76" rx="16" fill="url(#stageGrad)" stroke="#ffea9f" stroke-width="4.5"/>
        <rect x="566" y="158" width="788" height="64" rx="12" fill="none" stroke="#e0aa40" stroke-width="2"/>
        <path d="M 580,214 Q 960,228 1340,214" stroke="#ffd978" stroke-width="2.2" opacity="0.45" fill="none"/>
        <text x="960" y="204" dominant-baseline="middle" text-anchor="middle" fill="#ffffff" font-size="44" font-weight="900" letter-spacing="4" filter="url(#goldGlow)">SÂN KHẤU</text>
      </g>

      <!-- Left Backstage Wing (Cánh gà trái) -->
      <g filter="url(#stageDrop)">
        <rect x="430" y="158" width="115" height="64" rx="12" fill="url(#stageGrad)" stroke="#ffea9f" stroke-width="2.5"/>
        <rect x="434" y="162" width="107" height="56" rx="9" fill="none" stroke="#689cf0" stroke-width="1.2"/>
        <text x="487" y="185" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">Cánh gà</text>
        <text x="487" y="208" text-anchor="middle" fill="#ffe188" font-size="16" font-weight="800">trái</text>
      </g>

      <!-- Right Backstage Wing (Cánh gà phải) -->
      <g filter="url(#stageDrop)">
        <rect x="1375" y="158" width="115" height="64" rx="12" fill="url(#stageGrad)" stroke="#ffea9f" stroke-width="2.5"/>
        <rect x="1379" y="162" width="107" height="56" rx="9" fill="none" stroke="#689cf0" stroke-width="1.2"/>
        <text x="1432" y="185" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">Cánh gà</text>
        <text x="1432" y="208" text-anchor="middle" fill="#ffe188" font-size="16" font-weight="800">phải</text>
      </g>


      <!-- ================= GRAND RED CARPET (THẢM ĐỎ DANH DỰ TỪ DÃY 1 ĐẾN HẾT KHỐI NGƯỜI THÂN) ================= -->
      <!-- Center X = 960, Width = 46, X: 937 to 983, Y: 256 to 892 (tự động co giãn theo đáy khối người thân) -->
      <g id="redCarpetAisle" filter="url(#carpetShadow)">
        <rect id="redCarpetRect" x="937" y="256" width="46" height="636" rx="4" fill="url(#redCarpetGrad)"/>
        <!-- Gold Trim Borders along the edges of the Red Carpet -->
        <line id="redCarpetTrimLeft" x1="938" y1="256" x2="938" y2="892" stroke="#f2c355" stroke-width="1.8" stroke-dasharray="8 4"/>
        <line id="redCarpetTrimRight" x1="982" y1="256" x2="982" y2="892" stroke="#f2c355" stroke-width="1.8" stroke-dasharray="8 4"/>
      </g>


      <!-- ================= ROW NUMBER COLUMNS (DÃY 1 – 23) ================= -->
      <!-- Left Row Column (X: 454) | Right Row Column (X: 1420) -->
      <g id="rowNumbersLeft"></g>
      <g id="rowNumbersRight"></g>


      <!-- ================= SEATING BLOCKS (SYMMETRICALLY CENTERED) ================= -->
      <!-- Dãy 1–4: VIP / Đại biểu & NCS -->
      <g id="vipBlock"></g>

      <!-- Dãy 5–18: 280 Numbered Physical Seats (10 Seats x 14 Rows in 2 Blocks) -->
      <g id="seatBlock"></g>

      <!-- Dãy 19–23: Người thân Tân TS / ThS / ĐH -->
      <g id="familyBlock"></g>


      <!-- Bảng Vinh Danh đã được đưa lên lớp trên cùng (#topHonorsSvg z-index: 20) để nổi lên trên pháo hoa -->

      <!-- ================= COMPACT WC & LỐI VÀO (MINI BADGES SÁT LUỒNG MŨI TÊN X=390, NO DROP SHADOW) ================= -->
      <!-- Sleek Mini WC Badge (Width: 42, Height: 42, at X: 338, Y: 718, gap to arrow line X=390 is 10px) -->
      <g id="wcMarker">
        <rect x="338" y="718" width="42" height="42" rx="7" fill="#ffffff" stroke="#005EA3" stroke-width="1.6"/>
        <!-- Male Pictogram -->
        <circle cx="351" cy="728" r="2.8" fill="#005EA3"/>
        <path d="M 347,732.5 L 355,732.5 L 354,743 L 352,743 L 352,750 L 350,750 L 350,743 L 348,743 Z" fill="#005EA3"/>
        <!-- Female Pictogram -->
        <circle cx="367" cy="728" r="2.8" fill="#005EA3"/>
        <path d="M 363,732.5 L 371,732.5 L 372.5,742 L 369.5,742 L 369.5,750 L 368,750 L 368,742 L 366,742 L 366,750 L 364.5,750 L 364.5,742 L 361.5,742 Z" fill="#005EA3"/>
        <!-- Divider -->
        <line x1="359" y1="726" x2="359" y2="749" stroke="#d5e0f2" stroke-width="0.8"/>
        <!-- WC Text -->
        <text x="359" y="756" text-anchor="middle" fill="#005EA3" font-size="8.5" font-weight="900" letter-spacing="0.5">WC</text>
      </g>

      <!-- Sleek Mini Lối vào Badge (Width: 64, Height: 26, at X: 316, Y: 770, gap to arrow line X=390 is 10px) -->
      <g id="entrancePill">
        <rect x="316" y="770" width="64" height="26" rx="6" fill="url(#stageGrad)" stroke="#ffea9f" stroke-width="1.4"/>
        <text x="343" y="787" text-anchor="middle" fill="#ffffff" font-size="11.5" font-weight="800" letter-spacing="0.3">Lối vào</text>
        <path d="M 363,783 L 373,783 M 369,779 L 373,783 L 369,787" stroke="#ffe599" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      </g>


      <!-- ================= FLOW NAVIGATION ARROWS & GLOW TRAILS (SYMMETRIC & BALANCED) ================= -->
      <!-- Strict One-Way Circulation:
           1. Left Block: Exit into Hallway (Length = 64px) -> Ascend to Left Wing -> Onto Stage
           2. Right Block: Exit into Hallway (Length = 64px) -> Descend to Back Hallway -> Cross Over Left -> Ascend to Left Wing
           3. NO ARROWS on Center Stage.
      -->
      <!-- Solid Arrow Lines Layer (Continuous unbroken lines, exactly 1 arrow per corridor run) -->
      <g id="flowArrowsGroup" fill="none" stroke="#e01623" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
        <!-- 1. Right Block Horizontal Exit into Right Hallway (stops cleanly at X=1518, 9px margin before vertical line, no overlap) -->
        <path id="arrowExitRight" d="M 1466, 410 L 1518, 410" marker-end="url(#markerArrowRed)"/>

        <!-- 2. Right Corridor: Unbroken continuous line from Right Wing down to bottom corridor, with ONLY 1 arrowhead at Y=620 -->
        <path d="M 1485, 222 Q 1530, 222 1530, 260 L 1530, 620" marker-end="url(#markerArrowRed)"/>
        <path d="M 1530, 620 L 1530, 905 Q 1530, 934 1490, 934"/>

        <!-- 3. Bottom Corridor: Unbroken continuous line from Right to Left, with ONLY 1 arrowhead at center X=960 -->
        <path d="M 1490, 934 L 960, 934" marker-end="url(#markerArrowRed)"/>
        <path d="M 960, 934 L 430, 934"/>

        <!-- 4. Left Corridor: Unbroken continuous line from bottom corner up to Left Wing, with 1 arrowhead at Y=620 and 1 entering Left Wing -->
        <path d="M 430, 934 Q 390, 934 390, 895 L 390, 620" marker-end="url(#markerArrowRed)"/>
        <path d="M 390, 620 L 390, 248 Q 390, 222 430, 222" marker-end="url(#markerArrowRed)"/>

        <!-- 5. Left Block Horizontal Exit into Left Hallway (stops cleanly at X=402, 9px margin before vertical line, no overlap) -->
        <path id="arrowExitLeft" d="M 454, 410 L 402, 410" marker-end="url(#markerArrowRed)"/>
      </g>

      <!-- Animated Glowing Photon Streams along the Paths (tự động căn giữa theo hàng tân khoa đầu tiên) -->
      <g id="flowGlowingTrails" pointer-events="none">
        <path id="streamExitRight" class="flow-stream" d="M 1466, 410 L 1518, 410"/>
        <path class="flow-stream" d="M 1485, 222 Q 1530, 222 1530, 260 L 1530, 905 Q 1530, 934 1490, 934" style="animation-delay: -0.4s;"/>
        <path class="flow-stream" d="M 1490, 934 L 430, 934" style="animation-delay: -0.9s;"/>
        <path class="flow-stream" d="M 430, 934 Q 390, 934 390, 895 L 390, 248 Q 390, 222 430, 222" style="animation-delay: -1.3s;"/>
        <path id="streamExitLeft" class="flow-stream" d="M 454, 410 L 402, 410"/>
      </g>


      <!-- ================= COMPACT & ELEGANT LEGEND PANEL (RIGHT SIDE) ================= -->
      <!-- Width = 310, X: 1565 to 1875, Y: 224 to 876 -->
      <g id="legendPanel" transform="translate(1565, 224)" filter="url(#softCardDrop)">
        <rect x="0" y="0" width="310" height="650" rx="16" fill="#ffffff" stroke="url(#goldBorderGrad)" stroke-width="2.6"/>
        <rect x="5" y="5" width="300" height="640" rx="12" fill="#fcfaf4" stroke="#e2d3af" stroke-width="1"/>

        <!-- Legend Header -->
        <path d="M 5,5 L 305,5 C 305,5 305,52 305,52 C 260,58 190,60 155,60 C 120,60 50,58 5,52 Z" fill="url(#stageGrad)"/>
        <text x="155" y="38" text-anchor="middle" fill="url(#goldTextGrad)" font-size="24" font-weight="800" letter-spacing="1.5" filter="url(#goldGlow)">GHI CHÚ</text>

        <!-- 6 Category Swatches & Labels -->
        <g id="legendEntries"></g>

        <!-- Flow Direction Box (Bottom of Legend) -->
        <g transform="translate(14, 520)">
          <rect x="0" y="0" width="282" height="110" rx="10" fill="#fffdfa" stroke="#ebd3a7" stroke-width="1.6"/>
          <!-- Arrow with Flow Stream -->
          <g transform="translate(14, 55)">
            <line x1="0" y1="0" x2="48" y2="0" stroke="#e01623" stroke-width="4.5" stroke-linecap="round" marker-end="url(#markerArrowRed)"/>
            <line x1="0" y1="0" x2="48" y2="0" class="flow-stream" stroke-width="2.2"/>
          </g>
          <!-- Exact Required Caption -->
          <text x="72" y="38" fill="#142647" font-size="14" font-weight="800">Hướng di chuyển của</text>
          <text x="72" y="60" fill="#005EA3" font-size="14.5" font-weight="800">Tân Thạc sĩ, Tân Cử nhân</text>
          <text x="72" y="82" fill="#142647" font-size="14" font-weight="800">khi lên nhận bằng</text>
        </g>
      </g>
    </svg>

    <!-- 2. REAL CODE PARTICLE FIREWORKS CANVAS OVERLAY (1920 × 1080 - MIDDLE LAYER Z-INDEX 10) -->
    <canvas id="fireworksCanvas" width="1920" height="1080" class="fireworks-canvas"></canvas>

    <!-- 3. TOP HONORS OVERLAY SVG (1920 × 1080 - TOP LAYER Z-INDEX 20: THẺ TÊN NỔI LÊN TRÊN CÙNG) -->
    <svg id="topHonorsSvg" class="top-honors-svg" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Shadow filters for top layer plaque and text -->
        <filter id="topSoftCardDrop" x="-10%" y="-10%" width="120%" height="120%">
          <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#020a1c" flood-opacity="0.32"/>
        </filter>
        <filter id="topNameGlowDrop" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="2" stdDeviation="3.5" flood-color="#000000" flood-opacity="0.85"/>
        </filter>
        <filter id="nameGlowDrop" x="-30%" y="-30%" width="160%" height="160%">
          <feDropShadow dx="0" dy="2" stdDeviation="3.5" flood-color="#00081a" flood-opacity="0.95"/>
        </filter>
        <filter id="topAwardMedalDrop" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.5"/>
        </filter>

        <!-- Royal Award Metallic Gradient -->
        <linearGradient id="topRoyalAwardGoldGrad" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="#fff1b8"/>
          <stop offset="25%" stop-color="#ffd54f"/>
          <stop offset="50%" stop-color="#ffb300"/>
          <stop offset="75%" stop-color="#ffd54f"/>
          <stop offset="100%" stop-color="#fff1b8"/>
        </linearGradient>

        <!-- Ribbon Tails Dark Gradient -->
        <linearGradient id="topRibbonTailDarkGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#cc8a00"/>
          <stop offset="100%" stop-color="#664600"/>
        </linearGradient>

        <!-- Gold Border Gradient for Card -->
        <linearGradient id="topGoldBorderGrad" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#ffea9f"/>
          <stop offset="30%" stop-color="#d4af37"/>
          <stop offset="70%" stop-color="#aa820a"/>
          <stop offset="100%" stop-color="#ffea9f"/>
        </linearGradient>

        <!-- Star Stage Gradient -->
        <linearGradient id="topStageGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#0a2556"/>
          <stop offset="100%" stop-color="#03112b"/>
        </linearGradient>

        <!-- Seat Pill Level Color Gradients -->
        <linearGradient id="topPhdRed" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="#b71c1c"/>
          <stop offset="50%" stop-color="#8b0000"/>
          <stop offset="100%" stop-color="#5c0000"/>
        </linearGradient>
        <linearGradient id="topAwardYellow" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="#ffd54f"/>
          <stop offset="50%" stop-color="#ffb300"/>
          <stop offset="100%" stop-color="#ff8f00"/>
        </linearGradient>
        <linearGradient id="topMasterPurple" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="#7b1fa2"/>
          <stop offset="50%" stop-color="#512da8"/>
          <stop offset="100%" stop-color="#311b92"/>
        </linearGradient>
        <linearGradient id="topBachelorOrange" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="#f57c00"/>
          <stop offset="50%" stop-color="#e65100"/>
          <stop offset="100%" stop-color="#bf360c"/>
        </linearGradient>
      </defs>

      <!-- ================= BẢNG VINH DANH TÂN KHOA (THEO KHUNG TRÌNH ĐỘ & SỐ GHẾ) ================= -->
      <!-- Clean, Professional Presentation:
           1. Sparkling Fireworks Burst hovering above the Plaque
           2. Royal Honors Plaque (TanTiensi.png, TanThacsi.png, TanCunhan.png)
           3. Honoree Full Name within the plaque center open area (+ Optional Plaque Award Medal)
           4. Seat Number & Luxury 3D Award Ribbon Card directly below
      -->
      <g id="honorsSection" filter="url(#softCardDrop)">
        <!-- 1. Royal Honors Plaque (Width: 342, Height: 228, centered at X=209 between X=28 and X=390) -->
        <image id="honorsPlaqueImg" href="{b64_plaque_tiensi}" x="38" y="222" width="342" height="228" preserveAspectRatio="xMidYMid meet" pointer-events="none"/>

        <!-- 2. Honoree Full Name displayed in the open center area of the Plaque (Adjusted higher for vertical balance) -->
        <g id="honorsNameGroup" pointer-events="none">
          <text id="honorsPlaqueName1" x="209" y="342" fill="#ffffff" font-size="20.5" font-weight="900" letter-spacing="0.5" text-anchor="middle" filter="url(#nameGlowDrop)">TS. NGUYỄN VĂN AN</text>
          <text id="honorsPlaqueName2" x="209" y="364" fill="#ffffff" font-size="16.5" font-weight="900" letter-spacing="0.5" text-anchor="middle" filter="url(#nameGlowDrop)"></text>

          <!-- Distinction Award Badge directly on Plaque (Visible when Khen thưởng = true) -->
          <g id="plaqueAwardBadge" style="display:block;" transform="translate(209, 384)">
            <rect x="-68" y="-12" width="136" height="24" rx="12" fill="url(#royalAwardGoldGrad)" stroke="#ffffff" stroke-width="1.3" filter="url(#nameGlowDrop)"/>
            <text x="0" y="4.5" fill="#382000" font-size="11" font-weight="900" letter-spacing="0.8" text-anchor="middle">★ KHEN THƯỞNG ★</text>
          </g>
        </g>

        <!-- 3. Seat Number & Award Information Card (Positioned directly beneath the Plaque) -->
        <g id="honorsSeatCard" transform="translate(42, 464)">
          <!-- Outer Card Background with Gold Border -->
          <rect id="honorsSeatCardBg" x="0" y="0" width="334" height="166" rx="14" fill="#ffffff" stroke="url(#goldBorderGrad)" stroke-width="2.2"/>
          <rect x="4" y="4" width="326" height="158" rx="10" fill="#fcfbf7" stroke="#e8d8b5" stroke-width="1"/>

          <!-- Seat Number Badge Pill (Color matches seat category) -->
          <rect id="honorsSeatPillBg" x="27" y="14" width="280" height="52" rx="26" fill="url(#phdRed)" stroke="#ffe599" stroke-width="1.8"/>
          <text id="honorsSeatPillText" x="167" y="47" fill="#ffffff" font-size="23" font-weight="900" letter-spacing="1" text-anchor="middle">TS1</text>

          <!-- Seating Location Hint (Dãy, Khối, hoặc Hàng NCS) -->
          <rect x="22" y="76" width="290" height="34" rx="7" fill="#f0f5fc" stroke="#c0d4ed" stroke-width="1"/>
          <text id="honorsSeatLocation" x="167" y="98.5" fill="#005ea3" font-size="13.5" font-weight="800" text-anchor="middle">📍 Hàng NCS, GVHD &amp; Gia đình</text>

          <!-- High-End 3D Royal Award Ribbon Banner (Displayed if Khen thưởng = true) -->
          <g id="honorsAwardBadge" class="award-ribbon-active" transform="translate(18, 118)">
            <!-- Left Swallowtail Ribbon Tail -->
            <polygon points="4,7 24,0 24,34 4,27 12,17" fill="url(#ribbonTailDarkGrad)" stroke="#ffea9f" stroke-width="0.8"/>
            <!-- Right Swallowtail Ribbon Tail -->
            <polygon points="294,7 274,0 274,34 294,27 286,17" fill="url(#ribbonTailDarkGrad)" stroke="#ffea9f" stroke-width="0.8"/>

            <!-- Main Golden Ribbon Body -->
            <rect id="honorsAwardBadgeBg" x="18" y="0" width="262" height="34" rx="7" fill="url(#royalAwardGoldGrad)" stroke="#ffffff" stroke-width="1.4" filter="url(#awardMedalDrop)"/>
            <rect x="21" y="3" width="256" height="28" rx="5" fill="none" stroke="#ffe082" stroke-width="0.8"/>

            <!-- Left Gold Star Medal Icon -->
            <circle cx="32" cy="17" r="9.5" fill="url(#stageGrad)" stroke="#ffea9f" stroke-width="1.2"/>
            <text x="32" y="21" fill="#ffe082" font-size="11.5" font-weight="900" text-anchor="middle">★</text>

            <!-- Center Ribbon Banner Text (Tự động co chỉnh chống tràn trên mọi màn hình & font) -->
            <text id="honorsAwardBadgeText" x="149" y="21.5" fill="#3a1e00" font-size="11.2" font-weight="800" letter-spacing="0.3" text-anchor="middle">CÁ NHÂN ĐƯỢC KHEN THƯỞNG</text>

            <!-- Right Gold Star Medal Icon -->
            <circle cx="266" cy="17" r="9.5" fill="url(#stageGrad)" stroke="#ffea9f" stroke-width="1.2"/>
            <text x="266" y="21" fill="#ffe082" font-size="11.5" font-weight="900" text-anchor="middle">★</text>
          </g>
        </g>
      </g>
    </svg>
  </div>
</main>

<!-- CONFIGURATION SLIDE DRAWER (EDIT SEAT QUOTAS) -->
<aside class="config-drawer" id="configDrawer">
  <div style="background:linear-gradient(135deg, #021a40, #005EA3); margin:-28px -28px 20px -28px; padding:24px 28px; border-bottom:2px solid #ffd700; color:#ffffff;">
    <h2 style="margin:0 0 8px 0; color:#ffea9f; font-size:18px; letter-spacing:0.5px;">🎬 Cài Đặt Trình Chiếu Vinh Danh</h2>
    <p style="margin:0; font-size:12.5px; opacity:0.9;">Thiết đặt trước khi phát trên TV 43" &amp; LED</p>
  </div>

  <div style="background:#f4f8fe; border:1px solid #d0e1f7; border-radius:10px; padding:14px; margin-bottom:18px;">
    <label style="display:block; font-size:12.5px; font-weight:800; color:#005ea3; margin-bottom:8px;">⏱ Tốc độ chuyển người tự động:</label>
    <div style="display:flex; gap:6px; margin-bottom:12px;">
      <button class="btn-sub btn-speed-opt" id="btnDrawerSpeed1s" style="flex:1;">1 giây</button>
      <button class="btn-sub btn-speed-opt" id="btnDrawerSpeed2s" style="flex:1;">2 giây</button>
      <button class="btn-sub btn-speed-opt active" id="btnDrawerSpeed3s" style="flex:1; background:#005ea3; color:#fff; font-weight:800;">3 giây</button>
      <button class="btn-sub btn-speed-opt" id="btnDrawerSpeed5s" style="flex:1;">5 giây</button>
    </div>

    <label style="display:block; font-size:12.5px; font-weight:800; color:#005ea3; margin-bottom:8px;">🕹 Điều khiển vinh danh:</label>
    <div style="display:flex; gap:6px; margin-bottom:8px;">
      <button class="btn-sub" id="btnDrawerPrev" style="flex:1;" title="Phím ◄ hoặc PageUp">⏮ Trước</button>
      <button class="btn-sub" id="btnDrawerPlayPause" style="flex:1.2; background:#005ea3; color:#fff; font-weight:800;" title="Phím Space">⏸ Dừng</button>
      <button class="btn-sub" id="btnDrawerNext" style="flex:1;" title="Phím ► hoặc PageDown">⏭ Sau</button>
      <button class="btn-sub" id="btnDrawerFirst" style="flex:1;" title="Phím Home">⏪ Về đầu</button>
    </div>

    <!-- Nhập số để chuyển trực tiếp đến đúng số ghế / tân khoa mong muốn -->
    <div style="display:flex; align-items:center; gap:6px; margin-bottom:10px;">
      <input type="text" id="inputDrawerJumpNumber" placeholder="Nhập số ghế muốn đến (vd: 1, 15, TS1)..." style="flex:1; height:34px; padding:0 12px; font-size:12.5px; font-weight:700; color:#0c2652; background:#ffffff; border:1px solid #b8d2f2; border-radius:6px; outline:none;" />
      <button class="btn-sub" id="btnDrawerJumpNumber" style="height:34px; padding:0 12px; background:#005ea3; color:#ffffff; font-weight:800; border-radius:6px; white-space:nowrap; border:none; cursor:pointer;" title="Chuyển ngay tới số ghế này">🎯 Đi tới</button>
    </div>

    <div id="drawerHonorsStatus" style="font-size:11.5px; color:#536b88; text-align:center; margin-top:6px; font-weight:700;">
      Đang có 19 tân khoa trong danh sách trình chiếu.
    </div>
  </div>

  <hr style="border:none; border-top:1px dashed #d5e0ee; margin:16px 0;">

  <h2>🪑 Sơ Đồ Ghế Động Theo File Excel</h2>
  <p class="config-note">Số dãy và vị trí ghế trên sơ đồ được <strong>tự động sinh theo cột “Vị trí ghế”</strong>; số in trên ô ghế lấy từ cột <strong>“Số ghế”</strong>; màu ghế theo cột <strong>“Loại ghế”</strong> (để trống = tự động theo Trình độ + Khen thưởng).</p>
  <div id="layoutSummary" class="config-note" style="font-weight:800; color:#e2edfd;"></div>

  <!-- BỘ ĐIỀU KHIỂN CẤU HÌNH DÃY ĐẠI BIỂU, NCS & NGƯỜI THÂN -->
  <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(135,175,235,0.3); border-radius:10px; padding:12px; margin-bottom:14px;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
      <span style="font-size:12.5px; font-weight:800; color:#ffd778;">👑 Số dãy Đại biểu (VIP):</span>
      <div style="display:flex; align-items:center; gap:6px;">
        <button class="btn-sub" id="btnVipMinus" style="width:30px; height:28px; padding:0; font-weight:900; font-size:15px;" title="Giảm 1 dãy đại biểu">−</button>
        <span id="displayVipRows" style="font-size:14px; font-weight:800; color:#ffffff; min-width:56px; text-align:center; background:rgba(255,255,255,0.08); border:1px solid rgba(135,175,235,0.25); border-radius:6px; padding:3px 6px;">4 dãy</span>
        <button class="btn-sub" id="btnVipPlus" style="width:30px; height:28px; padding:0; font-weight:900; font-size:15px;" title="Tăng 1 dãy đại biểu">+</button>
      </div>
    </div>

    <div style="margin-bottom:10px;">
      <span style="display:block; font-size:12.5px; font-weight:800; color:#ffd778; margin-bottom:4px;">🎓 Vị trí dãy NCS / Tiến sĩ:</span>
      <div style="display:flex; gap:6px; margin-bottom:6px;">
        <input type="text" id="inputNcsSpec" value="4-R" placeholder="vd: 4-R, 4, 3, 4-R" style="flex:1; padding:6px 10px; font-size:13px; font-weight:700; background:rgba(3,12,28,0.9); border:1px solid rgba(135,175,235,0.4); border-radius:6px; color:#ffffff; text-transform:uppercase;">
        <button class="btn-sub" id="btnApplyNcsSpec" style="font-size:12px; padding:6px 12px; font-weight:800; color:#ffffff; background:#005ea3;">Áp dụng</button>
      </div>
      <div style="display:flex; gap:4px; flex-wrap:wrap;">
        <button class="btn-sub btn-ncs-quick" data-spec="4-R" style="font-size:11px; padding:3px 7px;">4-R</button>
        <button class="btn-sub btn-ncs-quick" data-spec="4-L" style="font-size:11px; padding:3px 7px;">4-L</button>
        <button class="btn-sub btn-ncs-quick" data-spec="4" style="font-size:11px; padding:3px 7px;">4 (Cả 2 bên)</button>
        <button class="btn-sub btn-ncs-quick" data-spec="3, 4-R" style="font-size:11px; padding:3px 7px;">3 + 4-R</button>
        <button class="btn-sub btn-ncs-quick" data-spec="3-R, 4-R" style="font-size:11px; padding:3px 7px;">3-R + 4-R</button>
      </div>
    </div>

    <div style="display:flex; justify-content:space-between; align-items:center;">
      <span style="font-size:12.5px; font-weight:800; color:#ffd778;">👨‍👩‍👧‍👦 Số dãy Người thân:</span>
      <div style="display:flex; align-items:center; gap:6px;">
        <button class="btn-sub" id="btnFamilyMinus" style="width:30px; height:28px; padding:0; font-weight:900; font-size:15px;" title="Giảm 1 dãy người thân">−</button>
        <span id="displayFamilyRows" style="font-size:14px; font-weight:800; color:#ffffff; min-width:56px; text-align:center; background:rgba(255,255,255,0.08); border:1px solid rgba(135,175,235,0.25); border-radius:6px; padding:3px 6px;">5 dãy</span>
        <button class="btn-sub" id="btnFamilyPlus" style="width:30px; height:28px; padding:0; font-weight:900; font-size:15px;" title="Tăng 1 dãy người thân">+</button>
      </div>
    </div>
  </div>

  <div class="stat-grid">
    <div class="stat-box gold">
      <strong id="statAwardsCount">0</strong>
      <span>Khen thưởng</span>
    </div>
    <div class="stat-box purple">
      <strong id="statMastersCount">0</strong>
      <span>Thạc sĩ</span>
    </div>
    <div class="stat-box orange">
      <strong id="statBachelorCount">0</strong>
      <span>Cử nhân</span>
    </div>
  </div>

  <div id="importIssues" style="margin-top:12px; padding:10px 12px; border-radius:8px; font-size:12px; line-height:1.5; max-height:190px; overflow:auto;"></div>

  <div class="btn-drawer-row" style="grid-template-columns:1fr;">
    <button class="btn-sub" id="btnResetHonorsData">↺ Khôi phục danh sách mặc định trong file</button>
  </div>
</aside>

<!-- FLOATING TOAST NOTIFICATION -->
<div id="toast"></div>

<!-- XLSX_INJECT_POINT -->

<!-- JAVASCRIPT LOGIC & MOTION SYSTEM -->
<script>
/**
 * TRƯỜNG ĐẠI HỌC KINH TẾ - ĐẠI HỌC ĐÀ NẴNG (DUE)
 * GRADUATION SEATING CEREMONY MASTER CONTROLLER
 */
(function() {{
  'use strict';

  const B64_EXCEL_TEMPLATE = "{b64_template_xlsx}";
  const SEATS_PER_ROW = 20;      // Mỗi dãy 20 ô: 10 ô khối trái + 10 ô khối phải
  const MAX_SEAT_ROWS = 20;      // Sức chứa tối đa: 20 dãy × 20 = 400 vị trí tân khoa, hội trường hỗ trợ tối đa 25 dãy

  const APP_STATE = {{
    effectsEnabled: true,
    highlightedPos: null,
    highlightTimer: null,
    // Cấu hình quy mô hội trường: Đại biểu (VIP), NCS/Tiến sĩ, Người thân
    config: {{
      vipRows: 4,          // Số dãy Đại biểu (1..6, mặc định 4: Dãy 1–4)
      ncsSpec: '4-R',      // Vị trí dãy NCS: '4-R', '4-L', '4', '3, 4-R', '3-R, 4-R'...
      familyRows: 5        // Số dãy Người thân (1..10, mặc định 5)
    }},
    // layout: sinh tự động từ Excel + config hình học
    layout: {{
      rows: 14,
      byPos: {{}},
      posByLabel: {{}},
      ncsSlots: new Set(['4-R']),
      geo: null
    }}
  }};
  window.APP_STATE = APP_STATE;

  // Phân tích mã vị trí NCS (hỗ trợ 1 dãy 1 bên, 1 dãy 2 bên, hoặc kết hợp nhiều dãy)
  // Ví dụ: '4-R', '4-L', '4', '3, 4-R', '3-R, 4-R', '3, 4'
  function parseNcsSlots(spec, vipRows) {{
    const s = String(spec || '').trim();
    const set = new Set();
    const V = Math.max(1, vipRows || 4);
    if (!s) {{
      set.add(`${{V}}-R`);
      return set;
    }}
    const tokens = s.split(/[,;+\\/\\s]+/);
    tokens.forEach(rawTok => {{
      const t = rawTok.trim().toUpperCase();
      if (!t) return;
      let m = t.match(/(\\d+)(?:-?([LR]))?/);
      if (!m) m = t.match(/([LR])-?(\\d+)/);
      if (m) {{
        const row = parseInt(m[1] && /^\\d+$/.test(m[1]) ? m[1] : m[2], 10);
        const side = (m[2] && /^[LR]$/.test(m[2])) ? m[2] : ((m[1] && /^[LR]$/.test(m[1])) ? m[1] : null);
        if (row >= 1) {{
          if (side === 'L' || side === 'R') {{
            set.add(`${{row}}-${{side}}`);
          }} else {{
            set.add(`${{row}}-L`);
            set.add(`${{row}}-R`);
          }}
        }}
      }}
    }});
    if (set.size === 0) set.add(`${{V}}-R`);
    return set;
  }}

  // Thuật toán hình học thống nhất hỗ trợ tối đa 25 dãy (khung Y=258..892 = 634px)
  // Tự động phân bổ đồng đều nhịp bước hàng (h, step) và 2 khoảng cách phân khu (Gap 1 = Gap 2 = G >= h/3)
  function computeGeometry(vipRows, seatRows, familyRows) {{
    const Y_START = 258;
    const Y_BOTTOM = 892;
    const H_TOTAL = Y_BOTTOM - Y_START; // 634px

    const V = Math.min(6, Math.max(1, vipRows || 4));
    const R = Math.min(MAX_SEAT_ROWS, Math.max(1, seatRows || 14));
    const F = Math.min(10, Math.max(1, familyRows || 5));
    const T = V + R + F;

    // Tổng số khe hở nội bộ giữa các hàng trong 3 phân khu: (V-1) + (R-1) + (F-1) = T - 3
    const N_intra = Math.max(0, V - 1) + Math.max(0, R - 1) + Math.max(0, F - 1);

    // Khe hở nội bộ giữa 2 hàng liên tiếp: 2.1px (khi T=25) .. 3.2px (khi T<=18)
    const g_intra = Math.max(2.0, Math.min(3.2, 3.2 - (T - 18) * 0.16));

    // Không gian còn lại dành cho tổng chiều cao các hàng (T * h) và 2 khoảng cách phân khu (2 * G)
    const H_rem = Math.max(100, H_TOTAL - N_intra * g_intra);

    // Tỷ lệ khoảng cách phân khu G = alpha * h
    // Khi đầy tải (T >= 25): alpha = 0.35 (> 1/3 = 0.3333, đảm bảo tối thiểu bằng 1/3 chiều cao dãy)
    // Khi số dãy ít hơn: tự động giãn rộng ra (lên tới 0.90 * h) để phân khu rõ nét
    const alpha = Math.max(0.35, Math.min(0.90, 0.35 + (25 - T) * 0.08));

    // Tính chiều cao hàng h: H_rem = (T + 2 * alpha) * h
    let h = H_rem / (T + 2 * alpha);
    let G = alpha * h;

    // Khống chế chiều cao hàng tối đa 27px để giữ tỷ lệ ô ghế thanh thoát
    if (h > 27.0) {{
      h = 27.0;
      G = Math.max(h / 3, (H_TOTAL - N_intra * g_intra - T * h) / 2);
    }}

    const step = h + g_intra;

    // 1. Phân khu Đại biểu (VIP: Dãy 1 .. V)
    const vipTop = Y_START;
    const vipRowH = h;
    const vipStep = step;
    const vipH = V * h + Math.max(0, V - 1) * g_intra;
    const vipBottom = vipTop + vipH;

    // Khoảng cách phân khu 1: Giữa hàng cuối Đại biểu và hàng 1 Tân khoa
    const gap1 = G;

    // 2. Phân khu Tân khoa (Graduates: Dãy V+1 .. V+R)
    const seatTop = vipBottom + gap1;
    const seatStep = step;
    const cellH = h;
    const seatH = R * h + Math.max(0, R - 1) * g_intra;
    const seatBottom = seatTop + seatH;

    // Khoảng cách phân khu 2: Giữa hàng cuối Tân khoa và hàng 1 Người thân (bằng đúng khoảng cách 1)
    const gap2 = G;

    // 3. Phân khu Người thân (Family: Dãy V+R+1 .. V+R+F)
    const familyStartY = seatBottom + gap2;
    const famH = F * h + Math.max(0, F - 1) * g_intra;
    const tierH = famH / F;

    const firstSeatRow = V + 1;
    const lastSeatRow = V + R;
    const firstFamilyRow = lastSeatRow + 1;
    const lastFamilyRow = lastSeatRow + F;
    const arrowY = seatTop + cellH / 2;

    return {{
      V, F, R, T,
      h, g_intra, step, gap: G,
      vip: {{ top: vipTop, step: vipStep, rowH: vipRowH, bottom: vipBottom, height: vipH }},
      seats: {{ top: seatTop, step: seatStep, cellH, bottom: seatBottom, height: seatH, firstRow: firstSeatRow, lastRow: lastSeatRow }},
      family: {{ startY: familyStartY, height: famH, tierH, firstRow: firstFamilyRow, lastRow: lastFamilyRow }},
      arrowY
    }};
  }}

  const SVGNS = "http://www.w3.org/2000/svg";
  const $ = id => document.getElementById(id);

  function createSvgEl(tag, attrs = {{}}, text = null) {{
    const el = document.createElementNS(SVGNS, tag);
    for (const [key, val] of Object.entries(attrs)) {{
      el.setAttribute(key, val);
    }}
    if (text !== null && text !== undefined) {{
      el.textContent = text;
    }}
    return el;
  }}

  let toastTimer = null;
  function showToast(msg) {{
    const toast = $('toast');
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 3500);
  }}

  // --- 1. BUILD SYMMETRIC ROW NUMBER COLUMNS ---
  function buildRowNumberColumns() {{
    const leftCol = $('rowNumbersLeft');
    const rightCol = $('rowNumbersRight');
    leftCol.replaceChildren();
    rightCol.replaceChildren();

    const geo = APP_STATE.layout.geo;
    if (!geo) return;

    const leftX = 454;
    const rightX = 1420;
    const boxW = 46, radius = 6;

    // Header Badge "Dãy"
    const createHeaderBadge = (x, y) => {{
      const g = createSvgEl('g', {{ transform: `translate(${{x}}, ${{y}})` }});
      g.append(createSvgEl('rect', {{
        x: 0, y: 0, width: boxW, height: 28, rx: radius,
        fill: '#005EA3', stroke: '#ffe082', 'stroke-width': '1.6'
      }}));
      g.append(createSvgEl('text', {{
        x: boxW / 2, y: 19, fill: '#ffffff', 'font-size': '15.5',
        'font-weight': '800', 'text-anchor': 'middle'
      }}, 'Dãy'));
      return g;
    }};

    leftCol.append(createHeaderBadge(leftX, 224));
    rightCol.append(createHeaderBadge(rightX, 224));

    // 1. VIP Rows 1..V (Căn giữa chính xác với các thanh Đại biểu)
    const badgeH = Math.min(24, Math.max(16, geo.h - 1.0));
    const fontSz = badgeH < 19 ? '12.5' : (badgeH < 22 ? '13.5' : '15');
    const yTxtOffset = badgeH / 2 + (badgeH < 20 ? 4.2 : 5);

    for (let r = 1; r <= geo.V; r++) {{
      const y = geo.vip.top + (r - 1) * geo.vip.step + (geo.vip.rowH - badgeH) / 2;
      [leftX, rightX].forEach((x, idx) => {{
        const g = createSvgEl('g', {{ transform: `translate(${{x}}, ${{y}})` }});
        g.append(createSvgEl('rect', {{
          x: 0, y: 0, width: boxW, height: badgeH, rx: 5,
          fill: '#ffffff', stroke: '#005EA3', 'stroke-width': '1.4'
        }}));
        g.append(createSvgEl('text', {{
          x: boxW / 2, y: yTxtOffset, fill: '#0a234f', 'font-size': fontSz,
          'font-weight': '800', 'text-anchor': 'middle'
        }}, String(r)));
        (idx === 0 ? leftCol : rightCol).append(g);
      }});
    }}

    // 2. Graduate Rows (V+1 .. V+R)
    for (let i = 0; i < geo.R; i++) {{
      const r = geo.seats.firstRow + i;
      const y = geo.seats.top + i * geo.seats.step + (geo.seats.cellH - badgeH) / 2;
      [leftX, rightX].forEach((x, idx) => {{
        const g = createSvgEl('g', {{ transform: `translate(${{x}}, ${{y}})` }});
        g.append(createSvgEl('rect', {{
          x: 0, y: 0, width: boxW, height: badgeH, rx: 5,
          fill: '#ffffff', stroke: '#005EA3', 'stroke-width': '1.3'
        }}));
        g.append(createSvgEl('text', {{
          x: boxW / 2, y: yTxtOffset, fill: '#0a234f', 'font-size': fontSz,
          'font-weight': '800', 'text-anchor': 'middle'
        }}, String(r)));
        (idx === 0 ? leftCol : rightCol).append(g);
      }});
    }}

    // 3. Family Rows (V+R+1 .. V+R+F)
    for (let i = 0; i < geo.F; i++) {{
      const r = geo.family.firstRow + i;
      const y = geo.family.startY + i * geo.step + (geo.h - badgeH) / 2;
      [leftX, rightX].forEach((x, idx) => {{
        const g = createSvgEl('g', {{ transform: `translate(${{x}}, ${{y}})` }});
        g.append(createSvgEl('rect', {{
          x: 0, y: 0, width: boxW, height: badgeH, rx: 5,
          fill: '#ffffff', stroke: '#005EA3', 'stroke-width': '1.3'
        }}));
        g.append(createSvgEl('text', {{
          x: boxW / 2, y: yTxtOffset, fill: '#0a234f', 'font-size': fontSz,
          'font-weight': '800', 'text-anchor': 'middle'
        }}, String(r)));
        (idx === 0 ? leftCol : rightCol).append(g);
      }});
    }}
  }}

  // --- 2. BUILD VIP BLOCKS (DÃY 1 – V, TỰ ĐỘNG THEO VỊ TRÍ NCS) ---
  function buildVipBlock() {{
    const container = $('vipBlock');
    container.replaceChildren();

    const geo = APP_STATE.layout.geo;
    if (!geo) return;

    const ncsSlots = APP_STATE.layout.ncsSlots || new Set();
    const blockWidth = 400;
    const leftBlockX = 520;
    const rightBlockX = 1000;
    const rowHeight = geo.vip.rowH;
    const startY = geo.vip.top;
    const step = geo.vip.step;
    const V = geo.V;

    for (let r = 1; r <= V; r++) {{
      const y = startY + (r - 1) * step;

      // Left Block
      const isLeftPhd = ncsSlots.has(`${{r}}-L`);
      const leftVip = createSvgEl('g', {{
        'class': isLeftPhd ? 'vip-row phd-row' : 'vip-row',
        'data-slot': `${{r}}-L`
      }});
      leftVip.append(createSvgEl('rect', {{
        x: leftBlockX, y: y, width: blockWidth, height: rowHeight, rx: 6,
        fill: isLeftPhd ? 'url(#phdRed)' : 'url(#vipGreen)',
        stroke: isLeftPhd ? '#6b030b' : '#024723', 'stroke-width': '1.4'
      }}));
      leftVip.append(createSvgEl('text', {{
        x: leftBlockX + blockWidth / 2, y: y + rowHeight / 2 + 5.5, fill: '#ffffff',
        'font-size': isLeftPhd ? (rowHeight < 24 ? '13.5' : '15.5') : (rowHeight < 24 ? '15.5' : '17.5'),
        'font-weight': '800', 'text-anchor': 'middle'
      }}, isLeftPhd ? 'NCS, GVHD và Gia đình NCS' : 'Đại biểu'));
      container.append(leftVip);

      // Right Block
      const isRightPhd = ncsSlots.has(`${{r}}-R`);
      const rightVip = createSvgEl('g', {{
        'class': isRightPhd ? 'vip-row phd-row' : 'vip-row',
        'data-slot': `${{r}}-R`
      }});
      rightVip.append(createSvgEl('rect', {{
        x: rightBlockX, y: y, width: blockWidth, height: rowHeight, rx: 6,
        fill: isRightPhd ? 'url(#phdRed)' : 'url(#vipGreen)',
        stroke: isRightPhd ? '#6b030b' : '#024723', 'stroke-width': '1.4'
      }}));
      rightVip.append(createSvgEl('text', {{
        x: rightBlockX + blockWidth / 2, y: y + rowHeight / 2 + 5.5, fill: '#ffffff',
        'font-size': isRightPhd ? (rowHeight < 24 ? '13.5' : '15.5') : (rowHeight < 24 ? '15.5' : '17.5'),
        'font-weight': '800', 'text-anchor': 'middle'
      }}, isRightPhd ? 'NCS, GVHD và Gia đình NCS' : 'Đại biểu'));
      container.append(rightVip);
    }}
  }}

  // --- 3. BUILD SEAT GRID FROM EXCEL DATA ---
  const SEAT_STYLE = {{
    awards:   {{ fill: 'url(#awardYellow)',    stroke: '#a87200', text: '#0e1f38', label: 'Khen thưởng' }},
    masters:  {{ fill: 'url(#masterPurple)',   stroke: '#3b0454', text: '#ffffff', label: 'Tân Thạc sĩ' }},
    bachelor: {{ fill: 'url(#bachelorOrange)', stroke: '#943202', text: '#140800', label: 'Tân Cử nhân' }},
    phd:      {{ fill: 'url(#phdRed)',         stroke: '#6b030b', text: '#ffffff', label: 'Tân Tiến sĩ' }}
  }};

  function getRecordCategory(rec) {{
    if (rec.seatType) return rec.seatType;
    if (rec.level === 'tiensi') return 'phd';
    if (rec.isAward) return 'awards';
    if (rec.level === 'thacsi') return 'masters';
    return 'bachelor';
  }}

  function drawSeatsGrid() {{
    const grid = $('seatBlock');
    grid.replaceChildren();

    const geo = APP_STATE.layout.geo;
    if (!geo) return;

    const rows = geo.R;
    const cellW = 38.4;
    const cellH = geo.seats.cellH;
    const gap = 1.8;
    const leftStartX = 520;
    const rightStartX = 1000;
    const baseFont = cellH < 22 ? 13.5 : 15;

    const counts = {{ awards: 0, masters: 0, bachelor: 0, phd: 0, empty: 0 }};

    for (let row = 0; row < rows; row++) {{
      const y = geo.seats.top + row * geo.seats.step;

      for (let k = 0; k < SEATS_PER_ROW; k++) {{
        const pos = row * SEATS_PER_ROW + k + 1;
        const isLeftBlock = k < 10;
        const colIdx = isLeftBlock ? k : (19 - k);
        const x = (isLeftBlock ? leftStartX : rightStartX) + colIdx * (cellW + gap);

        const rec = APP_STATE.layout.byPos[pos];
        if (!rec) {{
          // Ô trống mờ nét đứt
          counts.empty++;
          grid.append(createSvgEl('rect', {{
            'class': 'seat-empty',
            x: x, y: y, width: cellW, height: cellH, rx: 4.5,
            fill: 'rgba(120,140,170,0.10)', stroke: '#9fb0c8', 'stroke-width': '1',
            'stroke-dasharray': '3 3', opacity: '0.55', 'pointer-events': 'none'
          }}));
          continue;
        }}

        const category = getRecordCategory(rec);
        const style = SEAT_STYLE[category] || SEAT_STYLE.bachelor;
        counts[category] = (counts[category] || 0) + 1;

        const label = String(rec.seat);
        const isHighlighted = APP_STATE.highlightedPos === pos;
        const seatG = createSvgEl('g', {{
          'class': 'seat' + (isHighlighted ? ' highlight' : ''),
          'data-pos': pos,
          'data-number': label,
          'data-category': category
        }});

        seatG.append(createSvgEl('rect', {{
          x: x, y: y, width: cellW, height: cellH, rx: 4.5,
          fill: style.fill, stroke: style.stroke, 'stroke-width': '1.1'
        }}));

        const fontSize = label.length >= 4 ? 12 : (label.length === 3 ? Math.min(14, baseFont) : baseFont);
        seatG.append(createSvgEl('text', {{
          x: x + cellW / 2, y: y + cellH / 2 + 5.2,
          fill: style.text,
          'font-size': fontSize,
          'font-weight': '800',
          'text-anchor': 'middle'
        }}, label));

        const blockName = isLeftBlock ? 'Khối Trái' : 'Khối Phải';
        seatG.append(createSvgEl('title', {{}}, `Ghế ${{label}} • Dãy ${{geo.seats.firstRow + row}} (${{blockName}}) — ${{style.label}}`));

        grid.append(seatG);
      }}
    }}

    // Update Drawer summary
    $('statAwardsCount').textContent = counts.awards;
    $('statMastersCount').textContent = counts.masters;
    $('statBachelorCount').textContent = counts.bachelor;

    const filled = rows * SEATS_PER_ROW - counts.empty;
    $('layoutSummary').textContent =
      `Tổng ${{filled}} ghế tân khoa • ${{geo.V}} dãy Đại biểu (Dãy 1–${{geo.V}}) • ${{rows}} dãy Tân khoa (Dãy ${{geo.seats.firstRow}}–${{geo.seats.lastRow}}) • ${{geo.F}} dãy Người thân (Dãy ${{geo.family.firstRow}}–${{geo.family.lastRow}}) • Tổng ${{geo.T}} dãy (Khoảng cách phân khu: ${{Math.round(geo.gap)}}px)` +
      (counts.empty > 0 ? ` • ${{counts.empty}} ô trống` : '');
  }}

  // --- 4. BUILD FAMILY SECTION (KHỐI THẺ NGƯỜI THÂN LIỀN KHỐI THANH THOÁT) ---
  function buildFamilyBlock() {{
    const container = $('familyBlock');
    container.replaceChildren();

    const geo = APP_STATE.layout.geo;
    if (!geo) return;

    const blockWidth = 400;
    const leftBlockX = 520;
    const rightBlockX = 1000;
    const startY = geo.family.startY;
    const blockH = geo.family.height;
    const tierH = geo.family.tierH;
    const F = geo.F;

    [leftBlockX, rightBlockX].forEach(x => {{
      const g = createSvgEl('g', {{ 'class': 'family-card' }});
      // Khung thẻ xám xanh hoàng gia liền khối sạch sẽ (không dùng vạch nét đứt)
      g.append(createSvgEl('rect', {{
        x: x, y: startY, width: blockWidth, height: blockH, rx: 10,
        fill: 'url(#familyGray)', stroke: '#9ab3d6', 'stroke-width': '2'
      }}));

      // Nhãn dòng chữ trung tâm
      const fontSize = F >= 7 ? '17' : (F >= 6 ? '19' : '21');
      g.append(createSvgEl('text', {{
        x: x + blockWidth / 2, y: startY + blockH / 2 + 7,
        fill: '#0c2652', 'font-size': fontSize, 'font-weight': '800', 'text-anchor': 'middle',
        'pointer-events': 'none'
      }}, 'Người thân Tân TS/ThS/ĐH'));

      container.append(g);
    }});
  }}

  // Cập nhật vị trí Y của Mũi tên thoát ngang và Thảm đỏ danh dự theo hình học mới
  function updateDynamicExitArrowsAndCarpet() {{
    const geo = APP_STATE.layout.geo;
    if (!geo) return;

    const y = Math.round(geo.arrowY);
    const arR = $('arrowExitRight');
    const arL = $('arrowExitLeft');
    const stR = $('streamExitRight');
    const stL = $('streamExitLeft');
    if (arR) arR.setAttribute('d', `M 1466, ${{y}} L 1518, ${{y}}`);
    if (arL) arL.setAttribute('d', `M 454, ${{y}} L 402, ${{y}}`);
    if (stR) stR.setAttribute('d', `M 1466, ${{y}} L 1518, ${{y}}`);
    if (stL) stL.setAttribute('d', `M 454, ${{y}} L 402, ${{y}}`);

    // Đồng bộ chiều dài Thảm đỏ danh dự chạm khít mép đáy khối người thân
    const carpetBottom = Math.round(geo.family.startY + geo.family.height);
    const carpetH = carpetBottom - 256;
    const carpetRect = $('redCarpetRect');
    const trimL = $('redCarpetTrimLeft');
    const trimR = $('redCarpetTrimRight');
    if (carpetRect) carpetRect.setAttribute('height', String(carpetH));
    if (trimL) trimL.setAttribute('y2', String(carpetBottom));
    if (trimR) trimR.setAttribute('y2', String(carpetBottom));
  }}

  // --- 5. BUILD LEGEND ENTRIES (CHÚ GIẢI BẢNG GHI CHÚ COMPACT) ---
  function buildLegend() {{
    const g = $('legendEntries');
    g.replaceChildren();

    const entries = [
      {{ fill: 'url(#vipGreen)', stroke: '#024723', label: 'Ghế ngồi đại biểu' }},
      {{ fill: 'url(#phdRed)', stroke: '#6b030b', label: 'Ghế ngồi Tân Tiến sĩ' }},
      {{ fill: 'url(#awardYellow)', stroke: '#a87200', label: 'Ghế ngồi Cá nhân được\\ntuyên dương, khen thưởng' }},
      {{ fill: 'url(#masterPurple)', stroke: '#3b0454', label: 'Ghế ngồi Tân Thạc sĩ' }},
      {{ fill: 'url(#bachelorOrange)', stroke: '#943202', label: 'Ghế ngồi Tân Cử nhân' }},
      {{ fill: 'url(#familyGray)', stroke: '#9ab3d6', label: 'Ghế ngồi người thân\\nTân TS/ThS/ĐH' }}
    ];

    const startY = 88;
    const stepY = 70;

    entries.forEach((item, idx) => {{
      const y = startY + idx * stepY;
      const group = createSvgEl('g', {{ transform: `translate(16, ${{y}})` }});

      group.append(createSvgEl('rect', {{
        x: 0, y: 0, width: 48, height: 32, rx: 6,
        fill: item.fill, stroke: item.stroke, 'stroke-width': '1.6'
      }}));

      const lines = item.label.split('\\n');
      const textX = 62;
      if (lines.length === 1) {{
        group.append(createSvgEl('text', {{
          x: textX, y: 22, fill: '#0a1d3d', 'font-size': '15.5',
          'font-weight': '700'
        }}, lines[0]));
      }} else {{
        group.append(createSvgEl('text', {{
          x: textX, y: 14, fill: '#0a1d3d', 'font-size': '14.5',
          'font-weight': '700'
        }}, lines[0]));
        group.append(createSvgEl('text', {{
          x: textX, y: 32.5, fill: '#0a1d3d', 'font-size': '14.5',
          'font-weight': '700'
        }}, lines[1]));
      }}

      g.append(group);
    }});
  }}

  // --- 6. QUICK SEAT FINDER & PULSE HIGHLIGHT (tìm theo SỐ GHẾ hiển thị) ---
  function focusSeat(label) {{
    clearTimeout(APP_STATE.highlightTimer);
    document.querySelectorAll('.seat.highlight').forEach(el => el.classList.remove('highlight'));

    const key = (label === null || label === undefined) ? '' : String(label).trim();
    const pos = key ? APP_STATE.layout.posByLabel[key] : null;

    if (!pos) {{
      APP_STATE.highlightedPos = null;
      $('btnClearQuickSeat').classList.remove('show');
      return;
    }}

    APP_STATE.highlightedPos = pos;
    $('quickSeatInput').value = key;
    $('fsSeatInput').value = key;
    $('btnClearQuickSeat').classList.add('show');

    // Đồng bộ hiển thị bảng vinh danh người này nếu có trong danh sách
    if (typeof HONORS_STATE !== 'undefined' && HONORS_STATE.list && HONORS_STATE.list.length > 0) {{
      const foundIdx = HONORS_STATE.list.findIndex(item => item.pos === pos || String(item.seat || '').trim().toLowerCase() === key.toLowerCase());
      if (foundIdx !== -1 && foundIdx !== HONORS_STATE.currentIndex) {{
        updateHonorsDisplay(foundIdx);
      }}
    }}

    const target = document.querySelector(`.seat[data-pos="${{pos}}"]`);
    if (target) {{
      target.parentNode.append(target);
      target.classList.add('highlight');

      const rec = APP_STATE.layout.byPos[pos];
      const geo = APP_STATE.layout.geo;
      const firstSeatRow = geo ? geo.seats.firstRow : (APP_STATE.config.vipRows + 1);
      const row = Math.floor((pos - 1) / SEATS_PER_ROW) + firstSeatRow;
      const side = (pos - 1) % SEATS_PER_ROW < 10 ? 'Khối Trái' : 'Khối Phải';
      const catLabel = (SEAT_STYLE[getRecordCategory(rec)] || SEAT_STYLE.bachelor).label;

      showToast(`📍 Ghế số ${{key}}: Dãy ${{row}} • ${{side}} • Khu ${{catLabel}}`);

      APP_STATE.highlightTimer = setTimeout(() => {{
        target.classList.remove('highlight');
        APP_STATE.highlightedPos = null;
      }}, 7000);
    }}
  }}

  // --- 7. DATA -> LAYOUT PIPELINE (Excel quyết định số dãy, vị trí, số ghế, màu ghế) ---
  function computeLayout(list) {{
    const byPos = {{}};
    const posByLabel = {{}};
    let maxPos = 0;
    list.forEach(rec => {{
      if (!rec.pos) return;
      byPos[rec.pos] = rec;
      if (!(rec.seat in posByLabel)) posByLabel[rec.seat] = rec.pos;
      if (rec.pos > maxPos) maxPos = rec.pos;
    }});
    const rows = Math.min(MAX_SEAT_ROWS, Math.max(1, Math.ceil(maxPos / SEATS_PER_ROW)));
    const ncsSlots = parseNcsSlots(APP_STATE.config.ncsSpec, APP_STATE.config.vipRows);
    const geo = computeGeometry(APP_STATE.config.vipRows, rows, APP_STATE.config.familyRows);

    APP_STATE.layout = {{
      rows,
      byPos,
      posByLabel,
      ncsSlots,
      geo
    }};
  }}

  function renderIssues(issues) {{
    const box = $('importIssues');
    if (!box) return;
    box.replaceChildren();
    const ok = issues.length === 0;
    box.style.background = ok ? 'rgba(5,142,71,0.14)' : 'rgba(255,179,0,0.12)';
    box.style.border = ok ? '1px solid rgba(5,142,71,0.5)' : '1px solid rgba(255,179,0,0.5)';
    box.style.color = ok ? '#9be8bd' : '#ffe9a8';

    const title = document.createElement('div');
    title.style.fontWeight = '800';
    title.textContent = ok ? '✔ Dữ liệu hợp lệ — không có cảnh báo.' : `⚠ ${{issues.length}} cảnh báo khi đọc Excel:`;
    box.append(title);

    issues.slice(0, 8).forEach(t => {{
      const d = document.createElement('div');
      d.textContent = '• ' + t;
      box.append(d);
    }});
    if (issues.length > 8) {{
      const more = document.createElement('div');
      more.textContent = `… và ${{issues.length - 8}} cảnh báo khác.`;
      box.append(more);
    }}
  }}

  function applyHonorsData(list, issues, customConfig = null) {{
    HONORS_STATE.list = list;
    HONORS_STATE.currentIndex = 0;
    APP_STATE.highlightedPos = null;

    if (customConfig) {{
      if (customConfig.vipRows) APP_STATE.config.vipRows = Math.min(6, Math.max(1, customConfig.vipRows));
      if (customConfig.ncsSpec !== undefined && customConfig.ncsSpec !== null) APP_STATE.config.ncsSpec = customConfig.ncsSpec;
      if (customConfig.familyRows) APP_STATE.config.familyRows = Math.min(10, Math.max(1, customConfig.familyRows));
    }}

    computeLayout(list);
    buildVipBlock();
    buildRowNumberColumns();
    drawSeatsGrid();
    buildFamilyBlock();
    updateDynamicExitArrowsAndCarpet();
    updateDrawerConfigDisplay();
    renderIssues(issues || []);
  }}

  function updateDrawerConfigDisplay() {{
    const dispVip = $('displayVipRows');
    const dispFam = $('displayFamilyRows');
    const inpNcs = $('inputNcsSpec');
    if (dispVip) dispVip.textContent = `${{APP_STATE.config.vipRows}} dãy`;
    if (dispFam) dispFam.textContent = `${{APP_STATE.config.familyRows}} dãy`;
    if (inpNcs && document.activeElement !== inpNcs) inpNcs.value = APP_STATE.config.ncsSpec;
  }}

  function toggleEffects() {{
    APP_STATE.effectsEnabled = !APP_STATE.effectsEnabled;
    document.body.classList.toggle('effects-off', !APP_STATE.effectsEnabled);
    const label = '✦ Hiệu ứng: ' + (APP_STATE.effectsEnabled ? 'Bật' : 'Tắt');
    $('btnToggleFx').textContent = label;
    $('btnFsToggleFx').textContent = label;
    showToast(APP_STATE.effectsEnabled ? '✦ Đã bật luồng ánh sáng chuyển động' : '✦ Đã tắt hiệu ứng');
  }}

  async function toggleFullscreen() {{
    const target = $('stageWrapper');
    try {{
      if (!document.fullscreenElement) {{
        if (target.requestFullscreen) {{
          await target.requestFullscreen();
        }} else if (target.webkitRequestFullscreen) {{
          await target.webkitRequestFullscreen();
        }}
      }} else {{
        if (document.exitFullscreen) {{
          await document.exitFullscreen();
        }}
      }}
    }} catch (err) {{
      showToast('Chế độ trình chiếu: Hãy nhấn F11 trên bàn phím.');
    }}
  }}

  document.addEventListener('fullscreenchange', () => {{
    const isFull = !!document.fullscreenElement;
    $('btnFullscreen').textContent = isFull ? '✕ Thoát trình chiếu' : '⛶ Trình chiếu';
  }});

  // --- 8. ULTRA-HD PNG EXPORT (1920 × 1080) ---
  async function exportPng() {{
    showToast('⏳ Đang chuẩn bị tệp PNG 1920 × 1080...');
    try {{
      const svgClone = $('masterSvg').cloneNode(true);
      svgClone.setAttribute('width', '1920');
      svgClone.setAttribute('height', '1080');

      // Merge top honors overlay so exported PNG has the complete picture
      const topSvg = $('topHonorsSvg');
      if (topSvg) {{
        const topClone = topSvg.cloneNode(true);
        while (topClone.firstChild) {{
          svgClone.appendChild(topClone.firstChild);
        }}
      }}

      const xml = new XMLSerializer().serializeToString(svgClone);
      const svgBlob = new Blob([xml], {{ type: 'image/svg+xml;charset=utf-8' }});
      const url = URL.createObjectURL(svgBlob);

      const img = new Image();
      await new Promise((res, rej) => {{
        img.onload = res;
        img.onerror = rej;
        img.src = url;
      }});

      const exportCanvas = document.createElement('canvas');
      exportCanvas.width = 1920;
      exportCanvas.height = 1080;
      const eCtx = exportCanvas.getContext('2d');
      eCtx.drawImage(img, 0, 0, 1920, 1080);
      URL.revokeObjectURL(url);

      exportCanvas.toBlob(blob => {{
        if (blob) {{
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob);
          a.download = 'so-do-cho-ngoi-due-2026.png';
          a.click();
          setTimeout(() => URL.revokeObjectURL(a.href), 1500);
          showToast('✅ Đã xuất ảnh PNG 1920 × 1080 chuẩn sắc nét!');
        }}
      }}, 'image/png');
    }} catch (e) {{
      showToast('❌ Lỗi xuất ảnh: ' + e.message);
    }}
  }}

  // --- 9. EVENT LISTENERS & INITIALIZATION ---
  $('btnFullscreen').addEventListener('click', toggleFullscreen);
  $('btnFsExit').addEventListener('click', toggleFullscreen);
  $('btnToggleFx').addEventListener('click', toggleEffects);
  $('btnFsToggleFx').addEventListener('click', toggleEffects);
  $('btnExportPng').addEventListener('click', exportPng);

  $('btnToggleConfig').addEventListener('click', () => {{
    const isOpen = $('configDrawer').classList.toggle('open');
    $('btnToggleConfig').classList.toggle('active', isOpen);
  }});

  $('btnResetHonorsData').addEventListener('click', () => {{
    try {{ localStorage.removeItem(HONORS_STORAGE_KEY); }} catch (e) {{}}
    APP_STATE.config = {{ vipRows: 4, ncsSpec: '4-R', familyRows: 5 }};
    setHonorsSpeed(3);
    const res = parseHonorRows(DEFAULT_HONORS_ROWS);
    applyHonorsData(res.list, res.issues, res.config);
    updateHonorsDisplay(0);
    if (HONORS_STATE.isPlaying) scheduleNextHonors();
    showToast('↺ Đã khôi phục danh sách & cấu hình mặc định.');
  }});

  // Drawer Configuration Event Listeners
  const btnVipMinus = $('btnVipMinus');
  if (btnVipMinus) btnVipMinus.addEventListener('click', () => {{
    if (APP_STATE.config.vipRows > 1) {{
      APP_STATE.config.vipRows--;
      applyHonorsData(HONORS_STATE.list, []);
      showToast(`👑 Số dãy Đại biểu: ${{APP_STATE.config.vipRows}} dãy.`);
    }}
  }});

  const btnVipPlus = $('btnVipPlus');
  if (btnVipPlus) btnVipPlus.addEventListener('click', () => {{
    if (APP_STATE.config.vipRows < 6) {{
      APP_STATE.config.vipRows++;
      applyHonorsData(HONORS_STATE.list, []);
      showToast(`👑 Số dãy Đại biểu: ${{APP_STATE.config.vipRows}} dãy.`);
    }}
  }});

  const btnApplyNcs = $('btnApplyNcsSpec');
  const inputNcs = $('inputNcsSpec');
  if (btnApplyNcs && inputNcs) {{
    const doApplyNcs = () => {{
      const val = inputNcs.value.trim().toUpperCase() || '4-R';
      APP_STATE.config.ncsSpec = val;
      applyHonorsData(HONORS_STATE.list, []);
      showToast(`🎓 Vị trí dãy NCS: ${{val}}`);
    }};
    btnApplyNcs.addEventListener('click', doApplyNcs);
    inputNcs.addEventListener('keydown', (e) => {{ if (e.key === 'Enter') doApplyNcs(); }});
  }}

  document.querySelectorAll('.btn-ncs-quick').forEach(btn => {{
    btn.addEventListener('click', (e) => {{
      const spec = e.currentTarget.getAttribute('data-spec');
      if (spec) {{
        APP_STATE.config.ncsSpec = spec;
        if (inputNcs) inputNcs.value = spec;
        applyHonorsData(HONORS_STATE.list, []);
        showToast(`🎓 Vị trí dãy NCS: ${{spec}}`);
      }}
    }});
  }});

  const btnFamMinus = $('btnFamilyMinus');
  if (btnFamMinus) btnFamMinus.addEventListener('click', () => {{
    if (APP_STATE.config.familyRows > 1) {{
      APP_STATE.config.familyRows--;
      applyHonorsData(HONORS_STATE.list, []);
      showToast(`👨‍👩‍👧‍👦 Số dãy Người thân: ${{APP_STATE.config.familyRows}} dãy.`);
    }}
  }});

  const btnFamPlus = $('btnFamilyPlus');
  if (btnFamPlus) btnFamPlus.addEventListener('click', () => {{
    if (APP_STATE.config.familyRows < 10) {{
      APP_STATE.config.familyRows++;
      applyHonorsData(HONORS_STATE.list, []);
      showToast(`👨‍👩‍👧‍👦 Số dãy Người thân: ${{APP_STATE.config.familyRows}} dãy.`);
    }}
  }});

  [$('quickSeatInput'), $('fsSeatInput')].forEach(input => {{
    input.addEventListener('input', (e) => {{
      const val = e.target.value.trim();
      if (!val) focusSeat(null);
      else if (APP_STATE.layout.posByLabel[val]) focusSeat(val);
    }});
  }});

  $('btnClearQuickSeat').addEventListener('click', () => {{
    $('quickSeatInput').value = '';
    $('fsSeatInput').value = '';
    focusSeat(null);
  }});

  window.addEventListener('keydown', (e) => {{
    if (e.target.matches('input, textarea')) return;
    if (e.key.toLowerCase() === 'f') {{
      e.preventDefault();
      toggleFullscreen();
    }} else if (e.key.toLowerCase() === 'e') {{
      e.preventDefault();
      $('configDrawer').classList.toggle('open');
      $('btnToggleConfig').classList.toggle('active', $('configDrawer').classList.contains('open'));
    }}
  }});


  // --- REAL-TIME CODED FIREWORKS PARTICLE PHYSICS ENGINE (BẮN LÊN VÀ RỚT XUỐNG) ---
  let triggerHonorsFireworkBurst = function(isSpecial = false) {{}};

  (function initCanvasFireworks() {{
    const canvas = $('fireworksCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let particles = [];
    let rockets = [];
    let lastAutoSpawn = 0;

    // Palette of genuine golden pyrotechnic sparks
    const COLORS = [
      '#ffffff', '#fffdf0', '#fff3b0', '#ffe082', '#ffd54f',
      '#ffca28', '#ffb300', '#ffa000', '#ff8f00', '#ff6f00'
    ];

    // Falling ember particle (Rớt xuống với trọng lực và vệt sáng lấp lánh)
    class SparkParticle {{
      constructor(x, y, vx, vy, color, size, maxLife) {{
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
        this.color = color;
        this.size = size;
        this.alpha = 1;
        this.life = 0;
        this.maxLife = maxLife;
        this.gravity = 0.058; // Gravity pulling sparks downwards
        this.drag = 0.965;    // Air resistance
        this.history = [];
      }}
      update() {{
        this.history.push({{ x: this.x, y: this.y }});
        if (this.history.length > 5) this.history.shift();
        this.vx *= this.drag;
        this.vy = this.vy * this.drag + this.gravity;
        this.x += this.vx;
        this.y += this.vy;
        this.life++;
        this.alpha = Math.max(0, 1 - (this.life / this.maxLife));
      }}
      draw(c) {{
        if (this.alpha <= 0) return;
        c.save();
        c.globalAlpha = this.alpha;
        c.strokeStyle = this.color;
        c.fillStyle = this.color;

        // Sparkle trailing light
        if (this.history.length > 1) {{
          c.beginPath();
          c.moveTo(this.history[0].x, this.history[0].y);
          for (let i = 1; i < this.history.length; i++) {{
            c.lineTo(this.history[i].x, this.history[i].y);
          }}
          c.lineWidth = this.size * 0.75;
          c.stroke();
        }}

        // Glowing ember head
        c.beginPath();
        const r = (this.life % 4 < 2) ? this.size * 1.3 : this.size;
        c.arc(this.x, this.y, r, 0, Math.PI * 2);
        c.fill();
        c.restore();
      }}
    }}

    // Rocket streaking upwards (Bắn lên từ phía dưới)
    class FireworkRocket {{
      constructor(targetX, targetY, isSpecial = false) {{
        this.x = targetX + (Math.random() - 0.5) * 40;
        this.y = 230 + Math.random() * 20; // Starts from behind top arch of plaque (Y: 230-250), well above name at Y:356
        this.targetY = targetY;
        this.isSpecial = isSpecial;
        const dist = this.y - targetY;
        this.vy = -Math.sqrt(2 * 0.11 * dist); // Launch velocity
        this.vx = (targetX - this.x) / (Math.abs(this.vy) / 0.11);
        this.gravity = 0.11;
        this.trail = [];
        this.dead = false;
      }}
      update() {{
        this.trail.push({{ x: this.x, y: this.y }});
        if (this.trail.length > 7) this.trail.shift();
        this.vy += this.gravity;
        this.x += this.vx;
        this.y += this.vy;

        // Detonate at apex or when reaching target height
        if (this.vy >= -0.6 || this.y <= this.targetY) {{
          this.dead = true;
          this.explode();
        }}
      }}
      explode() {{
        const count = this.isSpecial ? 85 : 65;
        const power = this.isSpecial ? 5.8 : 4.8;
        for (let i = 0; i < count; i++) {{
          const angle = Math.random() * Math.PI * 2;
          const speed = (0.2 + Math.random() * 0.8) * power;
          const vx = Math.cos(angle) * speed;
          const vy = Math.sin(angle) * speed - 0.6; // Slight upward initial arc
          const color = COLORS[Math.floor(Math.random() * COLORS.length)];
          const size = 1.2 + Math.random() * 2.2;
          const maxLife = 40 + Math.floor(Math.random() * 35);
          particles.push(new SparkParticle(this.x, this.y, vx, vy, color, size, maxLife));
        }}
      }}
      draw(c) {{
        if (this.trail.length > 1) {{
          c.save();
          c.beginPath();
          c.moveTo(this.trail[0].x, this.trail[0].y);
          for (let i = 1; i < this.trail.length; i++) {{
            c.lineTo(this.trail[i].x, this.trail[i].y);
          }}
          c.strokeStyle = '#ffe599';
          c.lineWidth = 2.2;
          c.stroke();

          // Rocket head
          c.beginPath();
          c.arc(this.x, this.y, 2.8, 0, Math.PI * 2);
          c.fillStyle = '#ffffff';
          c.fill();
          c.restore();
        }}
      }}
    }}

    function launchPlaqueRocket(isSpecial = false) {{
      const targetX = 160 + Math.random() * 100; // X: 160 to 260
      const targetY = 120 + Math.random() * 55;  // Y: 120 to 175 (directly above plaque)
      rockets.push(new FireworkRocket(targetX, targetY, isSpecial));
    }}

    triggerHonorsFireworkBurst = function(isSpecial = false) {{
      if (document.body.classList.contains('effects-off')) return;
      const count = isSpecial ? 3 : 1;
      for (let i = 0; i < count; i++) {{
        setTimeout(() => {{
          launchPlaqueRocket(isSpecial);
        }}, i * 260);
      }}
    }};

    function animLoop(time) {{
      requestAnimationFrame(animLoop);
      if (document.body.classList.contains('effects-off')) {{
        ctx.clearRect(0, 0, 1920, 1080);
        return;
      }}
      ctx.clearRect(0, 0, 1920, 1080);
      ctx.globalCompositeOperation = 'lighter';

      // Auto periodic launch every 2.4 seconds right above plaque
      if (time - lastAutoSpawn > 2400) {{
        lastAutoSpawn = time;
        launchPlaqueRocket(false);
      }}

      // Update & draw rockets (Bắn lên)
      for (let i = rockets.length - 1; i >= 0; i--) {{
        const r = rockets[i];
        r.update();
        r.draw(ctx);
        if (r.dead) rockets.splice(i, 1);
      }}

      // Update & draw particles (Rớt xuống)
      for (let i = particles.length - 1; i >= 0; i--) {{
        const p = particles[i];
        p.update();
        p.draw(ctx);
        if (p.alpha <= 0) particles.splice(i, 1);
      }}
    }}

    // Initial celebratory launch at load
    launchPlaqueRocket(true);
    setTimeout(() => launchPlaqueRocket(false), 300);
    requestAnimationFrame(animLoop);
  }})();

    // --- 8. LIVE HONORS ROLL PRESENTATION & EXCEL ENGINE ---
  const PLAQUE_ASSETS = {{
    tiensi: '{b64_plaque_tiensi}',
    thacsi: '{b64_plaque_thacsi}',
    cunhan: '{b64_plaque_cunhan}'
  }};

  // Dữ liệu mặc định nhúng từ Excel (danhsach.xlsx hoặc file mẫu) — lưu dạng "dòng thô"
  // {{tiêu đề cột: giá trị}} để dùng CHUNG 1 bộ phân tích với nút "Nhập Excel".
  const DEFAULT_HONORS_ROWS = {default_honors_rows_json};
  const HONORS_STORAGE_KEY = 'due_graduation_honors_rows_v2';

  // Nhận diện cột theo tiêu đề (không phân biệt hoa/thường)
  function headerField(raw) {{
    const k = String(raw).trim().toLowerCase();
    if (k.includes('vị trí') || k.includes('vi tri') || k === 'stt' || k.includes('slot')) return 'pos';
    if (k.includes('loại ghế') || k.includes('loai ghe')) return 'seatType';
    if (k.includes('số ghế') || k.includes('so ghe') || k.includes('seat')) return 'seat';
    if (k.includes('họ') || k.includes('tên') || k.includes('name')) return 'name';
    if (k.includes('trình độ') || k.includes('trinh do') || k.includes('bậc') || k.includes('degree') || k.includes('level')) return 'level';
    if (k.includes('khen') || k.includes('thưởng') || k.includes('award')) return 'award';
    if (k.includes('ghi chú') || k.includes('ghi chu') || k.includes('note')) return 'note';
    return null;
  }}

  function normalizeSeatType(v) {{
    const s = String(v).trim().toLowerCase();
    if (!s) return null;
    if (s.includes('khen')) return 'awards';
    if (s.includes('thạc') || s.includes('thac')) return 'masters';
    if (s.includes('tiến') || s.includes('tien')) return 'phd';
    if (s.includes('cử nhân') || s.includes('cu nhan') || s.includes('đại học') || s.includes('dai hoc')) return 'bachelor';
    return null;
  }}

  // Phân tích các dòng Excel thành danh sách tân khoa + cấu hình hội trường + danh sách cảnh báo.
  // Tự động nhận diện 3 dòng cấu hình: "Số dãy Đại biểu", "Vị trí dãy NCS", "Số dãy Người thân".
  function parseHonorRows(rows) {{
    const issues = [];
    const list = [];
    const detectedConfig = {{}};
    if (!rows || rows.length === 0) return {{ list, issues, config: detectedConfig }};

    const keys = Object.keys(rows[0]);
    const hasPosCol = keys.some(h => headerField(h) === 'pos');
    const hasNameCol = keys.some(h => headerField(h) === 'name');
    const posSeen = {{}};
    const labelSeen = {{}};

    rows.forEach((row, idx) => {{
      const excelRow = idx + 2; // dòng 1 là tiêu đề
      const f = {{ pos: '', seat: '', name: '', level: '', seatType: '', award: '', note: '' }};
      const vals = [];
      for (const [key, val] of Object.entries(row)) {{
        const v = String(val === null || val === undefined ? '' : val).trim();
        if (v) vals.push(v);
        const field = headerField(key);
        if (field && v) f[field] = v;
      }}

      // Dự phòng file không có tiêu đề chuẩn: cột 1 = Số ghế, 2 = Họ tên, 3 = Trình độ, 4 = Khen thưởng
      if (!hasNameCol && vals.length >= 2) {{
        f.seat = f.seat || vals[0];
        f.name = vals[1];
        if (vals.length >= 3) f.level = f.level || vals[2];
        if (vals.length >= 4) f.award = f.award || vals[3];
      }}
      if (!f.name) return;

      // 1. Nhận diện các dòng Cấu hình Hội trường (Đại biểu, NCS, Người thân)
      const nameLower = f.name.toLowerCase();
      const levelLower = f.level.toLowerCase();
      const noteLower = f.note.toLowerCase();
      const fullText = `${{nameLower}} ${{levelLower}} ${{noteLower}}`;

      if (fullText.includes('số dãy đại biểu') || fullText.includes('so day dai bieu') || (fullText.includes('đại biểu') && !f.pos && /\\d+/.test(f.seat))) {{
        const m = (f.seat + ' ' + f.note).match(/\\d+/);
        if (m) detectedConfig.vipRows = parseInt(m[0], 10);
        return; // Không phải tân khoa, bỏ qua không đẩy vào danh sách vinh danh
      }}

      if (fullText.includes('vị trí dãy ncs') || fullText.includes('vi tri day ncs') || fullText.includes('vị trí ncs') || fullText.includes('dãy ncs')) {{
        const spec = (f.seat || f.note || '').trim();
        if (spec) detectedConfig.ncsSpec = spec;
        return;
      }}

      if (fullText.includes('số dãy người thân') || fullText.includes('so day nguoi than') || (fullText.includes('người thân') && !f.pos && /\\d+/.test(f.seat))) {{
        const m = (f.seat + ' ' + f.note).match(/\\d+/);
        if (m) detectedConfig.familyRows = parseInt(m[0], 10);
        return;
      }}

      const seatUpper = f.seat.toUpperCase();
      const lUpper = f.level.toUpperCase();
      let level = 'cunhan';
      if (seatUpper.startsWith('TS') || seatUpper.startsWith('NCS') || lUpper === 'TS' || lUpper.includes('TIẾN SĨ') || lUpper.includes('TIEN SI') || lUpper.includes('PHD')) {{
        level = 'tiensi';
      }} else if (lUpper.includes('THẠC SĨ') || lUpper.includes('THAC SI') || lUpper.includes('MASTER') || lUpper.includes('THS')) {{
        level = 'thacsi';
      }}

      const aUpper = f.award.toUpperCase();
      const seatType = normalizeSeatType(f.seatType);
      const isAward = ['X', 'CÓ', 'CO', '1', 'TRUE', 'YES', 'V', '✓', '✔'].includes(aUpper) ||
                      aUpper.includes('KHEN') || aUpper.includes('XUẤT SẮC') || seatType === 'awards';

      // Vị trí ghế (ô trên lưới). Không có cột "Vị trí ghế" -> coi Số ghế là vị trí (tương thích file cũ).
      let pos = null;
      if (level !== 'tiensi') {{
        const rawPos = hasPosCol ? f.pos : f.seat;
        if (/^\\d+$/.test(rawPos) && parseInt(rawPos, 10) >= 1) {{
          pos = parseInt(rawPos, 10);
        }} else {{
          issues.push(rawPos
            ? `Dòng ${{excelRow}} (${{f.name}}): Vị trí ghế "${{rawPos}}" không hợp lệ → không vẽ lên sơ đồ.`
            : `Dòng ${{excelRow}} (${{f.name}}): thiếu Vị trí ghế → không vẽ lên sơ đồ.`);
        }}
      }}

      if (pos !== null && pos > MAX_SEAT_ROWS * SEATS_PER_ROW) {{
        issues.push(`Dòng ${{excelRow}} (${{f.name}}): Vị trí ghế ${{pos}} vượt sức chứa tối đa ${{MAX_SEAT_ROWS * SEATS_PER_ROW}} → không vẽ lên sơ đồ.`);
        pos = null;
      }}
      if (pos !== null) {{
        if (posSeen[pos]) {{
          issues.push(`Vị trí ghế ${{pos}} bị trùng ở dòng ${{posSeen[pos]}} và ${{excelRow}} → dòng ${{excelRow}} không vẽ lên sơ đồ.`);
          pos = null;
        }} else {{
          posSeen[pos] = excelRow;
        }}
      }}

      const seat = f.seat || (pos ? String(pos) : '');
      if (level !== 'tiensi' && seat) {{
        if (labelSeen[seat]) {{
          issues.push(`Số ghế ${{seat}} bị trùng ở dòng ${{labelSeen[seat]}} và ${{excelRow}}.`);
        }} else {{
          labelSeen[seat] = excelRow;
        }}
      }}

      list.push({{ pos, seat, name: f.name, level, isAward, seatType, note: f.note }});
    }});

    const positions = Object.keys(posSeen).map(Number);
    if (positions.length) {{
      const maxPos = Math.max(...positions);
      const missing = [];
      for (let p = 1; p <= maxPos; p++) if (!posSeen[p]) missing.push(p);
      if (missing.length) {{
        issues.push(`Thiếu ${{missing.length}} vị trí ghế trong khoảng 1–${{maxPos}} (vẽ ô trống mờ): ${{missing.slice(0, 10).join(', ')}}${{missing.length > 10 ? '…' : ''}}`);
      }}
    }}
    return {{ list, issues, config: detectedConfig }};
  }}

  // Dấu vân tay của danh sách nhúng: bản build mới (danh sách mới) luôn thắng dữ liệu lưu cũ trong trình duyệt.
  function honorsFingerprint() {{
    const s = JSON.stringify(DEFAULT_HONORS_ROWS);
    let h = 5381;
    for (let i = 0; i < s.length; i++) h = ((h << 5) + h + s.charCodeAt(i)) | 0;
    return String(h);
  }}

  function loadInitialHonorsData() {{
    let rows = null;
    let savedConfig = null;
    try {{
      const saved = JSON.parse(localStorage.getItem(HONORS_STORAGE_KEY));
      if (saved && saved.fp === honorsFingerprint() && Array.isArray(saved.rows) && saved.rows.length > 0) {{
        rows = saved.rows;
        savedConfig = saved.config;
      }}
      localStorage.removeItem('due_graduation_honors_custom_list');
      localStorage.removeItem('due_graduation_seat_config_2026');
    }} catch (e) {{}}
    let res = parseHonorRows(rows || DEFAULT_HONORS_ROWS);
    if (res.list.length === 0) res = parseHonorRows(DEFAULT_HONORS_ROWS);
    const finalConfig = Object.assign({{}}, res.config || {{}}, savedConfig || {{}});
    applyHonorsData(res.list, res.issues, finalConfig);
  }}

  const HONORS_STATE = {{
    list: [],
    currentIndex: 0,
    isPlaying: true,
    timer: null,
    speedSeconds: 3
  }};
  window.HONORS_STATE = HONORS_STATE;
  window.updateHonorsDisplay = updateHonorsDisplay;
  window.applyHonorsData = applyHonorsData;

  function updateHonorsDisplay(index) {{
    if (!HONORS_STATE.list || HONORS_STATE.list.length === 0) return;

    if (index < 0) index = HONORS_STATE.list.length - 1;
    if (index >= HONORS_STATE.list.length) index = 0;
    HONORS_STATE.currentIndex = index;

    const current = HONORS_STATE.list[index];
    const seatStr = String(current.seat || '').trim();
    const seatUpper = seatStr.toUpperCase();
    const isPhd = (current.level === 'tiensi') || seatUpper === 'TS1' || seatUpper.startsWith('TS') || seatUpper.startsWith('NCS');
    const isAward = Boolean(current.isAward);

    // 1. UPDATE PLAQUE IMAGE BASED ON LEVEL
    const plaqueImg = $('honorsPlaqueImg');
    if (plaqueImg) {{
      let plaqueSrc = PLAQUE_ASSETS.cunhan;
      if (isPhd || current.level === 'tiensi') {{
        plaqueSrc = PLAQUE_ASSETS.tiensi;
      }} else if (current.level === 'thacsi') {{
        plaqueSrc = PLAQUE_ASSETS.thacsi;
      }} else {{
        plaqueSrc = PLAQUE_ASSETS.cunhan;
      }}
      plaqueImg.setAttribute('href', plaqueSrc);
    }}

    // 2. UPDATE HONOREE NAME IN OPEN CENTER OF PLAQUE
    const name1 = $('honorsPlaqueName1');
    const name2 = $('honorsPlaqueName2');
    const fullName = String(current.name || '').trim();

    // User requested: GIỮ NGUYÊN KÍCH CỠ CHỮ LỚN CHUẨN (20.5px), KHÔNG THU NHỎ
    const CONSTANT_FONT_SIZE = '20.5';

    if (fullName.length <= 27) {{
      // 1-Line Mode: Cố định chuẩn 20.5px không bị thu nhỏ
      if (name1) {{
        name1.textContent = fullName;
        name1.setAttribute('y', '342');
        name1.setAttribute('font-size', CONSTANT_FONT_SIZE);
      }}
      if (name2) {{
        name2.textContent = '';
      }}
    }} else {{
      // 2-Line Mode: Khi vượt quá 27 ký tự, ngắt 2 dòng và CẢ 2 DÒNG ĐỀU CÓ CÙNG CỠ CHỮ ĐỒNG NHẤT (19.5px)
      const parts = fullName.split(' ');
      const mid = Math.ceil(parts.length / 2);
      const line1 = parts.slice(0, mid).join(' ');
      const line2 = parts.slice(mid).join(' ');
      const twoLineSize = '19.5';

      if (name1) {{
        name1.textContent = line1;
        name1.setAttribute('y', '332');
        name1.setAttribute('font-size', twoLineSize);
      }}
      if (name2) {{
        name2.textContent = line2;
        name2.setAttribute('y', '356');
        name2.setAttribute('font-size', twoLineSize);
      }}
    }}

    // 3. UPDATE SEAT NUMBER & COLOR BADGE BELOW (màu theo Loại ghế trong Excel)
    const recCategory = getRecordCategory(current);
    const catStyle = SEAT_STYLE[recCategory] || SEAT_STYLE.bachelor;
    const seatBadgeBg = catStyle.fill;
    const seatTextColor = recCategory === 'awards' ? '#000000' : '#ffffff';

    const pillBg = $('honorsSeatPillBg');
    if (pillBg) pillBg.setAttribute('fill', seatBadgeBg);

    const pillText = $('honorsSeatPillText');
    if (pillText) {{
      pillText.textContent = isPhd ? seatStr : ('GHẾ ' + seatStr);
      pillText.setAttribute('fill', seatTextColor);
    }}

    // Seating Location Description
    const locText = $('honorsSeatLocation');
    const geo = APP_STATE.layout.geo;
    if (locText) {{
      if (isPhd) {{
        const slotsStr = [...(APP_STATE.layout.ncsSlots || [])].join(', ');
        locText.textContent = slotsStr ? `📍 Hàng NCS, GVHD & Gia đình (${{slotsStr}})` : '📍 Hàng NCS, GVHD & Gia đình';
      }} else {{
        if (current.pos) {{
          const firstSeatRow = geo ? geo.seats.firstRow : (APP_STATE.config.vipRows + 1);
          const row = Math.floor((current.pos - 1) / SEATS_PER_ROW) + firstSeatRow;
          const side = (current.pos - 1) % SEATS_PER_ROW < 10 ? 'Khối Trái' : 'Khối Phải';
          locText.textContent = `📍 Dãy ${{row}} • ${{side}}`;
        }} else {{
          locText.textContent = current.note ? `📍 ${{current.note}}` : '📍 Khu vực hội trường';
        }}
      }}
    }}

    // Award Badges Visibility (Both on Plaque & on Seat Card)
    const awardBadge = $('honorsAwardBadge');
    if (awardBadge) {{
      awardBadge.style.display = isAward ? 'block' : 'none';
      if (isAward) {{
        fitAwardBadgeText();
      }}
    }}
    const plaqueAward = $('plaqueAwardBadge');
    if (plaqueAward) {{
      plaqueAward.style.display = isAward ? 'block' : 'none';
    }}

    // Trigger Real Particle Fireworks Burst directly above the Honors Plaque
    if (typeof triggerHonorsFireworkBurst === 'function') {{
      triggerHonorsFireworkBurst(isAward || isPhd);
    }}

    // Highlight outer border of Seat Card if Award recipient
    const seatCardBg = $('honorsSeatCardBg');
    if (seatCardBg) {{
      seatCardBg.setAttribute('stroke', isAward ? '#ffb300' : 'url(#goldBorderGrad)');
      seatCardBg.setAttribute('stroke-width', isAward ? '3' : '2.2');
    }}

    // Update Drawer status
    const drawerStatus = $('drawerHonorsStatus');
    if (drawerStatus) {{
      drawerStatus.textContent = `Đang hiển thị tân khoa ${{index + 1}} / ${{HONORS_STATE.list.length}}: ${{fullName}} (${{seatStr}})`;
    }}

    // --- SPOTLIGHT SEAT ON SEATING DIAGRAM ---
    document.querySelectorAll('.seat.highlight').forEach(el => el.classList.remove('highlight'));
    document.querySelectorAll('.vip-row.phd-row').forEach(el => el.classList.remove('highlight'));

    if (isPhd) {{
      // Phát hào quang vàng kim vào TẤT CẢ các dãy/bên được chỉ định cho NCS
      document.querySelectorAll('.vip-row.phd-row').forEach(el => el.classList.add('highlight'));
    }} else {{
      if (current.pos) {{
        const target = document.querySelector(`.seat[data-pos="${{current.pos}}"]`);
        if (target) {{
          target.parentNode.append(target); // bring to top
          target.classList.add('highlight');
        }}
      }}
    }}
  }}

  // Tự động co chỉnh dòng chữ 'CÁ NHÂN ĐƯỢC KHEN THƯỞNG' trên ruy băng 3D để không bao giờ tràn/đè lên 2 ngôi sao trên mọi màn hình & font
  function fitAwardBadgeText() {{
    const textEl = $('honorsAwardBadgeText');
    const badge = $('honorsAwardBadge');
    if (!textEl || !badge) return;
    if (badge.style.display === 'none') return;
    textEl.removeAttribute('transform');
    const MAX_ALLOWED_WIDTH = 180; // Khoảng cách an toàn tối đa giữa 2 ngôi sao (cx=32 và cx=266)
    const CENTER_X = 149;
    const CENTER_Y = 21.5;
    try {{
      const bbox = textEl.getBBox();
      if (bbox && bbox.width > MAX_ALLOWED_WIDTH) {{
        const scale = (MAX_ALLOWED_WIDTH / bbox.width).toFixed(4);
        textEl.setAttribute('transform', `translate(${{CENTER_X}}, ${{CENTER_Y}}) scale(${{scale}}, 1) translate(${{-CENTER_X}}, ${{-CENTER_Y}})`);
      }}
    }} catch (e) {{}}
  }}

  function scheduleNextHonors() {{
    clearTimeout(HONORS_STATE.timer);
    if (!HONORS_STATE.isPlaying) return;
    HONORS_STATE.timer = setTimeout(() => {{
      updateHonorsDisplay(HONORS_STATE.currentIndex + 1);
      scheduleNextHonors();
    }}, HONORS_STATE.speedSeconds * 1000);
  }}

  function toggleHonorsPlay(forceState = null) {{
    if (forceState !== null) HONORS_STATE.isPlaying = forceState;
    else HONORS_STATE.isPlaying = !HONORS_STATE.isPlaying;

    const tbBtn = $('btnToolbarToggleHonors');
    const drawerPlay = $('btnDrawerPlayPause');

    if (HONORS_STATE.isPlaying) {{
      if (tbBtn) tbBtn.textContent = '⏯ Vinh danh: Đang chạy';
      if (drawerPlay) {{
        drawerPlay.textContent = '⏸ Tạm dừng';
        drawerPlay.style.background = '#005ea3';
      }}
      showToast('▶ Tiếp tục trình chiếu vinh danh tân khoa.');
      scheduleNextHonors();
    }} else {{
      clearTimeout(HONORS_STATE.timer);
      if (tbBtn) tbBtn.textContent = '⏯ Vinh danh: Tạm dừng';
      if (drawerPlay) {{
        drawerPlay.textContent = '▶ Tiếp tục';
        drawerPlay.style.background = '#058E47';
      }}
      showToast('⏸ Đã tạm dừng trình chiếu vinh danh.');
    }}
  }}

  function setHonorsSpeed(sec) {{
    HONORS_STATE.speedSeconds = sec;
    ['1s', '2s', '3s', '5s'].forEach(s => {{
      const btn = $('btnDrawerSpeed' + s);
      const isSel = (s === sec + 's');
      if (btn) {{
        btn.classList.toggle('active', isSel);
        btn.style.background = isSel ? '#005ea3' : '';
        btn.style.color = isSel ? '#ffffff' : '';
        btn.style.fontWeight = isSel ? '800' : 'normal';
      }}
    }});
    showToast(`⏱ Tốc độ chuyển người: ${{sec}} giây.`);
    if (HONORS_STATE.isPlaying) scheduleNextHonors();
  }}

  // Chuyển trực tiếp bảng vinh danh đến số ghế / vị trí / STT mong muốn
  function jumpToHonorsNumber(rawQuery) {{
    if (!rawQuery || !HONORS_STATE.list || HONORS_STATE.list.length === 0) return false;
    const q = String(rawQuery).trim();
    if (!q) return false;
    const qLower = q.toLowerCase();

    // 1. Tìm chính xác theo Số ghế hiển thị (seat: '1', '15', 'TS1', '280'...)
    let targetIdx = HONORS_STATE.list.findIndex(item => String(item.seat || '').trim().toLowerCase() === qLower);

    // 2. Nếu không thấy và query là số nguyên, thử tìm theo Vị trí ghế trên lưới (pos: 1, 15...)
    if (targetIdx === -1 && /^\\d+$/.test(q)) {{
      const num = parseInt(q, 10);
      targetIdx = HONORS_STATE.list.findIndex(item => item.pos === num);
    }}

    // 3. Nếu vẫn không thấy và query là số, thử tìm theo STT người học trong danh sách (1-based index)
    if (targetIdx === -1 && /^\\d+$/.test(q)) {{
      const num = parseInt(q, 10);
      if (num >= 1 && num <= HONORS_STATE.list.length) {{
        targetIdx = num - 1;
      }}
    }}

    // 4. Nếu vẫn chưa thấy, tìm mờ theo tên tân khoa (chứa tên)
    if (targetIdx === -1) {{
      targetIdx = HONORS_STATE.list.findIndex(item => String(item.name || '').toLowerCase().includes(qLower));
    }}

    if (targetIdx !== -1) {{
      updateHonorsDisplay(targetIdx);
      const honoree = HONORS_STATE.list[targetIdx];
      const isPhd = (honoree.level === 'tiensi') || String(honoree.seat || '').toUpperCase().startsWith('TS');
      const seatLabel = honoree.seat ? (isPhd ? honoree.seat : `Ghế ${{honoree.seat}}`) : '';
      showToast(`🎯 Đã chuyển đến: ${{honoree.name}} (${{seatLabel || `#${{targetIdx + 1}}`}})`);
      if (HONORS_STATE.isPlaying) scheduleNextHonors();
      return true;
    }} else {{
      showToast(`⚠ Không tìm thấy tân khoa có số ghế hoặc số thứ tự "${{q}}".`);
      return false;
    }}
  }}

  function downloadExcelTemplate() {{
    try {{
      // 1. Direct High-Speed Download from pre-packaged XLSX binary
      const byteCharacters = atob(B64_EXCEL_TEMPLATE);
      const byteNumbers = new Array(byteCharacters.length);
      for (let i = 0; i < byteCharacters.length; i++) {{
        byteNumbers[i] = byteCharacters.charCodeAt(i);
      }}
      const byteArray = new Uint8Array(byteNumbers);
      const blob = new Blob([byteArray], {{ type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(() => URL.revokeObjectURL(url), 2000);
      showToast('📄 Đã tải file Excel mẫu: Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx');
      return;
    }} catch(err) {{
      console.warn('Direct template download fallback to SheetJS:', err);
    }}

    if (typeof XLSX === 'undefined') {{
      showToast('❌ Thư viện Excel đang tải, vui lòng thử lại sau giây lát.');
      return;
    }}
    // Định dạng chuẩn: Vị trí ghế, Số ghế, Họ tên, Trình độ, Loại ghế, Khen thưởng, Ghi chú
    const headers = ['Vị trí ghế', 'Số ghế', 'Họ tên', 'Trình độ', 'Loại ghế', 'Khen thưởng', 'Ghi chú'];
    const sampleData = [
      headers,
      ['', 4, 'Số dãy Đại biểu', 'Đại biểu', '', '', 'Mặc định 4 dãy (Dãy 1-4, có thể nhập 2, 3, 5)'],
      ['', '4-R', 'Vị trí dãy NCS', 'Tiến sĩ', '', '', 'Ví dụ: 4-R, 4-L, 4, hoặc 3, 4-R (hỗ trợ nhiều dãy/bên)'],
      ['', 5, 'Số dãy Người thân', 'Người thân', '', '', 'Mặc định 5 dãy'],
      ['', 'TS1', 'TS. NGUYỄN VĂN AN', 'Tiến sĩ', '', 'x', 'Hàng NCS, GVHD và Gia đình NCS'],
      [1, 1, 'TRẦN MINH ĐỨC', 'Đại học', '', 'x', 'Thủ khoa Tốt nghiệp Cử nhân'],
      [2, 3, 'PHẠM QUANG HUY', 'Thạc sĩ', '', 'x', 'Vị trí 2 hiển thị số ghế 3'],
      [3, 4, 'HOÀNG THỊ THU HÀ', 'Thạc sĩ', '', '', ''],
      [4, 5, 'LÊ TRUNG KIÊN', 'Đại học', '', '', '']
    ];
    const ws = XLSX.utils.aoa_to_sheet(sampleData);
    ws['!cols'] = [{{ wch: 12 }}, {{ wch: 10 }}, {{ wch: 28 }}, {{ wch: 12 }}, {{ wch: 14 }}, {{ wch: 13 }}, {{ wch: 40 }}];
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'DanhSachTanKhoa');
    XLSX.writeFile(wb, 'Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx');
    showToast('📄 Đã tải file Excel mẫu: Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx');
  }}

  function handleExcelUpload(file) {{
    if (!file) return;
    if (typeof XLSX === 'undefined') {{
      showToast('❌ Thư viện Excel chưa sẵn sàng.');
      return;
    }}
    const reader = new FileReader();
    reader.onload = function(e) {{
      try {{
        const data = new Uint8Array(e.target.result);
        const workbook = XLSX.read(data, {{ type: 'array' }});
        const firstSheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[firstSheetName];
        const rows = XLSX.utils.sheet_to_json(worksheet, {{ defval: '' }});

        if (!rows || rows.length === 0) {{
          showToast('❌ File Excel không có dữ liệu.');
          return;
        }}

        const res = parseHonorRows(rows);
        if (res.list.length === 0) {{
          showToast('❌ Không tìm thấy cột Họ tên hợp lệ.');
          return;
        }}

        applyHonorsData(res.list, res.issues, res.config);
        try {{
          localStorage.setItem(HONORS_STORAGE_KEY, JSON.stringify({{
            fp: honorsFingerprint(),
            rows,
            config: APP_STATE.config
          }}));
        }} catch (e) {{}}
        updateHonorsDisplay(0);

        const placed = res.list.filter(r => r.pos).length;
        showToast(`✅ Đã nạp ${{res.list.length}} tân khoa (${{placed}} ghế trên sơ đồ)` +
                  (res.issues.length ? ` • ⚠ ${{res.issues.length}} cảnh báo (mở Cài đặt - phím E)` : ''));
        if (HONORS_STATE.isPlaying) scheduleNextHonors();
      }} catch (err) {{
        console.error(err);
        showToast('❌ Lỗi đọc file Excel: ' + (err.message || 'Kiểm tra định dạng file.'));
      }}
    }};
    reader.readAsArrayBuffer(file);
  }}

  function initHonorsSystem() {{
    // Toolbar Buttons
    const btnTbImport = $('btnToolbarImportExcel');
    if (btnTbImport) btnTbImport.addEventListener('click', () => $('honorsExcelInput').click());

    const btnTbDownload = $('btnToolbarDownloadTemplate');
    if (btnTbDownload) btnTbDownload.addEventListener('click', () => downloadExcelTemplate());

    const btnTbToggle = $('btnToolbarToggleHonors');
    if (btnTbToggle) btnTbToggle.addEventListener('click', () => toggleHonorsPlay());

    // Drawer Buttons
    const btnDrPlay = $('btnDrawerPlayPause');
    if (btnDrPlay) btnDrPlay.addEventListener('click', () => toggleHonorsPlay());

    const btnDrPrev = $('btnDrawerPrev');
    if (btnDrPrev) btnDrPrev.addEventListener('click', () => {{
      updateHonorsDisplay(HONORS_STATE.currentIndex - 1);
      if (HONORS_STATE.isPlaying) scheduleNextHonors();
    }});

    const btnDrNext = $('btnDrawerNext');
    if (btnDrNext) btnDrNext.addEventListener('click', () => {{
      updateHonorsDisplay(HONORS_STATE.currentIndex + 1);
      if (HONORS_STATE.isPlaying) scheduleNextHonors();
    }});

    const btnDrFirst = $('btnDrawerFirst');
    if (btnDrFirst) btnDrFirst.addEventListener('click', () => {{
      updateHonorsDisplay(0);
      if (HONORS_STATE.isPlaying) scheduleNextHonors();
    }});

    const btnDrS1 = $('btnDrawerSpeed1s');
    if (btnDrS1) btnDrS1.addEventListener('click', () => setHonorsSpeed(1));
    const btnDrS2 = $('btnDrawerSpeed2s');
    if (btnDrS2) btnDrS2.addEventListener('click', () => setHonorsSpeed(2));
    const btnDrS3 = $('btnDrawerSpeed3s');
    if (btnDrS3) btnDrS3.addEventListener('click', () => setHonorsSpeed(3));
    const btnDrS5 = $('btnDrawerSpeed5s');
    if (btnDrS5) btnDrS5.addEventListener('click', () => setHonorsSpeed(5));

    // Nhập số để chuyển trực tiếp đến đúng số ghế / tân khoa mong muốn
    const btnDrJump = $('btnDrawerJumpNumber');
    const inputDrJump = $('inputDrawerJumpNumber');
    const doJumpFromDrawer = () => {{
      if (!inputDrJump) return;
      const val = inputDrJump.value.trim();
      if (!val) {{
        showToast('ℹ Vui lòng nhập số ghế hoặc số thứ tự cần chuyển đến.');
        inputDrJump.focus();
        return;
      }}
      const success = jumpToHonorsNumber(val);
      if (success) inputDrJump.value = '';
    }};
    if (btnDrJump) btnDrJump.addEventListener('click', doJumpFromDrawer);
    if (inputDrJump) inputDrJump.addEventListener('keydown', (e) => {{
      if (e.key === 'Enter') {{
        e.preventDefault();
        doJumpFromDrawer();
      }}
    }});

    // File Input change
    const fileInput = $('honorsExcelInput');
    if (fileInput) fileInput.addEventListener('change', (e) => {{
      const file = e.target.files[0];
      if (file) handleExcelUpload(file);
      e.target.value = '';
    }});

    // Drag and Drop Excel files directly onto page
    window.addEventListener('dragover', (e) => {{
      e.preventDefault();
      e.stopPropagation();
    }});
    window.addEventListener('drop', (e) => {{
      e.preventDefault();
      e.stopPropagation();
      const files = e.dataTransfer && e.dataTransfer.files;
      if (files && files.length > 0) {{
        const file = files[0];
        const ext = file.name.split('.').pop().toLowerCase();
        if (['xlsx', 'xls', 'csv'].includes(ext)) {{
          handleExcelUpload(file);
        }} else {{
          showToast('❌ Vui lòng kéo thả file định dạng .xlsx, .xls hoặc .csv');
        }}
      }}
    }});

    // Keyboard Shortcuts for Wireless Remote Clicker & Operator Console
    window.addEventListener('keydown', (e) => {{
      if (e.target.matches('input, textarea')) return;
      if (e.code === 'Space') {{
        e.preventDefault();
        toggleHonorsPlay();
      }} else if (e.key === 'ArrowRight' || e.key === 'PageDown') {{
        e.preventDefault();
        updateHonorsDisplay(HONORS_STATE.currentIndex + 1);
        if (HONORS_STATE.isPlaying) scheduleNextHonors();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault();
        updateHonorsDisplay(HONORS_STATE.currentIndex - 1);
        if (HONORS_STATE.isPlaying) scheduleNextHonors();
      }} else if (e.key === 'Home') {{
        e.preventDefault();
        updateHonorsDisplay(0);
        if (HONORS_STATE.isPlaying) scheduleNextHonors();
      }} else if (e.key === 'End') {{
        e.preventDefault();
        updateHonorsDisplay(HONORS_STATE.list.length - 1);
        if (HONORS_STATE.isPlaying) scheduleNextHonors();
      }} else if (e.key === '1') {{
        setHonorsSpeed(1);
      }} else if (e.key === '2') {{
        setHonorsSpeed(2);
      }} else if (e.key === '3') {{
        setHonorsSpeed(3);
      }} else if (e.key === '4' || e.key === '5') {{
        setHonorsSpeed(5);
      }}
    }});

    // Hàm tìm vị trí tân khoa tương ứng khi click vào ô ghế
    function findHonoreeIndexBySeatEl(seatEl) {{
      if (!seatEl) return -1;
      const posAttr = seatEl.getAttribute('data-pos');
      const numAttr = (seatEl.getAttribute('data-number') || '').trim();
      const pos = posAttr ? parseInt(posAttr, 10) : null;

      // 1. Tìm theo pos trước nếu có
      if (pos !== null && !isNaN(pos)) {{
        const idx = HONORS_STATE.list.findIndex(item => item.pos === pos);
        if (idx !== -1) return idx;
      }}

      // 2. Tìm theo nhãn Số ghế (data-number)
      if (numAttr) {{
        const numLower = numAttr.toLowerCase();
        const idx = HONORS_STATE.list.findIndex(item => String(item.seat || '').trim().toLowerCase() === numLower);
        if (idx !== -1) return idx;
      }}

      // 3. Tìm theo APP_STATE.layout.byPos
      if (pos !== null && APP_STATE.layout && APP_STATE.layout.byPos && APP_STATE.layout.byPos[pos]) {{
        const rec = APP_STATE.layout.byPos[pos];
        const idx = HONORS_STATE.list.indexOf(rec);
        if (idx !== -1) return idx;
      }}

      return -1;
    }}

    // Xử lý sự kiện click vào ô ghế tân khoa (nhận diện trên cả seatBlock, vipBlock và document)
    const handleSeatClick = (e) => {{
      // 1. Click vào ô ghế tân khoa (.seat)
      const seatEl = e.target.closest('.seat');
      if (seatEl) {{
        const foundIdx = findHonoreeIndexBySeatEl(seatEl);
        if (foundIdx !== -1) {{
          updateHonorsDisplay(foundIdx);
          const honoree = HONORS_STATE.list[foundIdx];
          const isPhd = (honoree.level === 'tiensi') || String(honoree.seat || '').toUpperCase().startsWith('TS');
          const seatLabel = honoree.seat ? (isPhd ? honoree.seat : `Ghế ${{honoree.seat}}`) : '';
          showToast(`🎓 ${{honoree.name}} (${{seatLabel || `Vị trí ${{seatEl.getAttribute('data-pos')}}`}})`);
          if (HONORS_STATE.isPlaying) scheduleNextHonors();
        }} else {{
          focusSeat(seatEl.getAttribute('data-number') || seatEl.getAttribute('data-pos'));
        }}
        return;
      }}

      // 2. Click vào hàng ghế NCS (Dãy 4 phải hoặc dãy chỉ định cho NCS)
      const phdRowEl = e.target.closest('.vip-row.phd-row');
      if (phdRowEl) {{
        const phdIdx = HONORS_STATE.list.findIndex(item => item.level === 'tiensi' || String(item.seat || '').toUpperCase().startsWith('TS'));
        if (phdIdx !== -1) {{
          updateHonorsDisplay(phdIdx);
          const honoree = HONORS_STATE.list[phdIdx];
          showToast(`🎓 ${{honoree.name}} (${{honoree.seat || 'Tân Tiến sĩ'}})`);
          if (HONORS_STATE.isPlaying) scheduleNextHonors();
        }}
        return;
      }}
    }};

    $('seatBlock').addEventListener('click', handleSeatClick);
    const vipBlockEl = $('vipBlock');
    if (vipBlockEl) vipBlockEl.addEventListener('click', handleSeatClick);
    document.addEventListener('click', (e) => {{
      if (e.target.closest('.seat') || e.target.closest('.vip-row.phd-row')) {{
        handleSeatClick(e);
      }}
    }});

    // Nạp danh sách (ưu tiên bản người dùng vừa nhập trên máy này nếu cùng bản build) -> sinh dãy ghế + lưới ghế
    loadInitialHonorsData();

    // Start display & loop
    updateHonorsDisplay(0);
    scheduleNextHonors();

    // Tự động điều chỉnh dải ruy băng khi thay đổi kích thước cửa sổ hoặc font tải xong
    window.addEventListener('resize', fitAwardBadgeText);
    if (document.fonts && document.fonts.ready) {{
      document.fonts.ready.then(() => fitAwardBadgeText());
    }}
  }}

  // --- BOOTSTRAP ---
  buildVipBlock();
  buildFamilyBlock();
  buildLegend();
  initHonorsSystem();   // nạp dữ liệu Excel -> sinh dãy số dãy + lưới ghế

  window.dueGraduationApp = {{
    state: APP_STATE,
    honorsState: HONORS_STATE,
    updateHonors: updateHonorsDisplay,
    jumpTo: jumpToHonorsNumber,
    applyData: applyHonorsData,
    parseRows: parseHonorRows,
    focusSeat: focusSeat,
    exportPng: exportPng,
    toggleEffects: toggleEffects,
    fitAwardBadge: fitAwardBadgeText
  }};
}})();
</script>
</body>
</html>
"""

final_html = template.replace('<!-- XLSX_INJECT_POINT -->', f'<script>\n{js_xlsx}\n</script>')

# Keep the published page and the offline copy fully self-contained.
for font_name in ('Bold', 'XBold', 'Heavy', 'SemiBold', 'Medium', 'Regular'):
    font_path = Path('sources/brand-assets/fonts') / f'SVN-Gilroy {font_name}.otf'
    font_data = base64.b64encode(font_path.read_bytes()).decode('ascii')
    final_html = final_html.replace(str(font_path).replace('\\', '/'), f'data:font/otf;base64,{font_data}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print('SUCCESS: Generated index.html with Red Carpet, SVG WC/Entrance, balanced arrows, and visible layers.')
