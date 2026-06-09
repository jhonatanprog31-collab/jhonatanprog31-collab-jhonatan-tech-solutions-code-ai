#!/bin/bash

# Script de verificacao - JHONATAN CODE AI

echo "=========================================="
echo "JHONATAN TECH SOLUTIONS CODE AI"
echo "Verificacao de Sistema"
echo "=========================================="
echo ""

# Cores
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Contador
passed=0
failed=0

# Funcoes
check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} $2"
        ((passed++))
    else
        echo -e "${RED}✗${NC} $2"
        ((failed++))
    fi
}

check_dir() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}✓${NC} $2"
        ((passed++))
    else
        echo -e "${RED}✗${NC} $2"
        ((failed++))
    fi
}

# Verificacoes de arquivos
echo "[1/5] Verificando Arquivos..."
check_file "README_GITHUB.md" "README_GITHUB.md"
check_file "docker-compose.yml" "docker-compose.yml"
check_file "LICENSE" "LICENSE"
check_file ".env.example" ".env.example"
check_file ".gitignore" ".gitignore"
check_file "setup.bat" "setup.bat"
echo ""

# Verificacoes de diretorios
echo "[2/5] Verificando Diretorios..."
check_dir "backend" "backend/"
check_dir "backend/app" "backend/app/"
check_dir "apps/web" "apps/web/"
check_dir "apps/mobile" "apps/mobile/"
check_dir "apps/desktop" "apps/desktop/"
check_dir ".github/workflows" ".github/workflows/"
echo ""

# Verificacoes de Python
echo "[3/5] Verificando Python..."
if command -v python3 &> /dev/null; then
    echo -e "${GREEN}✓${NC} Python 3 instalado"
    ((passed++))
else
    echo -e "${YELLOW}⚠${NC} Python 3 nao encontrado (opcional)"
fi

if [ -f "backend/requirements.txt" ]; then
    echo -e "${GREEN}✓${NC} requirements.txt encontrado"
    ((passed++))
fi
echo ""

# Verificacoes de Node
echo "[4/5] Verificando Node.js..."
if command -v node &> /dev/null; then
    echo -e "${GREEN}✓${NC} Node.js instalado"
    ((passed++))
else
    echo -e "${YELLOW}⚠${NC} Node.js nao encontrado (opcional)"
fi

if [ -f "apps/web/package.json" ]; then
    echo -e "${GREEN}✓${NC} apps/web/package.json encontrado"
    ((passed++))
fi
echo ""

# Verificacoes de Docker
echo "[5/5] Verificando Docker..."
if command -v docker &> /dev/null; then
    echo -e "${GREEN}✓${NC} Docker instalado"
    ((passed++))
else
    echo -e "${RED}✗${NC} Docker nao encontrado"
    ((failed++))
fi

if command -v docker-compose &> /dev/null; then
    echo -e "${GREEN}✓${NC} Docker Compose instalado"
    ((passed++))
else
    echo -e "${RED}✗${NC} Docker Compose nao encontrado"
    ((failed++))
fi
echo ""

# Resultado
echo "=========================================="
echo "RESULTADO:"
echo -e "${GREEN}Passou: $passed${NC}"
echo -e "${RED}Falhou: $failed${NC}"
echo "=========================================="
echo ""

if [ $failed -eq 0 ]; then
    echo -e "${GREEN}✓ Sistema pronto para uso!${NC}"
    echo ""
    echo "Proximos passos:"
    echo "1. cp .env.example .env"
    echo "2. docker-compose up -d"
    echo "3. Acesse http://localhost:3000"
    exit 0
else
    echo -e "${YELLOW}⚠ Alguns componentes faltam, mas o sistema pode funcionar.${NC}"
    exit 1
fi
