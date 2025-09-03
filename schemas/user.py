from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., pattern=r"^[a-zA-Z\s]+$", description="Name should only contain letters and spaces")
    email: str
    age: int = Field(..., gt=0, description="Age must be a positive integer")

