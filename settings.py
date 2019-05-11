import pathlib  
from envparse import env

env.read_envfile()

BASE_PATH = pathlib.Path(__file__).parent

MYSQL_HOST = env('MYSQL_HOST', cast=str, default='localhost')
MYSQL_PORT = env('MYSQL_PORT', cast=int, default=3306)
MYSQL_USER = env('MYSQL_USER', cast=str)
MYSQL_PASSWORD = env('MYSQL_PASSWORD', cast=str)
MYSQL_DB = env('MYSQL_DB', cast=str)

DEBUG_LEVEL = env('DEBUG_LEVEL', cast=str, default='DEBUG')
