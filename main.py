# backend/main.py,
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
#import logging
import urllib.parse
from llm_model import TextModel
from dotenv import load_dotenv
from logging_config import setup_logger
load_dotenv()
PKG_NAME= os.getenv("LOG_PKG")
model_dir = os.getenv("MODEL_DIR")
model_name = os.getenv("MODEL_NAME")

app = FastAPI()

# Set up logging
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger("uvicorn")
logger = setup_logger(pkgname=PKG_NAME)
# Function to get origins safely
def get_origins():
    # Get the frontend URL from environment variables with fallback options
    frontend_url = os.getenv("FRONTEND_URL", "https://www.askmeai.de")
    frontend_dns = os.getenv("FRONTEND_DNS", "https://www.askmeai.de")
    #dev_url = os.getenv("DEV_URL", "")
    # Build the list of origins
    origins = [
        frontend_url,  # Custom domain from environment
         frontend_dns
    ]
    # Remove any empty origins
    origins = [origin for origin in origins if origin]
    # Return the list of origins
    return origins, frontend_url, frontend_dns

# Add CORS middleware with the origins list
origins, frontend_url, frontend_dns = get_origins()  # Call the function to get origins
logger.info(f"Allowed origins: {origins}")
# Add CORS middleware with the origins list
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Use the origins list
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)

# Startup event to log origins
@app.on_event("startup")
async def startup_event():
    #origins = get_origins()  # Reuse the same function to get origins
    # Log the origins with more context
    logger.info("CORS Configuration on Startup:")
    logger.info(f"Number of allowed origins: {len(origins)}")

     # Define the sources for each origin
    origin_sources = {
        "Frontend_URL": frontend_url,
        "Frontend_DNS": frontend_dns
    }
     # Log each origin with its source
    for key, item in origin_sources.items():
        logger.info(f"domain -> {item}; Source -> {key}")
    
    # Optional: Validate origins
    for origin in origins:
        try:
            parsed_url = urllib.parse.urlparse(origin)
            if not all([parsed_url.scheme, parsed_url.netloc]):
                logger.warning(f"Invalid origin format: {origin}")
        except Exception as e:
            logger.error(f"Error parsing origin {origin}: {e}", exc_info=True)
    """ This function will run when the FastAPI application starts. """
    # Initialize the model
    global model
    logger.info(f"Loading {model_name} from {model_dir}")
    model = TextModel(model_name=model_name, model_dir=model_dir)
    # Log or print that the model is loaded
    logger.info(f"Model {model_name} loaded from {model_dir}")


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
async def health():
    return {"status": "OK"}

@app.get("/search")
async def get_response(query: str = Query(...)) -> dict:
    """
    Handle search queries by generating response using text model
    
    Args:
        query(str): Input query in string format.
    Returns:
        dict: A dictionary containing response under key "result"
    Raises:
        Exeception: If there is an error during model response generation.
    """
    try:
        response = model.model_response(message=query)
        #response = f"{query}, How are you ?"
        return {"result": response}
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        return {"error": "An error occurred while processing your request"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "localhost"),
        port=int(os.getenv("PORT", 2000)),
        reload_includes=["config.py"],
        reload=False
    )
