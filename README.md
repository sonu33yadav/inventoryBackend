# Inventory Management API

A simple inventory management REST API built with FastAPI, SQLAlchemy, and PostgreSQL.

## Project Overview

This project provides endpoints for managing:
- Products
- Customers
- Orders

It includes basic order creation logic with stock validation and order cancellation logic that restores stock.

## Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn
- Docker / Docker Compose
- python-dotenv

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd inventory
```

### 2. Create environment variables

Copy the example environment file and update values as needed:

```bash
copy .env.example .env
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run the application locally

```bash
python main.py
```

Then open:
- `http://localhost:8000`
- `http://localhost:8000/docs` for Swagger UI
- `http://localhost:8000/redoc` for ReDoc

## Docker Setup

### Local development with Docker Compose

```bash
docker-compose up -d
```

The app will be available at:
- `http://localhost:8000`

To stop the services:

```bash
docker-compose down
```

### Build image manually

```bash
docker build -t inventory-api:latest .
```

Run the container:

```bash
docker run -d --name inventory_app -p 8000:8000 --env-file .env inventory-api:latest
```

## Environment Variables

The project supports the following variables in `.env`:

```env
DATABASE_URL=postgresql://neondb_owner:your_password@your_host/neondb?sslmode=require&channel_binding=require
DB_USER=inventory_user
DB_PASSWORD=inventory_password
DB_NAME=inventory
CORS_ORIGINS=*
ENVIRONMENT=production
DEBUG=False
```

- `DATABASE_URL`: Primary SQLAlchemy database URL.
- `DB_USER`, `DB_PASSWORD`, `DB_NAME`: Used by `docker-compose.yml` for the local PostgreSQL service.
- `CORS_ORIGINS`: Allowed origins for CORS.
- `ENVIRONMENT` / `DEBUG`: application environment settings.

## API Endpoints

### Root & Health

- `GET /` - Welcome message
- `GET /health` - Health check

### Products

- `POST /products/` - Create product
- `GET /products/` - List products
- `GET /products/{product_id}` - Get product
- `PUT /products/{product_id}` - Update product
- `DELETE /products/{product_id}` - Delete product

Product schema:
- `name` (string)
- `sku` (string)
- `price` (float)
- `quantity` (integer)

### Customers

- `POST /customers/` - Create customer
- `GET /customers/` - List customers
- `GET /customers/{customer_id}` - Get customer
- `PUT /customers/{customer_id}` - Update customer
- `DELETE /customers/{customer_id}` - Delete customer

Customer schema:
- `full_name` (string)
- `email` (string)
- `phone` (string)

### Orders

- `POST /orders/` - Create order
- `GET /orders/` - List orders
- `GET /orders/{order_id}` - Get order
- `DELETE /orders/{order_id}` - Cancel order

Order creation requires:
- `customer_id` (integer)
- `items` (list of product IDs and quantities)

## Database

The application uses SQLAlchemy with the declarative base located in `database.py`.

- `models/product.py`
- `models/customer.py`
- `models/order.py`
- `models/order_item.py`

Database tables are created automatically on startup via `Base.metadata.create_all(bind=engine)`.

## Project Structure

```text
.
├── Dockerfile
├── docker-compose.yml
├── main.py
├── database.py
├── requirements.txt
├── .env.example
├── models/
│   ├── customer.py
│   ├── order.py
│   ├── order_item.py
│   └── product.py
├── routes/
│   ├── customers.py
│   ├── orders.py
│   └── products.py
└── schemas/
    ├── customer.py
    ├── order.py
    ├── order_item.py
    └── product.py
```

## Notes

- The local `docker-compose.yml` includes a PostgreSQL service for local development.
- If using an external DB, update `DATABASE_URL` and optionally disable the local `db` service.
- Swagger documentation is available automatically via FastAPI.

## License

This repository does not include a license file. Add one if you want to publish or share the project publicly.
