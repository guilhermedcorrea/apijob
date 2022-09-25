"""Classes Schemmas- Serializa Informações vindas das databases"""

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.models import Produtos, LogUsuario,CotacaoFrete, MarcaProduto

#Schema/Produtos
class ProdutosSchema(SQLAlchemyAutoSchema):
    """
    Serializa e desserializa 
    """
    class Meta:
        model = Produtos
        include_relationships = True
        load_instance = True
        idproduto = auto_field()
        skuproduto = auto_field()
        idmarca = auto_field()
        nomeproduto = auto_field()
        idmarca = auto_field()
        urlpaginaproduto = auto_field()
        peso = auto_field()
        altura = auto_field()
        largura = auto_field()
        bitativo = auto_field()
        dataalterado = auto_field()


#Schema/Fretes
class FretesSchema(SQLAlchemyAutoSchema):
    """
    Serializa e desserializa 
    """
    class Meta:
        model = CotacaoFrete
        include_relationships = True
        load_instance = True
        idfrete = auto_field()
        idmarca = auto_field()
        idproduto = auto_field()
        cep = auto_field()
        categoriafrete = auto_field()
        valorFrete = auto_field()
        prazo = auto_field()
        transportadora = auto_field()
        dacotacao = auto_field()

  
#Schema/Usuario - Cadastro login e senha para acesso aos endpoints
class UsuariosSchema(SQLAlchemyAutoSchema):
    """
    Serializa e desserializa 
    """
    class Meta:
        model = Produtos
        include_relationships = True
        load_instance = True

        id_usuario = auto_field()
        nome = auto_field()
        password_hash= auto_field()
        bitusuario = auto_field()
        bitlogado = auto_field()
        datalogado = auto_field()
        datacadastro = auto_field()
        bitativo = auto_field()
  
#Schema/Marcas
class MarcasSchema(SQLAlchemyAutoSchema):
    """
    Serializa e desserializa 
    """
    class Meta:
        model = MarcaProduto
        include_relationships = True
        load_instance = True

        idmarca = auto_field()
        marca = auto_field()
        bitativo = auto_field()
        datacadastro = auto_field()
        bitativo = auto_field()


#Schema/Log Alterações e Cotações
class LogUsuariosSchema(SQLAlchemyAutoSchema):
    """
    Serializa e desserializa 
    """
    class Meta:
        model = LogUsuario
        include_relationships = True
        load_instance = True
        idlog = auto_field()
        idusuario = auto_field()
        idfrete = auto_field()
        datalog = auto_field()

