from flask import Blueprint, request, make_response, jsonify,current_app, Response, abort
from functools import wraps
from flask_restx import Resource, Api, fields

from ..models.models import Produtos, LogUsuario, CotacaoFrete, Usuarios
from ..models.serializer import ProdutosSchema, FretesSchema, UsuariosSchema 


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
