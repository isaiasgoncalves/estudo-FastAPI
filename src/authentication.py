from passlib.context import CryptContext
from dotenv import load_dotenv
import os

SECRET_KEY = os.getenv("SECRET_KEY")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")