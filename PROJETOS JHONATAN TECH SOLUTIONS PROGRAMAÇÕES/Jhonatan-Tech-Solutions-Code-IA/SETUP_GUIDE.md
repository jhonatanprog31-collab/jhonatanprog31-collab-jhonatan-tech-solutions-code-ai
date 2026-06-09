# 🤖 JHONATAN TECH SOLUTIONS CODE AI - Complete Setup Guide

## System Requirements

- Python 3.10+
- Node.js 18+
- Docker Desktop 4.0+
- 8GB RAM minimum
- 20GB disk space

## Quick Start (5 minutes)

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/jhonatan-code-ai.git
cd jhonatan-code-ai
```

### 2. Setup Environment
```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Start Services
```bash
docker-compose up -d
```

### 4. Access Applications

- **Frontend**: http://localhost:3000
- **API Docs**: http://localhost:8000/docs
- **API Health**: http://localhost:8000/health
- **Database**: localhost:5432
- **Redis**: localhost:6379

## Architecture Overview

```
┌─────────────────────────────────────────────────┐
│         Frontend (Next.js + React)              │
│  Web: http://localhost:3000                     │
└────────────────────┬────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────┐
│    Backend API (FastAPI + Python)               │
│  http://localhost:8000                          │
│  - Authentication & Authorization               │
│  - Code Generation                              │
│  - Agent Management                             │
└────────────────────┬────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
    ┌────────┐  ┌────────┐  ┌────────┐
    │ PostgreSQL  Redis    Celery
    │ Database   Cache    Workers
    └────────┘  └────────┘  └────────┘
```

## File Structure

```
.
├── backend/                    # FastAPI application
│   ├── app/
│   │   ├── main.py            # Application entry point
│   │   ├── core/              # Configuration, security, database
│   │   ├── routers/           # API endpoints
│   │   ├── schemas/           # Pydantic models
│   │   ├── models/            # SQLAlchemy ORM models
│   │   └── utils/             # Utility functions
│   ├── tests/                 # Unit tests
│   ├── Dockerfile             # Docker configuration
│   └── requirements.txt        # Python dependencies
│
├── apps/
│   ├── web/                   # Next.js web frontend
│   │   ├── pages/             # Next.js pages
│   │   ├── components/        # React components
│   │   ├── styles/            # CSS styles
│   │   ├── package.json       # Node dependencies
│   │   └── Dockerfile         # Docker configuration
│   │
│   ├── desktop/               # Electron desktop app
│   │   ├── public/            # Electron main process
│   │   └── package.json       # Electron dependencies
│   │
│   └── mobile/                # React Native Expo app
│       ├── App.tsx            # Mobile app entry point
│       ├── app.json           # Expo configuration
│       └── package.json       # Expo dependencies
│
├── .github/
│   └── workflows/             # GitHub Actions
│       ├── ci-cd.yml          # Main CI/CD pipeline
│       ├── security.yml       # Security scanning
│       ├── desktop.yml        # Desktop builds
│       └── mobile.yml         # Mobile builds
│
├── docker-compose.yml         # Docker Compose configuration
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
└── README.md                  # Documentation
```

## Development Workflows

### Running Backend Locally

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

### Running Frontend Locally

```bash
cd apps/web
npm install
npm run dev
```

### Running Tests

```bash
# Backend tests
cd backend
pytest tests/ --cov=app

# Frontend tests
cd apps/web
npm test
```

### Building Docker Images

```bash
# Backend
docker build -t jhonatan-code-ai-backend ./backend

# Frontend
docker build -t jhonatan-code-ai-web ./apps/web

# Test locally
docker-compose up -d
```

## API Endpoints

### Health Check
- `GET /health` - Service health status
- `GET /api/health` - API health check

### Code Generation
- `POST /api/code/generate` - Generate code
  ```json
  {
    "prompt": "Create a Python function to parse JSON",
    "language": "python"
  }
  ```

- `GET /api/code/languages` - List supported languages

## Database Migrations

```bash
# Create migration
alembic revision --autogenerate -m "Add users table"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Deployment

### Production Deployment

1. Set environment variables in `.env`
2. Build optimized images:
   ```bash
   docker-compose -f docker-compose.yml build
   ```
3. Start services:
   ```bash
   docker-compose -f docker-compose.yml up -d
   ```

### Cloud Deployment (AWS, GCP, Azure)

Deploy Docker images to your preferred cloud platform:
- Push to Docker registry
- Deploy using Kubernetes or container services
- Configure environment variables
- Setup monitoring and logging

## Troubleshooting

### Port Already in Use
```bash
# Kill process on port 8000
lsof -i :8000 | grep LISTEN | awk '{print $2}' | xargs kill -9

# Or use docker-compose to stop
docker-compose down
```

### Database Connection Issues
```bash
# Check database status
docker-compose logs db

# Reset database
docker-compose down -v
docker-compose up -d
```

### Frontend Not Loading
```bash
# Clear next cache
rm -rf apps/web/.next

# Rebuild
docker-compose build web
docker-compose restart web
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## CI/CD Pipeline

The GitHub Actions pipeline runs on every push:

1. **Code Quality**: Linting, type checking, formatting
2. **Testing**: Unit tests with coverage reports
3. **Security**: Bandit, Safety, CodeQL scans
4. **Build**: Docker image building and pushing
5. **Deploy**: Deployment to staging/production
6. **Release**: Automatic version tagging

## Monitoring

- Frontend: Developer tools in browser
- Backend: API logs via `docker-compose logs api`
- Database: Connect with `psql` or pgAdmin
- Redis: Use `redis-cli` for inspection

## Support

For issues, questions, or suggestions:
1. Check existing GitHub issues
2. Create a new issue with detailed description
3. Contact the development team

## License

MIT License - See LICENSE file for details

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Maintained By**: Jhonatan Tech Solutions
