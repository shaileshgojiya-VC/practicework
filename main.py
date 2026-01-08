## Importing necessary libraries
from apps.server import app
import os
import dotenv
import path 

dotenv.load_dotenv(path.join(path.dirname(__file__), ".env"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="SERVER_HOST", port=SERVER_PORT)