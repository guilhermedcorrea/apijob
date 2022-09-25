"""Classes Schemmas- Serializa Informações vindas das databases"""

from marshmallow import Schema, fields as ma_fields


#Schema/Produtos
class ProdutosSchema(Schema):
    id = ma_fields.Integer()
    user_id = ma_fields.Integer()
    nomeproduto = ma_fields.String()
    eanproduto = ma_fields.String()
    categoriaproduto = ma_fields.String()
    idmarca = ma_fields.Integer()
    sku = ma_fields.String()

#Schema/Fretes
class FretesSchema(Schema):
    idfrete = ma_fields
    cep = ma_fields
    valorFrete = ma_fields
    prazo = ma_fields
    transportadora = ma_fields
    dacotacao = ma_fields

#Schema/Usuario - Cadastro login e senha para acesso aos endpoints
class UsuariosSchema(Schema):
    id_usuario = ma_fields.Integer()
    nome = ma_fields.String()
    email = ma_fields.String()
    password_hash= ma_fields.String()
    bitusuario = ma_fields.Boolean()
    bitlogado = ma_fields.Boolean()
    datalogado = ma_fields.DateTime()
    datacadastro = ma_fields.DateTime()
    bitativo = ma_fields.Boolean()

#Schema/Marcas
class MarcasSchema(Schema):
    idmarca = ma_fields
    marca = ma_fields
    bitativo = ma_fields
    datacadastro = ma_fields

#Schema/Log Alterações e Cotações
class LogUsuariosSchema(Schema):
    idlog = ma_fields.Integer()
    idusuario = ma_fields.Integer()
    referenciaproduto = ma_fields
    dias  = ma_fields.Integer()
    valor = ma_fields.Float()
    tipo = ma_fields.String()
    datalog = ma_fields.DateTime()

