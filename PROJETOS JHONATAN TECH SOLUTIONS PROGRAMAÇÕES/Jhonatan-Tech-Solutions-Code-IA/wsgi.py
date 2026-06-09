# WSGI entry point para Vercel
import os
import sys

# Adicionar backend ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Importar app do FastAPI
from app.main import app

# Para Vercel, export como app
__all__ = ['app']
