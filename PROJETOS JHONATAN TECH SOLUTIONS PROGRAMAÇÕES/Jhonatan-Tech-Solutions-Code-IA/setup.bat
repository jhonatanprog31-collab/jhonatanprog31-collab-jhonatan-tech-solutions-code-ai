@echo off
REM Setup completo para Windows
REM JHONATAN TECH SOLUTIONS CODE AI

color 0A
cls

echo ============================================================
echo  JHONATAN TECH SOLUTIONS CODE AI - SETUP COMPLETO
echo ============================================================
echo.

REM Verificar Python
echo [1/5] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo Instale em: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo [OK] Python encontrado
echo.

REM Verificar Docker
echo [2/5] Verificando Docker...
docker --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Docker nao encontrado!
    echo Instale em: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)
echo [OK] Docker encontrado
echo.

REM Verificar Node
echo [3/5] Verificando Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo [AVISO] Node.js nao encontrado. Nem sempre necessario.
) else (
    echo [OK] Node.js encontrado
)
echo.

REM Setup Backend
echo [4/5] Configurando Backend...
cd backend
if not exist venv (
    echo Criando virtual environment...
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
cd ..
echo [OK] Backend configurado
echo.

REM Setup Frontend
echo [5/5] Configurando Frontend...
cd apps\web
if not exist node_modules (
    echo Instalando dependencias npm...
    call npm install
) else (
    call npm update
)
cd ..\..
echo [OK] Frontend configurado
echo.

REM Criar .env se nao existir
if not exist .env (
    echo Criando arquivo .env...
    copy .env.example .env
    echo [OK] .env criado
) else (
    echo [OK] .env ja existe
)
echo.

echo ============================================================
echo SETUP COMPLETO COM SUCESSO!
echo ============================================================
echo.
echo Proximos passos:
echo.
echo 1. Inicie o Docker Compose:
echo    docker-compose up
echo.
echo 2. Acesse a aplicacao:
echo    Frontend:  http://localhost:3000
echo    API Docs:  http://localhost:8000/docs
echo.
echo ============================================================
echo.
pause
