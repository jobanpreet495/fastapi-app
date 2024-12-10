from fastapi import FastAPI
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




# Run the FastAPI app with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)