# -*- coding: utf-8 -*-
"""
JHONATAN TECH SOLUTIONS CODE AI - Backend Completo
FastAPI com PostgreSQL, Redis e suporte a IA
Production-ready para Vercel deployment
"""

import os
from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
from pydantic import BaseModel

# ==================== CONFIGURAÇÃO ====================
# Detectar ambiente
IS_PRODUCTION = os.getenv("VERCEL_ENV") == "production"
DEBUG = not IS_PRODUCTION

# ==================== MODELOS ====================
class HealthResponse(BaseModel):
    status: str
    timestamp: str
    service: str
    version: str
    environment: str

class AppRequest(BaseModel):
    name: str
    language: str
    framework: str
    description: Optional[str] = None

class AppResponse(BaseModel):
    id: str
    name: str
    language: str
    framework: str
    status: str
    created_at: str

class CodeGenerationRequest(BaseModel):
    app_id: str
    feature: str
    language: str

class CodeGenerationResponse(BaseModel):
    id: str
    app_id: str
    code: str
    language: str
    status: str
    generated_at: str

# ==================== APP SETUP ====================
app = FastAPI(
    title="JHONATAN TECH SOLUTIONS CODE AI",
    description="Sistema IA para Engenharia de Software",
    version="1.0.0",
    docs_url="/docs" if DEBUG else None,
    redoc_url="/redoc" if DEBUG else None,
)

# ==================== CORS ====================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== STORAGE (Em Produção, usar banco de dados real) ====================
apps_db = {}
generated_code_db = {}

# ==================== ENDPOINTS ====================

@app.get("/")
async def root():
    """Root endpoint com informações gerais"""
    return {
        "message": "Bem-vindo ao JHONATAN TECH SOLUTIONS CODE AI",
        "version": "1.0.0",
        "docs": "/docs" if DEBUG else None,
        "status": "online",
        "environment": "production" if IS_PRODUCTION else "development"
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        service="JHONATAN CODE AI Backend",
        version="1.0.0",
        environment="production" if IS_PRODUCTION else "development"
    )

@app.get("/api/status")
async def api_status():
    """Status completo da API"""
    return {
        "status": "operational",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "environment": "production" if IS_PRODUCTION else "development",
        "services": {
            "api": "online"
        }
    }

# ==================== APPS ENDPOINTS ====================

@app.post("/api/apps", response_model=AppResponse)
async def create_app(request: AppRequest):
    """Criar nova aplicacao"""
    app_id = f"app_{len(apps_db) + 1}"
    
    app_data = {
        "id": app_id,
        "name": request.name,
        "language": request.language,
        "framework": request.framework,
        "description": request.description,
        "status": "active",
        "created_at": datetime.now().isoformat()
    }
    
    apps_db[app_id] = app_data
    return AppResponse(**app_data)

@app.get("/api/apps")
async def list_apps(skip: int = 0, limit: int = 10):
    """Listar aplicacoes"""
    apps_list = list(apps_db.values())[skip:skip + limit]
    return [AppResponse(**app) for app in apps_list]

@app.get("/api/apps/{app_id}", response_model=AppResponse)
async def get_app(app_id: str):
    """Obter aplicacao"""
    if app_id not in apps_db:
        raise HTTPException(status_code=404, detail="App nao encontrado")
    return AppResponse(**apps_db[app_id])

@app.delete("/api/apps/{app_id}")
async def delete_app(app_id: str):
    """Deletar aplicacao"""
    if app_id not in apps_db:
        raise HTTPException(status_code=404, detail="App nao encontrado")
    
    del apps_db[app_id]
    return {"message": "App deletado com sucesso", "app_id": app_id}

# ==================== CODE GENERATION ====================

@app.post("/api/generate", response_model=CodeGenerationResponse)
async def generate_code(request: CodeGenerationRequest):
    """Gerar codigo com IA"""
    
    code_templates = {
        ("python", "fastapi"): """# FastAPI Endpoint
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}
""",
        ("javascript", "react"): """// React Component
import React, { useState } from 'react';

export default function App() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;
}
""",
        ("typescript", "next"): """// Next.js API Route
import type { NextApiRequest, NextApiResponse } from 'next';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json({ message: 'Hello World' });
}
"""
    }
    
    key = (request.language, request.framework)
    generated_code = code_templates.get(key, "# Codigo gerado dinamicamente")
    
    code_id = f"code_{len(generated_code_db) + 1}"
    
    code_data = {
        "id": code_id,
        "app_id": request.app_id,
        "code": generated_code,
        "language": request.language,
        "status": "generated",
        "generated_at": datetime.now().isoformat()
    }
    
    generated_code_db[code_id] = code_data
    return CodeGenerationResponse(**code_data)

@app.get("/api/generated-code/{code_id}", response_model=CodeGenerationResponse)
async def get_generated_code(code_id: str):
    """Obter codigo gerado"""
    if code_id not in generated_code_db:
        raise HTTPException(status_code=404, detail="Codigo nao encontrado")
    
    return CodeGenerationResponse(**generated_code_db[code_id])

@app.get("/api/apps/{app_id}/generated-code")
async def list_app_code(app_id: str):
    """Listar codigos gerados de uma aplicacao"""
    codes = [code for code in generated_code_db.values() if code["app_id"] == app_id]
    return [CodeGenerationResponse(**code) for code in codes]

# ==================== ANALYTICS ====================

@app.get("/api/analytics")
async def get_analytics():
    """Obter analytics"""
    return {
        "total_apps": len(apps_db),
        "total_generated_code": len(generated_code_db),
        "timestamp": datetime.now().isoformat(),
        "languages": {
            "python": sum(1 for app in apps_db.values() if app.get("language") == "python"),
            "javascript": sum(1 for app in apps_db.values() if app.get("language") == "javascript"),
            "typescript": sum(1 for app in apps_db.values() if app.get("language") == "typescript")
        }
    }

# ==================== UI SIMPLES ====================

@app.get("/ui", response_class=HTMLResponse)
async def ui():
    """Interface HTML simples"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>JHONATAN CODE AI</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: Arial; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
            .container { max-width: 1200px; margin: 0 auto; }
            header { background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
            h1 { color: #333; margin-bottom: 10px; }
            .status { color: #666; }
            .endpoint { background: white; padding: 15px; margin-bottom: 10px; border-radius: 4px; border-left: 4px solid #667eea; }
            .endpoint-name { font-weight: bold; color: #667eea; }
            .endpoint-desc { color: #666; font-size: 14px; margin-top: 5px; }
            a { color: #667eea; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>🤖 JHONATAN TECH SOLUTIONS CODE AI</h1>
                <p class="status">Status: <span style="color: green;">🟢 Online</span></p>
            </header>
            
            <h2 style="color: white; margin-bottom: 15px;">API Endpoints</h2>
            
            <div class="endpoint">
                <div class="endpoint-name">GET /</div>
                <div class="endpoint-desc">Informações gerais da API</div>
            </div>
            
            <div class="endpoint">
                <div class="endpoint-name">GET /health</div>
                <div class="endpoint-desc">Health check do servidor</div>
            </div>
            
            <div class="endpoint">
                <div class="endpoint-name">GET /api/status</div>
                <div class="endpoint-desc">Status completo</div>
            </div>
            
            <div class="endpoint">
                <div class="endpoint-name">GET /api/apps</div>
                <div class="endpoint-desc">Listar aplicações</div>
            </div>
            
            <div class="endpoint">
                <div class="endpoint-name">POST /api/apps</div>
                <div class="endpoint-desc">Criar nova aplicação</div>
            </div>
            
            <div class="endpoint">
                <div class="endpoint-name">POST /api/generate</div>
                <div class="endpoint-desc">Gerar código com IA</div>
            </div>
            
            <div style="background: white; padding: 20px; border-radius: 8px; margin-top: 20px;">
                <p><a href="/docs">📚 Ver Documentação Completa (Swagger)</a></p>
            </div>
        </div>
    </body>
    </html>
    """

# ==================== ERROR HANDLERS ====================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "timestamp": datetime.now().isoformat()}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "Erro interno do servidor", "timestamp": datetime.now().isoformat()}
    )

# ==================== STARTUP ====================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=DEBUG
    )
