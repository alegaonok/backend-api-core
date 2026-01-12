# Backend API Core

High-performance backend REST API built with FastAPI and PostgreSQL, designed following production-ready and scalable architecture practices.

## Overview

This project is a backend API intended to serve as a solid foundation for high-traffic applications.  
It focuses on clean architecture, clear separation of concerns, and readiness for real-world production environments.

The API will evolve to include authentication, background processing, database optimization, and deployment workflows.

## Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Poetry
- Docker (planned)
- Pytest

## Project Structure

```text
backend-api-core/
├── src/
│   └── app/
│       ├── api/        # API routes
│       ├── core/       # Configuration and core utilities
│       ├── db/         # Database setup and sessions
│       ├── models/     # ORM models
│       ├── schemas/    # Pydantic schemas
│       └── services/   # Business logic
├── tests/              # Automated tests
├── README.md
├── pyproject.toml
└── poetry.lock
