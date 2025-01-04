import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # General Configurations
    SECRET_KEY = os.environ.get('SECRET_KEY')
