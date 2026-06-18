from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routes import products_router, customers_router, orders_router
import os

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventory Management API",
    description="API for managing products, customers, and orders",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(products_router)
app.include_router(customers_router)
app.include_router(orders_router)


@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to Inventory Management API"}


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
