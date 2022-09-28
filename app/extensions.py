from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restx import Api
from flask_jwt_extended import JWTManager
#from flask_migrate import Migrate
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
# imports/
"""
Imports referentes as Libs Flask Restx,  SQLAlchemy, Marshmallow e JWT- São excenciais para a construção da aplicaçao
Devido ao padrão de Projeto Factory e Blueprints  elas tem de ser importadas aqui e carregadas para os outros modulos. Do contrario
são levantados erros de importação Circular.
"""
api = Api()
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()


#Migrações de databases
migrate = Migrate()
