from flask import Blueprint, request, make_response, jsonify,current_app, Response, abort
from functools import wraps
from flask_restx import Resource, Api, fields

from ..models.models import Produtos, LogUsuario, CotacaoFrete, Usuarios
from ..models.serializer import ProdutosSchema, FretesSchema, UsuariosSchema 

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


def register_handlers(current_app):
    if current_app.config.get('DEBUG') is True:
        current_app.logger.debug('Skipping error handlers in Debug mode')
        return


    @current_app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"Error":"not found error"}), 404


    @current_app.errorhandler(500)
    def internal_error(error):
        return jsonify({"Error":"internal error"}), 500



frete_bp = Blueprint("api",__name__)

api = Api(current_app)

api_model = api.model('Produtos',{'referenciasku':fields.String,
 'id':fields.Integer,'quantidade':fields.Float, 'cep':fields.String})


from .calcula_frete import RetetornaCalculoFrete


@api.route('/api/v1/fretes/all')
class ExibeFretes(Resource):
    #@api.expect(api_model, envelope='Produtos')
    def get(self):
        prods = ProdutosSchema(many=True)
        produtos = Produtos.query.all()
        return (prods.dump(produtos)), 200


@api.route('/api/v1/fretes/add')
class AdicionaFrete(Resource):
    """
    cria frete e insere no banco
    """
    @api.expect(api_model, envelope='Produtos')
    def post(self):
        if request.method == 'POST':
            valor = request.json
            #produtos.append(api.payload)
 
            return {"ok":valor},201
        return {"valor":"invalido"}, 404


class RetornaUnitario(Resource):pass


register_handlers(current_app)
