from flask import Blueprint, request, make_response, jsonify,current_app, Response, abort
from functools import wraps
from flask_restx import Resource, Api, fields

from ..models.models import Produtos, LogUsuario, CotacaoFrete, Usuarios
from ..models.serializer import ProdutosSchema, FretesSchema, UsuariosSchema 
from .get_frete import MelhorEnvio

from itertools import groupby


import time
def register_handlers(app):
    if app.config.get('DEBUG') is True:
        app.logger.debug('Skipping error handlers in Debug mode')
        return


def retornafrete(f):
    @wraps(f)
    def insert_Valores(*args, **kwargs):

        print('Insere valores nas tabelas')
        return f(*args, **kwargs)
    return insert_Valores

@retornafrete
def gera_log(*args, **kwargs):
    """
    função pega id usuario da sessao, id frete cadastrado na tabela "CotacaoFrete"
    """
    """Recebe parametros de entrada"""
    #log =   LogUsuario(idusuario = , idfrete = datalog =)
    pass

#Handlers
def register_handlers(app):
    if current_app.config.get('DEBUG') is True:
        current_app.logger.debug('Skipping error handlers in Debug mode')
        return

    @current_app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"Error":"not found error"}), 404

    @current_app.errorhandler(500)
    def internal_error(error):
        return jsonify({"Error":"internal error"}), 500

    @current_app.errorhandler(500)
    def ModuleNotFoundError(*args, **kwargs):
        return jsonify({"Error":"Server Error"}), 500

    @current_app.errorhandler(404)
    def page_not_found(*args, **kwargs):
        return jsonify({"Error":"EndPoint NotFound"}), 404
   
    @current_app.errorhandler(405)
    def method_not_allowed_page(*args, **kwargs):
  
        return jsonify({"Error":"Method not found"}), 40


def key_func(key):
    return key['skuproduto']


def verifica_maiorquantidade(*args, **kwargs):
    if isinstance(kwargs, dict):
        
        items = sorted(list, key=lambda i: i['skuproduto'], reverse=True)
            
        for key, value in groupby(items, key_func):
            print(key)
            print(list(value))


def getcampos(func):
   
    @wraps(func)
    @current_app.before_request
    def decorated_function(*args, **kwargs):
        request_data = request.get_json()

        origem = request_data['origem']
        destino = request_data['destino']
        altura = request_data['altura']
        largura = request_data['largura']
        comprimento = request_data['comprimento']
        peso = request_data['peso']
        valor = request_data['valor']
        
        items = {
            "Origem":origem,
            "Destino":destino,
            "altura":altura,
            "Largura":largura,
            "comprimento":comprimento,
            "peso":peso,
            "valor":valor
            
            }
        
        #verifica_maiorquantidade()
     

        return jsonify({"Frete":items})
        
    return decorated_function


frete_bp = Blueprint("api",__name__)

api = Api(current_app)

api_model = api.model('Produtos',{'referenciasku':fields.String,
 'id':fields.Integer,'quantidade':fields.Float, 'cep':fields.String})


@api.route('/api/v1/fretes/all')
class ExibeFretes(Resource):
    #@api.expect(api_model, envelope='Produtos')
    def get(self):
        prods = ProdutosSchema(many=True)
        produtos = Produtos.query.all()
        return (prods.dump(produtos)), 200


@getcampos
@api.route('/api/v1/fretes/add')
class AdicionaFrete(Resource):
  
    def post(self):
        request_data = request.get_json()
        
      
      
        return {"username":request_data}, 201
   


class RetornaUnitario(Resource):pass


register_handlers(current_app)
