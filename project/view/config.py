import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///mila.db")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "default-jwt-secret")
    HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY", "default-hf-key")

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "default-jwt-secret")
    HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY", "default-hf-key")