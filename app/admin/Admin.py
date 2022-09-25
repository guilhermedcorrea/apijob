from flask import Blueprint
from flask_admin import Admin
from flask import current_app
from datetime import datetime
from flask_admin.base import BaseView, expose
from flask_admin.menu import MenuLink
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView

admin_bp = Blueprint('adminuser', __name__)

admin = Admin(current_app, name='microblog', template_mode='bootstrap3')
current_app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True

from ..extensions import db

from models.models import Produtos, MarcaProduto, CotacaoFrete, Usuarios, LogUsuario


class ProdutosView(ModelView): pass

class MarcaProdutoView(ModelView): pass

class CotacaoFreteView(ModelView): pass

class UsuariosView(ModelView): pass

class LogUsuarioView(ModelView): pass


admin.add_view(ProdutosView(
    Produtos, db.session, category="Produtos"))

admin.add_view(MarcaProdutoView(
    MarcaProduto, db.session, category="Produtos"))

admin.add_view(CotacaoFrete(
    CotacaoFreteView, db.session, category="Produtos"))

admin.add_view(UsuariosView(
    Usuarios, db.session, category="Produtos"))

admin.add_sub_category(name="Produtos", parent_name="Produtos")

admin.add_view(LogUsuarioView(
    LogUsuario, db.session, category="Usuario"))


admin.add_sub_category(name="Usuarios", parent_name="Usuarios")