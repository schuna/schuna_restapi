#!/bin/sh

alembic upgrade head

exec uvicorn main:app --reload --host 0.0.0.0 --port 80