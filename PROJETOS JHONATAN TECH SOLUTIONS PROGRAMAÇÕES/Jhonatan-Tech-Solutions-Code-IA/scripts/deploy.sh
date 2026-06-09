#!/bin/bash

# Deploy script for production

set -e

echo "🚀 Deploying JHONATAN TECH SOLUTIONS CODE AI"
echo "=============================================="

# Check environment
if [ ! -f .env ]; then
    echo "❌ .env file not found!"
    exit 1
fi

# Pull latest changes
echo "📥 Pulling latest changes..."
git pull origin main

# Build images
echo "🏗️ Building Docker images..."
docker-compose build --no-cache

# Stop old containers
echo "⛔ Stopping old containers..."
docker-compose down

# Start new containers
echo "🚀 Starting new containers..."
docker-compose up -d

# Run migrations
echo "🔄 Running database migrations..."
docker-compose exec -T api alembic upgrade head

# Health check
echo "🏥 Performing health checks..."
sleep 5

HEALTH=$(curl -s http://localhost:8000/health | grep -q "healthy" && echo "passed" || echo "failed")

if [ "$HEALTH" == "passed" ]; then
    echo "✅ Deployment successful!"
    echo ""
    echo "Access your application:"
    echo "  Frontend: http://localhost:3000"
    echo "  API: http://localhost:8000/docs"
else
    echo "❌ Deployment failed! Health check did not pass."
    docker-compose logs
    exit 1
fi
