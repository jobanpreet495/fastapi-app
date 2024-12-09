from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI instance
app = FastAPI()

# Define a Pydantic model for request body validation
class Item(BaseModel):
    name: str
    description: str
    price: float

# POST endpoint
@app.post("/create-item/")
async def create_item(item: Item):
    # Log the received data
    print(f"Received item: {item}")
    
    # Return a response
    return {
        "message": "Item created successfully!",
        "item": {
            "name": item.name,
            "description": item.description,
            "price": item.price,
        },
    }

# Simple GET endpoint to check the server
@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI! Use /create-item/ to send a POST request."}
