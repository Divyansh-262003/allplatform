import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
SQLITE_DB_PATH = os.path.join(INSTANCE_DIR, 'database.db')

class Config:
    # Ensure instance folder exists
    os.makedirs(INSTANCE_DIR, exist_ok=True)
    
    # Database
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLITE_DB_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'generate-a-good-key-here'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'generate-a-good-key-here'
    
    # Flask
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')
