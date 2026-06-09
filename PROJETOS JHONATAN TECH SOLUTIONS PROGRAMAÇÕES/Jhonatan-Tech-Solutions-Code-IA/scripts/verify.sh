#!/bin/bash
# Verification Script for JHONATAN TECH SOLUTIONS CODE AI
# Run this to verify all components are properly set up

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║   JHONATAN TECH SOLUTIONS CODE AI - System Verification       ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
total=0
passed=0
failed=0

# Function to check
check() {
    total=$((total + 1))
    if [ $? -eq 0 ]; then
        passed=$((passed + 1))
        echo -e "${GREEN}✓${NC} $1"
    else
        failed=$((failed + 1))
        echo -e "${RED}✗${NC} $1"
    fi
}

echo "📋 Checking Prerequisites..."
echo "────────────────────────────────────────────────────────────────"

command -v docker >/dev/null 2>&1
check "Docker installed"

command -v docker-compose >/dev/null 2>&1
check "Docker Compose installed"

command -v python3 >/dev/null 2>&1
check "Python 3 installed"

command -v node >/dev/null 2>&1
check "Node.js installed"

echo ""
echo "📁 Checking Project Structure..."
echo "────────────────────────────────────────────────────────────────"

[ -d "backend" ]
check "Backend directory exists"

[ -d "apps/web" ]
check "Frontend directory exists"

[ -d "apps/desktop" ]
check "Desktop app directory exists"

[ -d "apps/mobile" ]
check "Mobile app directory exists"

[ -d ".github/workflows" ]
check "GitHub Actions workflows exist"

[ -d "scripts" ]
check "Scripts directory exists"

echo ""
echo "📄 Checking Key Files..."
echo "────────────────────────────────────────────────────────────────"

[ -f "backend/app/main.py" ]
check "Backend main.py exists"

[ -f "backend/Dockerfile" ]
check "Backend Dockerfile exists"

[ -f "backend/requirements.txt" ]
check "Backend requirements.txt exists"

[ -f "apps/web/package.json" ]
check "Frontend package.json exists"

[ -f "apps/web/Dockerfile" ]
check "Frontend Dockerfile exists"

[ -f "docker-compose.yml" ]
check "docker-compose.yml exists"

[ -f ".env.example" ]
check ".env.example exists"

[ -f "README.md" ]
check "README.md exists"

[ -f "SETUP_GUIDE.md" ]
check "SETUP_GUIDE.md exists"

echo ""
echo "🐳 Checking Docker Images..."
echo "────────────────────────────────────────────────────────────────"

docker images | grep -q "jhonatan-tech-solutions-code-ia-api"
check "Backend Docker image built"

docker images | grep -q "jhonatan-tech-solutions-code-ia-web"
check "Frontend Docker image built"

echo ""
echo "🔧 Checking Configuration..."
echo "────────────────────────────────────────────────────────────────"

[ -f "backend/app/core/config.py" ]
check "Backend config module exists"

[ -f "backend/app/core/database.py" ]
check "Backend database module exists"

[ -f "backend/app/core/security.py" ]
check "Backend security module exists"

[ -f "backend/app/routers/health.py" ]
check "Health router exists"

[ -f "backend/app/routers/code.py" ]
check "Code generation router exists"

echo ""
echo "📝 Checking Documentation..."
echo "────────────────────────────────────────────────────────────────"

grep -q "JHONATAN TECH SOLUTIONS CODE AI" README.md
check "README.md properly configured"

grep -q "Quick Start" SETUP_GUIDE.md
check "SETUP_GUIDE.md properly configured"

grep -q "CI/CD Pipeline" ".github/workflows/ci-cd.yml"
check "CI/CD workflow configured"

echo ""
echo "✅ Results Summary"
echo "════════════════════════════════════════════════════════════════"
echo -e "Total Checks:    $total"
echo -e "${GREEN}Passed:${NC}          $passed"
if [ $failed -gt 0 ]; then
    echo -e "${RED}Failed:${NC}          $failed"
else
    echo -e "${GREEN}Failed:${NC}          $failed"
fi
echo ""

if [ $failed -eq 0 ]; then
    echo -e "${GREEN}╔════════════════════════════════════════════════════════════════╗"
    echo "║          ✅ ALL CHECKS PASSED - SYSTEM READY! ✅               ║"
    echo "╚════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "🚀 Next Steps:"
    echo "1. Configure .env file (cp .env.example .env)"
    echo "2. Start the application (docker-compose up -d)"
    echo "3. Access the frontend (http://localhost:3000)"
    echo "4. Access API docs (http://localhost:8000/docs)"
    exit 0
else
    echo -e "${RED}╔════════════════════════════════════════════════════════════════╗"
    echo "║          ⚠️  SOME CHECKS FAILED - REVIEW ABOVE ⚠️              ║"
    echo "╚════════════════════════════════════════════════════════════════╝${NC}"
    exit 1
fi
