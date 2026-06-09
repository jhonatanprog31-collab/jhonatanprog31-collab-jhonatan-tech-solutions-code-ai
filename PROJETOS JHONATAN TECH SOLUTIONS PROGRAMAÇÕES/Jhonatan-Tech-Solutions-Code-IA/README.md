# 🤖 JHONATAN TECH SOLUTIONS CODE AI

**Complete AI-Powered Software Engineering Platform with Web, Desktop, and Mobile Applications**

![Status](https://img.shields.io/badge/Status-Active-green) ![Version](https://img.shields.io/badge/Version-1.0.0-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## 🌟 Features

- ✨ **AI Code Generation** - Generate code snippets using artificial intelligence
- 🤖 **8 Specialized Agents** - Domain-specific AI agents for different tasks
- 🔐 **Secure Sandbox** - Isolated execution environment for generated code
- 📊 **Real-time Monitoring** - Monitor application performance and health
- 🔄 **Automatic CI/CD** - GitHub Actions pipeline with automated testing and deployment
- 🧪 **Integrated Testing** - Comprehensive test suite with coverage reports
- 📱 **Multi-Platform** - Web, Desktop (Windows/Mac/Linux), and Mobile (Android)
- 🐳 **Docker Optimized** - Alpine-based images with minimal footprint
- 🎯 **Production Ready** - Security scanning, type checking, and quality gates

## 📋 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker Desktop 4.0+
- Git
- 8GB RAM
- 20GB disk space

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/jhonatan-code-ai.git
cd jhonatan-code-ai
```

2. **Setup environment**
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. **Run setup script**

**Windows:**
```bash
scripts\setup.bat
```

**Linux/Mac:**
```bash
bash scripts/setup.sh
```

4. **Start the application**
```bash
docker-compose up
```

5. **Access applications**
- 🌐 **Frontend**: http://localhost:3000
- 📚 **API Documentation**: http://localhost:8000/docs
- 🏥 **Health Check**: http://localhost:8000/health

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    Frontend Layer                         │
├──────────────────┬──────────────────┬────────────────────┤
│   Web (Next.js)  │  Desktop (Electron)  │ Mobile (Expo)  │
│   Port: 3000     │  Windows/Mac/Linux   │   Android      │
└────────┬─────────┴──────────┬──────────┴─────────┬────────┘
         │                    │                     │
         └────────────────────┼─────────────────────┘
                              │
         ┌────────────────────┴────────────────────┐
         │                                         │
         ▼                                         ▼
┌─────────────────────────────────┐    ┌──────────────────────┐
│   Backend API (FastAPI)         │    │  Cache & Queue       │
│   Port: 8000                    │    │  - Redis: 6379       │
│                                 │    │  - Celery: Tasks     │
│   Core Services:                │    └──────────────────────┘
│   - Auth & Security             │
│   - Code Generation             │
│   - Agent Management            │
│   - Data Processing             │
└─────────────────────────────────┘
         │
         ├──────────────────┬──────────────────┐
         │                  │                  │
         ▼                  ▼                  ▼
    ┌─────────┐        ┌────────┐        ┌────────┐
    │PostgreSQL       Redis         Celery  │
    │5432            6379           Workers │
    └─────────┘        └────────┘        └────────┘
```

## 📁 Project Structure

```
jhonatan-code-ai/
├── backend/                          # FastAPI backend
│   ├── app/
│   │   ├── main.py                  # Application entry
│   │   ├── core/                    # Configuration, database, security
│   │   ├── routers/                 # API endpoints
│   │   ├── schemas/                 # Pydantic models
│   │   ├── models/                  # SQLAlchemy models
│   │   └── utils/                   # Utility functions
│   ├── tests/                       # Unit tests
│   ├── requirements.txt             # Python dependencies
│   └── Dockerfile                   # Docker image
│
├── apps/
│   ├── web/                         # Next.js web frontend
│   │   ├── pages/                   # Pages and routing
│   │   ├── components/              # React components
│   │   ├── styles/                  # Tailwind CSS
│   │   └── package.json
│   │
│   ├── desktop/                     # Electron desktop app
│   │   ├── public/                  # Electron main process
│   │   └── package.json
│   │
│   └── mobile/                      # React Native Expo app
│       ├── App.tsx                  # Mobile app
│       └── app.json                 # Expo config
│
├── .github/
│   └── workflows/                   # GitHub Actions
│       ├── ci-cd.yml               # Main pipeline
│       ├── security.yml            # Security scanning
│       ├── desktop.yml             # Desktop builds
│       └── mobile.yml              # Mobile builds
│
├── scripts/                         # Automation scripts
│   ├── setup.sh/bat                # Initial setup
│   └── deploy.sh                   # Deployment
│
├── docker-compose.yml              # Docker services
├── .env.example                    # Environment template
├── README.md                       # This file
└── SETUP_GUIDE.md                  # Detailed setup guide
```

## 🚀 API Endpoints

### Health & Status
```bash
GET /health                  # Service health
GET /api/health             # API health
GET /ping                   # Ping endpoint
```

### Code Generation
```bash
GET /api/code/languages     # List supported languages
POST /api/code/generate     # Generate code
```

Request:
```json
{
  "prompt": "Create a Python function to parse JSON",
  "language": "python",
  "context": "Optional context"
}
```

## 🧪 Testing

### Run All Tests
```bash
# Backend
cd backend
pytest tests/ --cov=app

# Frontend
cd apps/web
npm test
```

### Run Specific Test Suite
```bash
# Health checks
pytest backend/tests/test_api.py::TestHealth

# Code generation
pytest backend/tests/test_api.py::TestCodeGeneration
```

## 🔧 Development

### Backend Development
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Development
```bash
cd apps/web
npm install
npm run dev
```

### Code Quality

```bash
# Linting
flake8 backend/app
cd apps/web && npm run lint

# Type checking
mypy backend/app
cd apps/web && npm run type-check

# Formatting
black backend/app
cd apps/web && npx prettier --write .

# Security
bandit -r backend/app
safety check
```

## 🐳 Docker

### Build Images
```bash
docker-compose build
```

### Run Services
```bash
docker-compose up -d
```

### View Logs
```bash
docker-compose logs -f api
docker-compose logs -f web
```

### Stop Services
```bash
docker-compose down
```

## 🔐 Security

- ✅ Pydantic validation
- ✅ JWT authentication
- ✅ Password hashing with bcrypt
- ✅ CORS configuration
- ✅ Security headers
- ✅ Bandit security scanning
- ✅ CodeQL analysis
- ✅ Dependency vulnerability checks

## 📊 Monitoring

- **Application Logs**: `docker-compose logs`
- **Database**: Connect with `psql` or pgAdmin
- **Cache**: Use `redis-cli`
- **API Docs**: http://localhost:8000/docs
- **Health Status**: http://localhost:8000/health

## 🚢 Deployment

### Docker Compose (Local/Development)
```bash
docker-compose up -d
```

### Production Deployment
```bash
bash scripts/deploy.sh
```

### Kubernetes (Optional)
```bash
kubectl apply -f deployment/k8s/
```

### Cloud Deployment
- **AWS**: ECS, EKS, or Lightsail
- **GCP**: Cloud Run, GKE
- **Azure**: Container Instances, AKS

## 🔄 CI/CD Pipeline

Automated pipeline runs on every push:

1. **Code Quality** - Linting, formatting, type checking
2. **Testing** - Unit tests with coverage
3. **Security** - Bandit, Safety, CodeQL scans
4. **Building** - Docker image builds
5. **Deployment** - To staging/production
6. **Releases** - Automatic version tagging

## 📱 Mobile Deployment

### Android
```bash
cd apps/mobile
eas build --platform android
```

### iOS
```bash
cd apps/mobile
eas build --platform ios
```

## 💻 Desktop Deployment

### Windows
```bash
cd apps/desktop
npm run dist
```

### macOS
```bash
cd apps/desktop
npm run dist
```

### Linux
```bash
cd apps/desktop
npm run dist
```

## 📚 Documentation

- [Setup Guide](./SETUP_GUIDE.md) - Detailed installation and configuration
- [API Documentation](http://localhost:8000/docs) - Interactive Swagger UI
- [Architecture Guide](./docs/ARCHITECTURE.md) - System design and components
- [Contributing Guide](./docs/CONTRIBUTING.md) - How to contribute

## 🆘 Troubleshooting

### Common Issues

**Port already in use**
```bash
docker-compose down
```

**Database connection failed**
```bash
docker-compose logs db
docker-compose restart db
```

**Frontend not loading**
```bash
rm -rf apps/web/.next
docker-compose rebuild web
```

### Debug Mode
```bash
DEBUG=True docker-compose up
```

## 📊 Performance

- **Frontend**: ~95 Lighthouse score
- **Backend**: <100ms response time
- **Database**: Optimized queries with indexing
- **Docker**: Alpine-based ~200MB images

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💼 Author

**Jhonatan Tech Solutions**
- Email: contact@jhonatan.tech
- Website: https://jhonatan.tech
- GitHub: [@jhonatan-tech](https://github.com/jhonatan-tech)

## 🙏 Acknowledgments

- FastAPI documentation
- Next.js community
- React Native Expo
- Electron framework
- GitHub Actions
- Docker community

## 📞 Support

For questions, issues, or suggestions:
1. Check [existing issues](https://github.com/jhonatan-tech/code-ai/issues)
2. Create a [new issue](https://github.com/jhonatan-tech/code-ai/issues/new)
3. Contact the team

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Status**: Active Development ✅

⭐ If you find this project useful, please give it a star!
