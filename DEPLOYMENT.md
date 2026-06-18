# Inventory Management API - Deployment Guide

## Prerequisites
- Docker and Docker Compose installed
- PostgreSQL database (Neon or local)
- Python 3.11+ (for local development)

## Deployment Options

### Option 1: Local Development with Docker Compose (Recommended for Testing)

#### Setup:
1. Create a `.env` file from the template:
```bash
copy .env.example .env
```

2. Update the `.env` file with your configuration (optional for local testing)

3. Start the application with Docker Compose:
```bash
docker-compose up -d
```

4. Verify the application is running:
```bash
curl http://localhost:8000/health
```

5. Access the API:
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

6. Stop the application:
```bash
docker-compose down
```

---

### Option 2: Production Deployment with External PostgreSQL

For production, use an external PostgreSQL database (like Neon):

#### Setup:
1. Create a `.env` file:
```bash
copy .env.example .env
```

2. Update `.env` with your production database URL:
```
DATABASE_URL=postgresql://user:password@host:5432/database?sslmode=require
CORS_ORIGINS=your-domain.com
```

3. Build the Docker image:
```bash
docker build -t inventory-api:latest .
```

4. Run the container:
```bash
docker run -d \
  --name inventory_app \
  -p 8000:8000 \
  --env-file .env \
  inventory-api:latest
```

5. Check logs:
```bash
docker logs inventory_app
```

---

### Option 3: Docker Compose with Neon Database (Recommended for Production)

Update the `docker-compose.yml` service `app` environment:

```yaml
environment:
  - DATABASE_URL=postgresql://user:password@your-neon-host/database?sslmode=require
  - CORS_ORIGINS=your-domain.com
```

Then run:
```bash
docker-compose up -d app
```

Note: The `db` service will not be used; comment it out if desired.

---

## Common Docker Commands

### View running containers:
```bash
docker-compose ps
```

### View logs:
```bash
docker-compose logs -f app
```

### Execute commands in container:
```bash
docker-compose exec app bash
```

### Rebuild the image:
```bash
docker-compose build --no-cache
```

### Stop and remove all containers/volumes:
```bash
docker-compose down -v
```

---

## Production Best Practices

1. **Environment Variables**: Always use `.env` files; never hardcode secrets
2. **Image Registry**: Push images to Docker Hub, AWS ECR, or similar:
   ```bash
   docker tag inventory-api:latest your-registry/inventory-api:latest
   docker push your-registry/inventory-api:latest
   ```

3. **Networking**: Use a reverse proxy (Nginx, Traefik) for production
4. **SSL/TLS**: Enable HTTPS for all external connections
5. **Scaling**: Use Kubernetes or Docker Swarm for multiple instances
6. **Monitoring**: Set up logging and monitoring with tools like ELK Stack or Datadog
7. **Backups**: Regular database backups for production data

---

## Troubleshooting

### Port already in use:
```bash
# Find process using port 8000
netstat -ano | findstr :8000
# Kill the process (Windows)
taskkill /PID <PID> /F
```

### Database connection issues:
```bash
# Test database connection
docker-compose exec app bash
python -c "from database import engine; print('Connected!')"
```

### Container fails to start:
```bash
docker-compose logs app
```

### Rebuild everything fresh:
```bash
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

---

## File Structure

- `Dockerfile` - Multi-stage build for optimal image size
- `docker-compose.yml` - Compose configuration for local/development
- `.dockerignore` - Files to exclude from Docker build
- `.env.example` - Template for environment variables
- `DEPLOYMENT.md` - This deployment guide

---

## Next Steps

1. Configure your environment variables in `.env`
2. Test locally with `docker-compose up`
3. Build and push to your registry
4. Deploy to your hosting platform (AWS, DigitalOcean, Heroku, etc.)
5. Set up CI/CD pipeline for automated deployments
