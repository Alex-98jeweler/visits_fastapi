import os

from dotenv import load_dotenv

load_dotenv('./.env')

DB_NAME = os.environ.get("DB_NAME", 'visits')
DB_USER = os.environ.get("DB_USER", 'postgres')
DB_PWD = os.environ.get("DB_PWD", 'postgres')
DB_HOST = os.environ.get("DB_HOST", 'localhost')
DB_PORT = os.environ.get("DB_PORT", '5432')


REDIS_URL = os.environ.get("REDIS_URL", 'redis://localhost/1')
REDIS_URL_TEST = os.environ.get("REDIS_URL_TEST", 'redis://localhost:8023/2')
