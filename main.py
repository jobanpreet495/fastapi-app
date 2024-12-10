from fastapi import FastAPI, Form
import uvicorn 

# Create a FastAPI instance
app = FastAPI()


# Simple GET endpoint to check the server
@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI GET Request"}


# Simple GET endpoint to check the server
@app.get("/health")
async def read_root():
    return {"message": "API is Healthy"}

@app.post("/add-numbers")
async def add_numbers(num1: float = Form(...), num2: float = Form(...)):
    """
    Add two numbers provided as form data and return the sum.
    """
    total = num1 + num2
    return {"num1": num1, "num2": num2, "sum": total}


# Run the FastAPI app with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
