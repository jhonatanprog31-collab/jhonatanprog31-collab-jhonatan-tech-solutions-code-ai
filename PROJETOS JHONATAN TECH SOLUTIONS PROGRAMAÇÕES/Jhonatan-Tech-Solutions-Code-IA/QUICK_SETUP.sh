#!/bin/bash
# Setup Rápido para Mac/Linux

clear

echo "╔════════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                                ║"
echo "║          🤖 JHONATAN TECH SOLUTIONS CODE AI - QUICK SETUP 🤖                  ║"
echo "║                                                                                ║"
echo "╚════════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Verificar Python
echo "Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "✗ Python não encontrado!"
    echo "Instale em: https://www.python.org/downloads/"
    exit 1
fi
echo "✓ Python encontrado"

# Verificar Docker
echo ""
echo "Verificando Docker..."
if ! command -v docker &> /dev/null; then
    echo "✗ Docker não encontrado!"
    echo "Instale em: https://www.docker.com/products/docker-desktop"
    exit 1
fi
echo "✓ Docker encontrado"

# Executar setup
echo ""
echo "Iniciando setup completo..."
echo ""

python3 JHONATAN_TECH_SOLUTIONS_CODE_AI_SETUP.py setup
