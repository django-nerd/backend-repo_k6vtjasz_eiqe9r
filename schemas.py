"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (you can keep or remove if unused):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: Optional[str] = Field(None, description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Clinic-specific schemas

class AppointmentRequest(BaseModel):
    """
    Appointment requests submitted from website (non-PHI)
    Collection name: "appointmentrequest"
    """
    full_name: str = Field(..., min_length=2, max_length=120, description="Full name")
    phone: str = Field(..., min_length=7, max_length=40, description="Contact phone number")
    email: EmailStr = Field(..., description="Contact email address")
    preferred_datetime: Optional[str] = Field(None, description="Preferred date/time text from user")
    message: Optional[str] = Field(None, max_length=1000, description="General non-medical message")
    confirmed_no_phi: bool = Field(..., description="User confirmed no medical info submitted")
