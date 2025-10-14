@echo off
REM ==========================================
REM  🔄 Auto Update Flask Project ke GitHub
REM ==========================================

set PROJECT_DIR=%~dp0
cd /d "%PROJECT_DIR%"

echo ===============================
echo 🔧 Mengaktifkan virtual environment...
echo ===============================
call .venv\Scripts\activate

echo ===============================
echo 📦 Menginstal dependensi...
echo ===============================
pip install --upgrade pip
pip install -r requirements.txt

echo ===============================
echo 📝 Masukkan pesan commit:
echo ===============================
set /p commitMsg="Pesan commit: "

echo ===============================
echo 🚀 Menjalankan git push...
echo ===============================
git add .
git commit -m "%commitMsg%"
git push origin main

echo.
echo ✅ Berhasil di-push ke GitHub dan Vercel akan auto-deploy!
echo Tekan sembarang tombol untuk keluar.
pause >nul