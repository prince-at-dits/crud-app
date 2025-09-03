# FastAPI CRUD App

A simple CRUD (Create, Read, Update, Delete) application built with FastAPI, SQLAlchemy, and MySQL. This application provides user management functionality with JWT-based authentication.

## Features

- User registration and authentication
- JWT token-based authorization
- CRUD operations for users
- MySQL database integration
- CORS support for cross-origin requests
- Pydantic schemas for data validation

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8 or higher
- MySQL Server
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd crud-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv fastapi-env
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     fastapi-env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source fastapi-env/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy pymysql python-dotenv passlib[bcrypt] python-jose[cryptography] python-multipart
   ```

## Environment Setup

1. Create a `.env` file in the root directory of the project:
   ```env
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8080
   ```

   - `SECRET_KEY`: A secret key for JWT token signing
   - `ALGORITHM`: The algorithm used for JWT (default: HS256)
   - `ALLOWED_ORIGINS`: Comma-separated list of allowed origins for CORS

## Database Setup

1. Create a MySQL database named `crudapp`:
   ```sql
   CREATE DATABASE crudapp;
   ```

2. Update the database connection string in `config/db.py` if necessary:
   ```python
   engine = create_engine("mysql+pymysql://username:password@localhost/crudapp")
   ```

   Replace `username` and `password` with your MySQL credentials.

## Running the Application

1. Ensure the virtual environment is activated.

2. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

3. The application will be available at `http://localhost:8000`

4. Access the interactive API documentation at `http://localhost:8000/docs`

## API Endpoints

### Authentication

- `POST /auth/`: Create a new user account
- `POST /auth/token`: Login and obtain access token

### User Management (requires authentication)

- `GET /`: Get all users
- `GET /{id}`: Get user by ID
- `POST /`: Create a new user
- `PUT /{id}`: Update user by ID
- `DELETE /{id}`: Delete user by ID

## Authentication

To access protected endpoints, include the JWT token in the Authorization header:
```
Authorization: Bearer <your-jwt-token>
```

## Project Structure

```
crud-app/
├── main.py                 # FastAPI application entry point
├── app/
│   ├── auth/
│   │   └── auth_handler.py # Authentication logic
│   ├── api.py
│   └── model.py
├── config/
│   └── db.py               # Database configuration
├── models/
│   ├── index.py
│   └── user.py             # User model
├── routes/
│   ├── index.py
│   └── user.py             # User routes
├── schemas/
│   ├── index.py
│   └── user.py             # Pydantic schemas
├── fastapi-env/            # Virtual environment
├── .env                    # Environment variables
├── .gitignore
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is licensed under the MIT License.
