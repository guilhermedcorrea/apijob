#imports Python
from flask_sqlalchemy import SQLAlchemy

#Imports Modulos
from ..extensions import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    __table_args__ = {"schema": "usuarios"}
    id_usuario = db.Column(db.Integer,  primary_key = True)
    id_grupo = db.Column(db.Integer)
    nome =db.Column(db.String(255))
    email =db.Column(db.String(255))
    password_hash= db.Column(db.String(255))
    bitusuario = db.Column(db.Boolean, nullable=False)
    bitlogado = db.Column(db.Boolean, nullable=False)
    datalogado = db.Column(db.DateTime, unique=False, nullable=False)
    datacadastro = db.Column(db.DateTime, unique=False, nullable=False)
    grupo = db.Column(db.String(255))
    bitativo = db.Column(db.String(255))

    def __repr__(self):
        return self.id_usuario

 
class MarcaProduto(db.Model):
    __tablename__ = 'marcaproduto'
    __table_args__ = {"schema": "produtos"}
    idmarca = db.Column(db.Integer,  primary_key = True)
    marca = db.Column(db.Integer,  primary_key = True)
    bitativo = db.Column(db.Boolean, nullable=False)
    datacadastro = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return self.idmarca


class Produtos(db.Model):
    __tablename__ = 'produto'
    __table_args__ = {"schema": "produtos"}
    idproduto = db.Column(db.Integer, primary_key = True)
    skuproduto = db.Column(db.Integer,unique=False , nullable=True)
    nomeproduto =db.Column(db.String(255),unique=False , nullable=True)
    eanproduto = db.Column(db.String(255),unique=False , nullable=True)
    categoriaproduto = db.Column(db.String(255),unique=False , nullable=True)
    idmarca = db.Column(db.Integer,unique=False , nullable=True)
    sku = db.Column(db.String(255),unique=False , nullable=True)
    urlpaginaproduto = db.Column(db.String(2000),unique=False , nullable=True)
    peso = db.Column(db.Float,unique=False , nullable=True)
    altura = db.Column(db.Float,unique=False , nullable=True)
    largura = db.Column(db.Float,unique=False , nullable=True)
    bitativo = db.Column(db.Float,unique=False ,nullable=True)
    dataalterado = db.Column(db.DateTime, unique=False, nullable=True)

    def __repr__(self):
        return self.idproduto

class CotacaoFrete(db.Model):
    __tablename__ = 'cotacaofrete'
    __table_args__ = {"schema": "fretes"}
    idfrete = db.Column(db.Integer, primary_key = True)
    cep = db.Column(db.String)
    valorFrete = db.Column(db.Float)
    prazo = db.Column(db.Integer)
    transportadora = db.Column(db.String)
    dacotacao = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return self.idfrete


class LogUsuario(db.Model):
    __tablename__ = 'logusuario'
    __table_args__ = {"schema": "usuarios"}
    idlog = db.Column(db.Integer, primary_key = True)
    idusuario = db.Column(db.Integer)
    datalog = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return self.idlog

