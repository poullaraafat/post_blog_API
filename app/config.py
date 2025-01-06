import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # General Configurations
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
