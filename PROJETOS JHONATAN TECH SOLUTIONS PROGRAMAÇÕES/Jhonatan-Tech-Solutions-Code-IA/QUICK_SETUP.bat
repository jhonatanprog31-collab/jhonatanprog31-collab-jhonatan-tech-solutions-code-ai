@echo off
REM Setup Rápido para Windows

cls

echo.
echo ╔════════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                                ║
echo ║          🤖 JHONATAN TECH SOLUTIONS CODE AI - QUICK SETUP 🤖                  ║
echo ║                                                                                ║
echo ╚════════════════════════════════════════════════════════════════════════════════╝
echo.

REM Verificar Python
echo Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ✗ Python não encontrado!
    echo Instale em: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo ✓ Python encontrado

REM Verificar Docker
echo.
echo Verificando Docker...
docker --version >nul 2>&1
if errorlevel 1 (
    echo ✗ Docker não encontrado!
    echo Instale em: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)
echo ✓ Docker encontrado

REM Executar setup
echo.
echo Iniciando setup completo...
echo.

python JHONATAN_TECH_SOLUTIONS_CODE_AI_SETUP.py setup

pause
