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
from ..models.models import Produtos

'''
class DefaultModelView(ModelView):
    page_size = 20

    column_display_pk = True
    column_searchable_list = ['idproduto']
    can_view_details = True

    column_list = []

    column_filters = []

    can_create = True
    can_edit = True
    can_export = True
'''

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
    #column_sortable_list = ('idproduto',(Produtos.idproduto))



admin.add_view(ProdutosView(Produtos, db.session))
