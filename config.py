"""Arquivo de configurações do APP"""

from dotenv import load_dotenv
from os import path
import os


#String Conexao banco de dados
load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))

URI_DATABASE = 'sqlite:///' + os.path.join(basedir, 'kabumdbapi.db')
print(URI_DATABASE)
