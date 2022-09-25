"""Arquivo de configurações do APP"""

from dotenv import load_dotenv
from os import path
import os


#String Conexao banco de dados
load_dotenv()
uri_database = driver = os.getenv('stringcon')

secret_key = driver = os.getenv('SECRET_KEY')