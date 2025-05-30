# FastAPI Template

A modular template for FastAPI projects with an organized structure and a `/tasks` resource example.

## Project Structure

```
fastapi-template/
├── app/
│   ├── client/
│   │   ├── __init__.py                # Client package exports
│   │   └── jsonplaceholder_client.py  # Example external API client
│   ├── config/
│   │   ├── __init__.py                # Configuration exports
│   │   ├── settings.py                # Application settings
│   │   ├── database.py                # SQLAlchemy database configuration
│   │   └── logger.py                  # Console logging configuration
│   ├── controllers/
│   │   ├── __init__.py                # Controllers exports
│   │   └── task_controller.py         # Task controller with input validation
│   ├── models/
│   │   ├── __init__.py                # Models exports
│   │   └── task.py                    # SQLAlchemy model definition
│   ├── routes/
│   │   ├── __init__.py                # Routes exports
│   │   └── task_routes.py             # Task routes with documentation
│   ├── schemas/
│   │   ├── __init__.py                # Schemas exports
│   │   ├── task.py                    # Pydantic validation schemas for tasks
│   │   └── jsonplaceholder.py         # Schemas for external API
│   ├── services/
│   │   ├── __init__.py                # Services exports
│   │   └── task_service.py            # Task service with business logic
│   └── utils/
│       ├── __init__.py        # Utils exports
│       ├── errors.py          # Custom error classes
│       └── error_handler.py   # Global error handler
├── migrations/                # Database migrations with Alembic
│   ├── versions/              # Migration versions
│   ├── env.py                 # Alembic environment configuration
│   └── script.py.mako         # Migration script template
├── alembic.ini                # Alembic configuration
├── main.py                    # Application entry point
├── run.py                     # Helper script to run the application
├── pyproject.toml             # Project metadata and dependencies
├── requirements.txt           # Project dependencies
├── .env.example               # Example environment variables
└── README.md                  # Project documentation
```

## Features

- Modular and scalable structure following clean architecture principles
- Separation of concerns with controllers, services, and models
- Centralized error handling with custom exception classes
- Data validation with Pydantic schemas
- Database migrations with Alembic
- Structured logging configuration
- Automatic documentation with Swagger/OpenAPI
- Complete CRUD resource example for tasks
- SQLite database with SQLAlchemy ORM
- External API client example with request/response schemas

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

### External API Client Example

The project also includes an example client for consuming the JSONPlaceholder API:

```python
# Import the client
from app.client.jsonplaceholder_client import JSONPlaceholderClient

# Get all posts
posts = await JSONPlaceholderClient.get_posts()

# Get a specific post
post = await JSONPlaceholderClient.get_post(post_id=1)

# Create a new post
from app.schemas.jsonplaceholder import PostRequest
post_data = PostRequest(title="New Post", body="This is the content", userId=1)
response = await JSONPlaceholderClient.create_post(post_data=post_data)

# Get user information
user = await JSONPlaceholderClient.get_user(user_id=1)
```

The client uses async methods with httpx for better performance and includes proper error handling with logging.

## Project Architecture

This project follows a clean architecture approach with clear separation of concerns:

- **Controllers**: Handle HTTP requests and responses, input validation
- **Services**: Contain business logic and interact with the database
- **Models**: Define database models using SQLAlchemy
- **Schemas**: Define data validation and serialization with Pydantic
- **Routes**: Define API endpoints and connect them to controllers
- **Config**: Application configuration and dependencies
- **Utils**: Utility functions and error handling
- **Client**: External API clients with proper request/response schemas

This architecture makes the codebase more maintainable, testable, and scalable.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.