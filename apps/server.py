## Importing necessary libraries
from fastapi import FastAPI



app = FastAPI(
    title="FastAPI Boilerplate",
    description="A FastAPI boilerplate for building APIs",
    version="0.1.0",
    contact={
        "name": "John Doe",
        "email": "john.doe@example.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}