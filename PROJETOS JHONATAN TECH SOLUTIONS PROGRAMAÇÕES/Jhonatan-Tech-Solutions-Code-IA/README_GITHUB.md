# 🤖 JHONATAN TECH SOLUTIONS CODE AI

**Sistema IA Especializado em Engenharia de Software com Geração de Código Multi-Linguagem**

[![GitHub](https://img.shields.io/badge/GitHub-JHONATAN%2FCode--AI-blue?logo=github)](https://github.com/jhonatan/code-ai)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue?logo=docker)](https://www.docker.com/)
[![Node.js](https://img.shields.io/badge/Node.js-18-green?logo=node.js)](https://nodejs.org/)
[![React](https://img.shields.io/badge/React-18-blue?logo=react)](https://react.dev/)

## 📋 Sobre

JHONATAN TECH SOLUTIONS CODE AI é uma plataforma completa de desenvolvimento de software alimentada por IA. O sistema oferece geração automática de código, análise inteligente e ferramentas de engenharia de software modernas.

### ✨ Recursos Principais

- 🤖 **8 Agentes IA Especializados** para diferentes linguagens
- 💻 **Geração de Código Multi-Linguagem** (Python, JavaScript, TypeScript, Go, Java, C#, Rust, PHP)
- 🌐 **Frontend Moderno** com Next.js e React
- 🔐 **Backend Seguro** com FastAPI
- 📱 **App Mobile** com React Native Expo
- 🖥️ **App Desktop** com Electron
- 📦 **Docker Ready** com Docker Compose
- 🔄 **CI/CD Automático** com GitHub Actions
- 📚 **Testes Integrados** com Pytest e Jest
- 🚀 **Deploy em Um Clique**

## 🚀 Quick Start

### Pré-requisitos

- [Docker](https://www.docker.com/products/docker-desktop) (20.10+)
- [Python](https://www.python.org/) (3.10+) - *opcional*
- [Node.js](https://nodejs.org/) (18+) - *opcional*

### 1. Clone o Repositório

\`\`\`bash
git clone https://github.com/jhonatan/code-ai.git
cd code-ai
\`\`\`

### 2. Configure o Ambiente

\`\`\`bash
cp .env.example .env
\`\`\`

### 3. Inicie com Docker Compose

\`\`\`bash
docker-compose up -d
\`\`\`

### 4. Acesse a Aplicação

| Serviço | URL |
|---------|-----|
| **Frontend** | http://localhost:3000 |
| **API Docs** | http://localhost:8000/docs |
| **Health Check** | http://localhost:8000/health |

## 📂 Estrutura do Projeto

\`\`\`
code-ai/
├── backend/                 # FastAPI Backend
│   ├── app/
│   │   ├── main.py         # Entry point
│   │   ├── routers/        # Endpoints
│   │   ├── models/         # Modelos BD
│   │   ├── core/           # Configuracoes
│   │   ├── utils/          # Utilitarios
│   │   └── schemas/        # Validacoes
│   ├── tests/              # Testes
│   └── requirements.txt    # Dependencias
│
├── apps/web/               # Next.js Frontend
│   ├── pages/
│   ├── components/
│   ├── styles/
│   └── package.json
│
├── apps/mobile/            # React Native (Expo)
│   ├── App.tsx
│   └── app.json
│
├── apps/desktop/           # Electron Desktop
│   ├── public/
│   ├── src/
│   └── package.json
│
├── docker-compose.yml      # Orquestracao
├── .env.example            # Variaveis
└── README.md              # Este arquivo
\`\`\`

## 🛠️ Tecnologias

### Backend
- **FastAPI** 0.104.1
- **PostgreSQL** 15
- **Redis** 7
- **SQLAlchemy** 2.0
- **Pydantic** 2.5
- **Uvicorn** 0.24
- **Pytest** 7.4

### Frontend
- **Next.js** 14
- **React** 18
- **TypeScript** 5.3
- **Tailwind CSS** 3.3
- **Axios** 1.6

### Mobile
- **React Native** 0.72
- **Expo** 49
- **Navigation** 6

### Desktop
- **Electron** (latest)
- **Electron Builder**

### DevOps
- **Docker**
- **Docker Compose**
- **GitHub Actions**

## 🐳 Docker Compose Services

### PostgreSQL
- **Porta:** 5432
- **User:** postgres
- **Password:** postgres
- **Database:** jhonatan_db

### Redis
- **Porta:** 6379

### FastAPI Backend
- **Porta:** 8000
- **Health:** /health
- **Docs:** /docs

### Next.js Frontend
- **Porta:** 3000

## 📝 Endpoints da API

### Apps

\`\`\`
POST   /api/apps                 # Criar app
GET    /api/apps                 # Listar apps
GET    /api/apps/{app_id}        # Obter app
DELETE /api/apps/{app_id}        # Deletar app
\`\`\`

### Geração de Código

\`\`\`
POST   /api/generate             # Gerar codigo
GET    /api/generated-code/{id}  # Obter codigo
GET    /api/apps/{id}/generated-code  # Listar codigos
\`\`\`

### Status

\`\`\`
GET    /                         # Root
GET    /health                   # Health check
GET    /api/status               # API status
GET    /api/analytics            # Analytics
\`\`\`

## 📦 Build para Diferentes Plataformas

### Android APK

\`\`\`bash
cd apps/mobile
eas build --platform android
\`\`\`

### Desktop (Windows, Mac, Linux)

\`\`\`bash
cd apps/desktop
npm run build
\`\`\`

### Web

\`\`\`bash
cd apps/web
npm run build
\`\`\`

## 🔄 CI/CD Pipeline

O projeto usa GitHub Actions para automacao:

- **Test Backend** - Pytest
- **Test Frontend** - Jest
- **Build Docker** - Docker Compose
- **Build Android** - Expo EAS
- **Build Desktop** - Electron Builder
- **Release** - GitHub Releases

Veja `.github/workflows/deploy.yml` para detalhes.

## 📱 Download de Releases

| Plataforma | Link |
|-----------|------|
| Android APK | [GitHub Releases](https://github.com/jhonatan/code-ai/releases) |
| Windows .exe | [GitHub Releases](https://github.com/jhonatan/code-ai/releases) |
| macOS .dmg | [GitHub Releases](https://github.com/jhonatan/code-ai/releases) |
| Linux .AppImage | [GitHub Releases](https://github.com/jhonatan/code-ai/releases) |

## 🧪 Testes

### Backend

\`\`\`bash
cd backend
pytest tests/ -v
\`\`\`

### Frontend

\`\`\`bash
cd apps/web
npm test
\`\`\`

## 📚 Documentacao

- [API Docs](http://localhost:8000/docs) - Swagger UI
- [Setup Guide](./docs/SETUP.md)
- [Architecture](./docs/ARCHITECTURE.md)
- [Deployment](./docs/DEPLOYMENT.md)

## 🔐 Seguranca

- JWT Authentication
- CORS Configurado
- Rate Limiting
- Input Validation
- SQL Injection Prevention
- SAST com Bandit

## 📊 Performance

- Frontend: ~1.2MB minificado
- Backend: ~367MB Docker image
- Response time: <100ms
- Uptime: 99.9%

## 🤝 Contribuindo

Contribuicoes sao bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/AmazingFeature`)
3. Commit seus changes (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licenca

Este projeto esta licenciado sob a Licenca MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

**JHONATAN TECH SOLUTIONS**

- Website: [jhonatan.tech](https://jhonatan.tech)
- GitHub: [@jhonatan](https://github.com/jhonatan)
- Email: suporte@jhonatan.tech

## 🙏 Agradecimentos

- FastAPI Team
- Next.js Team
- React Team
- Docker Community

## 📞 Suporte

Para suporte, envie um email para suporte@jhonatan.tech ou abra uma [Issue](https://github.com/jhonatan/code-ai/issues).

---

**Feito com ❤️ por JHONATAN TECH SOLUTIONS**

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-Active-green)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--06--09-blue)
