# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to manage a collection of items. Learn how to create endpoints, handle HTTP requests and responses, validate data, and structure a production-ready API.

## 📝 Tasks

### 🛠️ Create a FastAPI Application with CRUD Operations

#### Description
Create a FastAPI application that implements full CRUD (Create, Read, Update, Delete) operations for a simple resource. Use Pydantic models for data validation and learn how to structure API endpoints properly.

#### Requirements
Completed program should:

- Define a Pydantic model for the resource with appropriate data validation
- Implement GET endpoint to retrieve all items
- Implement GET endpoint with path parameter to retrieve a specific item by ID
- Implement POST endpoint to create a new item
- Implement PUT endpoint to update an existing item
- Implement DELETE endpoint to remove an item
- Return appropriate HTTP status codes for each operation

### 🛠️ Add Data Persistence and Error Handling

#### Description
Enhance the API with persistent storage and proper error handling. Implement validation checks and meaningful error responses for invalid requests.

#### Requirements
Completed program should:

- Store items in a file (JSON) or simple in-memory database
- Handle and return appropriate error responses (404, 400, etc.) with descriptive messages
- Validate input data and reject invalid requests with clear error descriptions
- Include request/response examples in docstrings or use Swagger documentation
- Test all endpoints to ensure they work correctly
