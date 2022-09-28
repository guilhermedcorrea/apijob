from flask import Blueprint
from flask_admin import Admin
from flask import current_app
from datetime import datetime
from flask_admin.base import BaseView, expose
from flask_admin.menu import MenuLink
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy


admin_bp = Blueprint('adminuser', __name__)

admin = Admin(current_app, name='KABUM', template_mode='bootstrap3')

current_app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True



from ..extensions import db
from ..models.models import Produtos, MarcaProduto, CotacaoFrete, Usuarios



class ProdutosView(ModelView):

    can_set_page_size = True
    page_size = 15
    create_modal = True
    column_sortable_list = ('idproduto',('Produtos', Produtos.idproduto))
    column_display_pk = True
    column_searchable_list = ['idproduto', 'skuproduto', 'nomeproduto', 'bitativo']
    column_list = ['idproduto', 'skuproduto', 'nomeproduto', 'peso', 'bitativo']

    column_filters = ['skuproduto']
    can_create = True
    can_edit = True
    Can_delete = True
    can_export = True
    column_default_sort = 'idproduto'
    column_details_list = ['idproduto', 'skuproduto', 'nomeproduto', 'peso', 'bitativo','dataalterado']
    column_filters = ['skuproduto', 'idproduto', 'bitativo', 'peso']

    column_display_all_relations = True



class MarcaProdutoView(ModelView):
    can_set_page_size = True
    page_size = 15
    create_modal = True
    column_sortable_list = ('idmarca',('MarcaProduto', MarcaProduto.idmarca))
    column_display_pk = True
    column_searchable_list = ['idmarca', 'marca', 'bitativo', 'datacadastro','bitativo']
    column_list = ['idmarca', 'marca', 'bitativo', 'datacadastro','bitativo']

    column_filters = ['idmarca','marca','bitativo']
    can_create = True
    can_edit = True
    Can_delete = True
    can_export = True
    column_default_sort = 'idmarca'
    column_details_list = ['idmarca', 'marca', 'bitativo', 'datacadastro','bitativo']
    column_filters = ['idmarca', 'marca', 'bitativo', 'datacadastro','bitativo']

    column_display_all_relations = True
    

class CotacaoFreteView(ModelView):
    can_set_page_size = True
    page_size = 15
    create_modal = True
    column_sortable_list = ('idfrete',('CotacaoFrete', CotacaoFrete.idfrete))
    column_display_pk = True
    column_searchable_list = ['idfrete', 'transportadora']
    column_list = ['idfrete', 'transportadora', 'idmarca', 'idproduto','cep','categoriafrete',
                   'valorFrete','prazo','transportadora','dacotacao']

    column_filters = ['idmarca','idproduto','categoriafrete']
    can_create = True
    can_edit = True
    Can_delete = True
    can_export = True
    column_default_sort = 'idfrete'
    column_details_list = ['idfrete', 'transportadora', 'idmarca', 'idproduto','cep','categoriafrete',
                   'valorFrete','prazo','transportadora','dacotacao']
    column_filters = ['idfrete', 'transportadora', 'idmarca', 'idproduto','cep','categoriafrete',
                   'valorFrete','prazo','transportadora','dacotacao']

    column_display_all_relations = True
    


admin.add_view(CotacaoFreteView(CotacaoFrete, db.session))
admin.add_view(ProdutosView(Produtos, db.session))

admin.add_view(MarcaProdutoView(MarcaProduto, db.session))
