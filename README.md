# FastAPI Template

A modular template for FastAPI projects with an organized structure and a `/tasks` resource example.

## Project Structure

```
fastapi-template/
├── src/
│   ├── config/
│   │   ├── __init__.py        # Configuration exports
│   │   ├── settings.py         # Application settings
│   │   ├── database.py         # SQLAlchemy database configuration
│   │   └── logger.py           # Logging configuration
│   ├── controllers/
│   │   └── task_controller.py  # Task controller with input validation
│   ├── entities/
│   │   └── task.py             # SQLAlchemy entity definition
│   ├── routes/
│   │   └── task_routes.py      # Task routes with documentation
│   ├── schemas/
│   │   └── task.py             # Pydantic validation schemas for tasks
│   ├── services/
│   │   └── task_service.py     # Task service with business logic
│   ├── utils/
│   │   ├── errors.py           # Custom error classes
│   │   └── error_handler.py    # Global error handler
│   └── migrations/             # Database migrations with Alembic
│       ├── versions/           # Migration versions
│       ├── env.py              # Alembic environment configuration
│       └── script.py.mako      # Migration script template
│   ├── main.py                 # FastAPI application configuration
├── alembic.ini                 # Alembic configuration
├── main.py                     # Application entry point
├── .env.example                # Example environment variables
└── requirements.txt            # Project dependencies
```

## Features

- Modular and scalable structure following clean architecture principles
- Separation of concerns with controllers, services, and entities
- Centralized error handling with custom exception classes
- Data validation with Pydantic schemas
- Database migrations with Alembic
- Structured logging configuration
- Automatic documentation with Swagger/OpenAPI
- Complete CRUD resource example for tasks
- SQLite database with SQLAlchemy ORM

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file based on the provided example
5. Run database migrations:
   ```
   alembic upgrade head
   ```

## Execution

```
python main.py
```

The API will be available at `http://localhost:8000`.

- Swagger Documentation: `http://localhost:8000/docs`
- ReDoc Documentation: `http://localhost:8000/redoc`
- Health Check: `http://localhost:8000/healthz`

## Usage Example

The project includes a complete example of a `/tasks` resource with CRUD operations:

- `GET /api/tasks` - Get all tasks
- `GET /api/tasks/{task_id}` - Get a task by ID
- `POST /api/tasks` - Create a new task
- `PATCH /api/tasks/{task_id}` - Update an existing task
- `DELETE /api/tasks/{task_id}` - Delete a task

## Project Architecture

This project follows a clean architecture approach with clear separation of concerns:

- **Controllers**: Handle HTTP requests and responses, input validation
- **Services**: Contain business logic and interact with the database
- **Entities**: Define database models using SQLAlchemy
- **Schemas**: Define data validation and serialization with Pydantic
- **Routes**: Define API endpoints and connect them to controllers
- **Config**: Application configuration and dependencies
- **Utils**: Utility functions and error handling

This architecture makes the codebase more maintainable, testable, and scalable.
