@echo off
REM JHONATAN TECH SOLUTIONS CODE AI - Windows Setup Script

setlocal enabledelayedexpansion

echo.
echo 🚀 JHONATAN TECH SOLUTIONS CODE AI - Windows Setup
echo ====================================================
echo.

REM Check requirements
echo 📋 Checking requirements...

where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ✗ Python not found. Please install Python 3.10+
    pause
    exit /b 1
)
echo ✓ Python found

where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ✗ Node.js not found. Please install Node.js 18+
    pause
    exit /b 1
)
echo ✓ Node.js found

where docker >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ✗ Docker not found. Please install Docker Desktop
    pause
    exit /b 1
)
echo ✓ Docker found

REM Create environment file
if not exist .env (
    echo.
    echo 📝 Creating .env file from .env.example...
    copy .env.example .env
    echo ✓ .env created (update with your values)
)

REM Backend setup
echo.
echo 🔧 Setting up backend...
cd backend

if not exist venv (
    echo Creating Python virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat
echo Installing Python dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
call venv\Scripts\deactivate.bat

cd ..

REM Frontend setup
echo.
echo 🔧 Setting up frontend...
cd apps\web

if not exist node_modules (
    echo Installing Node dependencies...
    call npm install
)

cd ..\..

REM Create necessary directories
echo.
echo 📁 Creating necessary directories...
if not exist logs mkdir logs
if not exist reports mkdir reports

REM Build Docker images
echo.
echo 🐳 Building Docker images...
docker-compose build

echo.
echo ✅ Setup complete!
echo.
echo To start the application, run:
echo   docker-compose up
echo.
echo Then access:
echo   Frontend: http://localhost:3000
echo   API: http://localhost:8000/docs
echo.
pause
