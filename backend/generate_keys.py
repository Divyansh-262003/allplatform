import secrets
import os
from dotenv import load_dotenv

def generate_env_file(env_type="development"):
    """Generate a .env file with secure keys"""
    env_content = f"""FLASK_ENV={env_type}
FLASK_APP=app.py
SECRET_KEY={secrets.token_hex(32)}
JWT_SECRET_KEY={secrets.token_hex(32)}
DEBUG={'True' if env_type == 'development' else 'False'}
"""
    
    filename = f".env.{env_type}"
    with open(filename, "w") as f:
        f.write(env_content)
    print(f"Generated {filename} with secure keys")

if __name__ == "__main__":
    # Generate development environment file
    generate_env_file("development")
    # Generate production environment file
    generate_env_file("production")
