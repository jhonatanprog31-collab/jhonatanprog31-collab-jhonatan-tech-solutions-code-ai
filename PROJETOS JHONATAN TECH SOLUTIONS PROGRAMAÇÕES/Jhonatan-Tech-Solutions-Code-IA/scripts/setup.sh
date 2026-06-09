#!/bin/bash

# JHONATAN TECH SOLUTIONS CODE AI - Complete Setup Script
# This script initializes the entire development environment

set -e

echo "🚀 JHONATAN TECH SOLUTIONS CODE AI - Setup"
echo "==========================================="

# Check requirements
echo "📋 Checking requirements..."

check_command() {
    if command -v $1 &> /dev/null; then
        echo "✓ $1 found"
    else
        echo "✗ $1 not found. Please install it."
        exit 1
    fi
}

check_command "python3"
check_command "node"
check_command "npm"
check_command "docker"

# Create environment file
if [ ! -f .env ]; then
    echo "📝 Creating .env file from .env.example..."
    cp .env.example .env
    echo "✓ .env created (update with your values)"
fi

# Backend setup
echo ""
echo "🔧 Setting up backend..."
cd backend

if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
deactivate

cd ..

# Frontend setup
echo ""
echo "🔧 Setting up frontend..."
cd apps/web

if [ ! -d "node_modules" ]; then
    echo "Installing Node dependencies..."
    npm install
fi

cd ../../

# Create necessary directories
echo ""
echo "📁 Creating necessary directories..."
mkdir -p logs reports

# Build Docker images
echo ""
echo "🐳 Building Docker images..."
docker-compose build

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the application, run:"
echo "  docker-compose up"
echo ""
echo "Then access:"
echo "  Frontend: http://localhost:3000"
echo "  API: http://localhost:8000/docs"
