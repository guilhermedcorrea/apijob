#imports Python
from flask_sqlalchemy import SQLAlchemy

#Imports Modulos
from ..extensions import db


class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer,  primary_key = True)
    nome =db.Column(db.String(255))
    password_hash= db.Column(db.String(255))
    bitusuario = db.Column(db.Boolean, nullable=False)
    bitlogado = db.Column(db.Boolean, nullable=False)
    datalogado = db.Column(db.DateTime, unique=False, nullable=True)
    datacadastro = db.Column(db.DateTime, unique=False, nullable=True)
    bitativo = db.Column(db.Boolean)

    def __repr__(self):
        return  f'<Nome>"{self.id_usuario}"'

 
class MarcaProduto(db.Model):
    __tablename__ = 'marcaproduto'
    idmarca = db.Column(db.Integer,  primary_key = True)
    marca = db.Column(db.String(100))
    bitativo = db.Column(db.Boolean, nullable=True)
    datacadastro = db.Column(db.DateTime, unique=False, nullable=True)
    bitativo = db.Column(db.Boolean)
    produtos = db.relationship('skuproduto', backref='idmarca')
    frete = db.relationship('marca', backref='idmarca')

    def __repr__(self):
        return  f'<Marca>"{self.marca}"'


class Produtos(db.Model):
    __tablename__ = 'produto'
    idproduto = db.Column(db.Integer, primary_key = True)
    skuproduto = db.Column(db.String(300),unique=False , nullable=True)
    nomeproduto =db.Column(db.String(1000),unique=False , nullable=True)
    idmarca = db.Column(db.Integer,db.ForeignKey('marcaproduto.idmarca'))
    urlpaginaproduto = db.Column(db.String(2000),unique=False , nullable=True)
    peso = db.Column(db.Float,unique=False , nullable=True)
    altura = db.Column(db.Float,unique=False , nullable=True)
    largura = db.Column(db.Float,unique=False , nullable=True)
    bitativo = db.Column(db.Boolean,unique=False ,nullable=True)
    dataalterado = db.Column(db.DateTime, unique=False, nullable=True)
    frete = db.relationship('idproduto', backref='idproduto')

    def __repr__(self):
        return  f'<SKU>"{self.idproduto}"'

class CotacaoFrete(db.Model):
    __tablename__ = 'cotacaofrete'
    idfrete = db.Column(db.Integer, primary_key = True)
    idmarca = db.Column(db.Integer,db.ForeignKey('marcaproduto.idmarca')) #adicionar
    idproduto = db.Column(db.Integer,db.ForeignKey('produto.idproduto'))#adicionar
    cep = db.Column(db.String(20))
    categoriafrete = db.Column(db.String(50))
    valorFrete = db.Column(db.Float)
    prazo = db.Column(db.Integer)
    transportadora = db.Column(db.String(200))
    dacotacao = db.Column(db.DateTime, unique=False, nullable=True)
    log = db.relationship('idfrete', backref='idfrete')

    def __repr__(self):
        return f'<idfrete>"{self.idfrete}"'

class LogUsuario(db.Model):
    __tablename__ = 'logusuario'
    idlog = db.Column(db.Integer, primary_key = True)
    idusuario = db.Column(db.Integer,db.ForeignKey('usuarios.id_usuario'))
    idfrete = db.Column(db.Integer, db.ForeignKey('cotacaofrete.idfrete'))
    datalog = db.Column(db.DateTime, unique=False, nullable=True)

    def __repr__(self):
        return f'<idfrete>"{self.idlog}"'

