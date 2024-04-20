import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

try:
    database_url = os.getenv("DATABASE_URL")
except:
    raise ValueError("DATABASE_URL is not set in the environment")
