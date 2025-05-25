# FastAPI Template

A modular template for FastAPI projects with an organized structure and a `/tasks` resource example.

## Project Structure

```
fastapi-template/
├── app/
│   ├── api/
│   │   ├── tasks/
│   │   │   ├── router.py      # API routes for tasks
│   │   │   ├── schemas.py     # Pydantic schemas for validation
│   │   │   └── service.py     # Business logic for tasks
│   ├── core/
│   │   ├── app.py             # FastAPI application configuration
│   │   ├── config.py          # Configuration variables
│   │   └── error_handlers.py  # Global error handlers
│   ├── dependencies/
│   │   └── database.py        # Database dependencies
│   ├── models/
│   │   └── task.py            # SQLAlchemy models
│   └── utils/
│       └── exceptions.py      # Custom exceptions
├── main.py                    # Application entry point
└── requirements.txt           # Project dependencies
```

## Features

- Modular and scalable structure
- Centralized error handling
- Data validation with Pydantic
- Automatic documentation with Swagger/OpenAPI
- Complete CRUD resource example for tasks

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

## Execution

```
python main.py
```

The API will be available at `http://localhost:8000`.

- Swagger Documentation: `http://localhost:8000/docs`
- ReDoc Documentation: `http://localhost:8000/redoc`

## Usage Example

The project includes a complete example of a `/tasks` resource with CRUD operations:

- `GET /api/tasks` - Get all tasks
- `GET /api/tasks/{task_id}` - Get a task by ID
- `POST /api/tasks` - Create a new task
- `PATCH /api/tasks/{task_id}` - Update an existing task
- `DELETE /api/tasks/{task_id}` - Delete a task

This resource can serve as a base for developing new modules following the same pattern.
