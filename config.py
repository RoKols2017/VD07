# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_default_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
