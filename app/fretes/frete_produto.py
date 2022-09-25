from flask import Blueprint, request, make_response, jsonify,current_app, Response, abort
from functools import wraps
from flask_restx import Resource, Api, fields



def retornafrete(f):
    @wraps(f)
    def insert_Valores(*args, **kwds):
        print('Insere valores nas tabelas')
        return f(*args, **kwds)
    return insert_Valores


@retornafrete
def gera_log():
    """Recebe parametros de entrada"""
    print('registra log acoes')


frete_bp = Blueprint("api",__name__)

from ..models.serializer import ProdutosSchema, FretesSchema, MarcasSchema
from ..models.models import Produtos, MarcaProduto, Usuarios, LogUsuario

from ..extensions import db


api = Api(current_app)

produtos = [{"referenciasku":"aaaaa","id":12,"quantidade":22,"cep":"13013000"}
    ,{"referenciasku":"bbbb","id":18,"quantidade":22,"cep":"13013000"}]


api_model = api.model('Produtos',{'referenciasku':fields.String,
 'id':fields.Integer,'quantidade':fields.Float, 'cep':fields.String})

@api.route('/api/v1/fretes/all')
class ExibeFretes(Resource):
    @api.expect(api_model, envelope='Produtos')
    def get(self):
        if request.method=='GET':
            return {"valor":produtos},201
        return {"error":"naoencontrado"}, 404
    

@api.route('/api/v1/fretes/add')
class AdicionaFrete(Resource):
    """
    cria frete e insere no banco
    """
    @api.expect(api_model, envelope='Produtos')
    def post(self):
        if request.method == 'POST':
            valor = request.json
            produtos.append(api.payload)
          
 
            return {"ok":valor},201
        return {"valor":"invalido"}, 404


class RetornaUnitario(Resource):pass