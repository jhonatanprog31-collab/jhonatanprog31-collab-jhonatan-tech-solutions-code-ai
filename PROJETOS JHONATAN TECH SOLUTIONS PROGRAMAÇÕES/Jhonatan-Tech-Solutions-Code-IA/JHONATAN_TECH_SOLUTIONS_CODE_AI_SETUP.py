# -*- coding: utf-8 -*-
"""
JHONATAN TECH SOLUTIONS CODE AI - SETUP COMPLETO
Sistema IA Especializado em Engenharia de Software
Versao: 1.0.0 | Status: Production Ready

USO:
    python JHONATAN_TECH_SOLUTIONS_CODE_AI_SETUP.py [comando]

COMANDOS:
    setup       - Setup completo do projeto
    start       - Inicia o projeto
"""

import os
import sys
import json
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple
import platform

# ==================== CORES PARA TERMINAL ====================
class Colors:
    """Codigos ANSI para cores no terminal"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ==================== CLASSE PRINCIPAL ====================
class JhonatanTechSolutionsSetup:
    """Gerenciador de setup do projeto JHONATAN TECH SOLUTIONS CODE AI"""
    
    def __init__(self):
        self.base_path = Path(os.getcwd())
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.os_type = platform.system()
        
    def print_banner(self):
        """Exibe banner do projeto"""
        banner = f"""{Colors.CYAN}
========================================
JHONATAN TECH SOLUTIONS CODE AI
Versao: 1.0.0
Timestamp: {self.timestamp}
Sistema: {self.os_type}
========================================
{Colors.ENDC}"""
        print(banner)
    
    def print_section(self, title: str):
        """Exibe titulo de secao"""
        print(f"\n{Colors.BLUE}{Colors.BOLD}{'='*60}{Colors.ENDC}")
        print(f"{Colors.BLUE}{Colors.BOLD}>>> {title}{Colors.ENDC}")
        print(f"{Colors.BLUE}{Colors.BOLD}{'='*60}{Colors.ENDC}\n")
    
    def print_success(self, message: str):
        """Exibe mensagem de sucesso"""
        print(f"{Colors.GREEN}[OK] {message}{Colors.ENDC}")
    
    def print_error(self, message: str):
        """Exibe mensagem de erro"""
        print(f"{Colors.RED}[ERRO] {message}{Colors.ENDC}")
    
    def print_info(self, message: str):
        """Exibe mensagem de informacao"""
        print(f"{Colors.CYAN}[INFO] {message}{Colors.ENDC}")
    
    def create_structure(self):
        """Cria estrutura de pastas do projeto"""
        self.print_section("Criando Estrutura de Pastas")
        
        try:
            # Diretorios principais
            dirs = [
                "backend/app/routers",
                "backend/app/models",
                "backend/app/core",
                "backend/app/utils",
                "backend/app/schemas",
                "backend/tests",
                "apps/web/components",
                "scripts",
                "docs",
                "logs",
                "reports",
            ]
            
            for dir_path in dirs:
                dir_full = self.base_path / dir_path
                dir_full.mkdir(parents=True, exist_ok=True)
                self.print_success(f"Pasta criada: {dir_path}")
            
            # Criar __init__.py
            init_dirs = [
                "backend/app",
                "backend/app/routers",
                "backend/app/models",
                "backend/app/core",
                "backend/app/utils",
                "backend/app/schemas",
                "backend/tests",
            ]
            
            for dir_path in init_dirs:
                init_file = self.base_path / dir_path / "__init__.py"
                init_file.touch()
                self.print_success(f"__init__.py criado em: {dir_path}")
            
        except Exception as e:
            self.print_error(f"Erro ao criar estrutura: {str(e)}")
            return False
        
        return True
    
    def show_next_steps(self):
        """Exibe proximos passos"""
        self.print_section("Proximos Passos")
        
        next_steps = f"""{Colors.GREEN}

Setup Completo com Sucesso!
Bem-vindo ao JHONATAN TECH SOLUTIONS CODE AI!

{Colors.CYAN}

1. Para Comcar:
   - docker-compose up

2. Acessar Aplicacao:
   - Frontend: http://localhost:3000
   - API: http://localhost:8000/docs

3. Documentacao:
   - Leia: README.md
   - Explore: docs/

{Colors.ENDC}"""
        
        print(next_steps)
    
    def run_setup(self):
        """Executa setup completo"""
        self.print_banner()
        if self.create_structure():
            self.show_next_steps()
        else:
            self.print_error("Setup falhou!")
    
    def run_start(self):
        """Inicia o projeto"""
        self.print_banner()
        self.print_section("Iniciando Projeto")
        self.print_info("Iniciando Docker Compose...")
        
        try:
            subprocess.run(["docker-compose", "up"], cwd=str(self.base_path))
        except Exception as e:
            self.print_error(f"Erro: {str(e)}")

# ==================== PONTO DE ENTRADA ====================
def main():
    """Funcao principal"""
    setup = JhonatanTechSolutionsSetup()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "setup":
            setup.run_setup()
        elif command == "start":
            setup.run_start()
        else:
            print(f"Comando desconhecido: {command}")
    else:
        setup.run_setup()

if __name__ == "__main__":
    main()
