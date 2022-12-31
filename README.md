# schuna_fastapi

# alembic migration
alembic init migrations
alembic revision --autogenerate -m "Initial"
alembic upgrade head

# docker
- docker build -t fastapi-schuna .
- docker run -dp 80:80 --name fastapi-schuna -w /app -v %cd%:/app fastapi-schuna