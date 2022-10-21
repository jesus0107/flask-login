from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = 'kZSA`12345A'

class DevelopmentConfig:
    DEBUG = True
    MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
    MYSQL_USER = os.environ['MYSQL_USER']
    MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
    MYSQL_HOST = os.environ['MYSQL_HOST']




settings = {
    "development": DevelopmentConfig
}