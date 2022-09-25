from ..extensions import db


class Usuarios(db.Model):
    """
    Recebe informaçoes de usuario| Foi necessario criar para que fosse possivel
    configurar o JWT para criar acesso de usuario da API
    """
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
    """
    Armazena informações referentes a Marca
    """
    __tablename__ = 'marcaproduto'
    idmarca = db.Column(db.Integer,  primary_key = True)
    marca = db.Column(db.String(100))
    bitativo = db.Column(db.Boolean, nullable=True)
    datacadastro = db.Column(db.DateTime, unique=False, nullable=True)
    bitativo = db.Column(db.Boolean)

    def __repr__(self):
        return  f'<Marca>"{self.marca}"'


class Produtos(db.Model):
    """
    Armazena Informações referentes aos produtos usados no calculo do frete
    Recebe chave estrangeira da tabea marca
    """
    __tablename__ = 'produto'
    idproduto = db.Column(db.Integer, primary_key = True)
    skuproduto = db.Column(db.String(300),unique=False , nullable=True)
    nomeproduto =db.Column(db.String(1000),unique=False , nullable=True)
    idmarca = db.Column(db.Integer,db.ForeignKey('marcaproduto.idmarca'))
    urlpaginaproduto = db.Column(db.String(2000),unique=False , nullable=True)
    peso = db.Column(db.Float,unique=False , nullable=True)
    altura = db.Column(db.Float,unique=False , nullable=True)
    largura = db.Column(db.Float,unique=False , nullable=True)
    comprimento = db.Column(db.Float,unique=False , nullable=True)
    bitativo = db.Column(db.Boolean,unique=False ,nullable=True)
    dataalterado = db.Column(db.DateTime, unique=False, nullable=True)
   
    def __repr__(self):
        return  f'<SKU>"{self.idproduto}"'


class CotacaoFrete(db.Model):
    """
    Armazena informações referente ao frete / calculo frete
    Recebe 2 chaves estrangeiras das tabelas Marca e Produto
    """
    __tablename__ = 'cotacaofrete'
    idfrete = db.Column(db.Integer, primary_key = True)
    idmarca = db.Column(db.Integer,db.ForeignKey('marcaproduto.idmarca'))
    idproduto = db.Column(db.Integer,db.ForeignKey('produto.idproduto'))
    cep = db.Column(db.String(20))
    categoriafrete = db.Column(db.String(50))
    valorFrete = db.Column(db.Float)
    prazo = db.Column(db.Integer)
    transportadora = db.Column(db.String(200))
    dacotacao = db.Column(db.DateTime, unique=False, nullable=True)
    #log = db.relationship('idfrete', backref='idfrete')


    def __repr__(self):
        return f'<idfrete>"{self.idfrete}"'

class LogUsuario(db.Model):
    """
    Armazena informações de usuario da sessao e algumas informaçoes de ações realizadas
    Recebe 2 chaves estrangeiras de Usuario e Cotacao
    """
    __tablename__ = 'logusuario'
    idlog = db.Column(db.Integer, primary_key = True)
    idusuario = db.Column(db.Integer,db.ForeignKey('usuarios.id_usuario'))
    idfrete = db.Column(db.Integer, db.ForeignKey('cotacaofrete.idfrete'))
    datalog = db.Column(db.DateTime, unique=False)

    def __repr__(self):
        return f'<idfrete>"{self.idlog}"'
    
    
