@echo off
setlocal enabledelayedexpansion
title CAP NHAT DANH SACH GOC - SO DO CHO NGOI DUE 2026

echo ======================================================================
echo   TRUONG DAI HOC KINH TE - DAI HOC DA NANG (DUE)
echo   CAP NHAT DANH SACH GOC VAO TEP index.html
echo ======================================================================
echo.

cd /d "%~dp0"

REM 1. Neu nguoi dung keo-tha tep Excel truc tiep vao file .bat
if not "%~1"=="" (
    echo [*] Nhan thay ban vua keo-tha tep: "%~nx1"
    copy /y "%~1" "danhsach.xlsx" > nul
    echo [*] Da sao chep thanh "danhsach.xlsx".
    echo.
)

REM 2. Kiem tra tep Excel dau vao
if not exist "danhsach.xlsx" (
    if not exist "Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx" (
        echo [!] LOI: KHONG TIM THAY TEP EXCEL DANH SACH!
        echo Vui long chep tep danh sach Excel vao thu muc nay voi ten "danhsach.xlsx",
        echo hoac keo-tha tep Excel cua ban tha truc tiep len tep Cap_Nhat_Danh_Sach.bat.
        echo.
        pause
        exit /b 1
    ) else (
        echo [*] Chua co tep "danhsach.xlsx", se dung: Mau_Danh_Sach_Vinh_Danh_Tot_Nghiep_2026.xlsx
    )
) else (
    echo [*] Tim thay tep danh sach moi: danhsach.xlsx
)

echo [*] Dang bien dich danh sach vao loi tep index.html...
python build_due_html.py

if errorlevel 1 (
    echo.
    echo [X] CO LOI XAY RA TRONG QUA TRINH BIEN DICH!
    echo Vui long kiem tra lai cau truc cot trong tep Excel hoac cai dat Python.
    echo.
    pause
    exit /b 1
)

echo.
echo ======================================================================
echo   [V] THANH CONG! DA CAP NHAT DANH SACH MOI LAM DANH SACH GOC!
echo   Tep "index.html" da duoc cap nhat vinh vien.
echo   Bay gio ban chi can copy duy nhat tep "index.html" mang di trinh chieu.
echo ======================================================================
echo.
