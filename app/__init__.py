from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import uri_database, secret_key
#Factory
def create_app():
    """Declare APP e registra blueprints"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri_database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = secret_key  #Token JWT


    #instancia APP/SqlAlchemy/Marshmallow
    from .extensions import db, ma, jwt
    db.init_app(app)
    ma = ma.init_app(app)
    jwt.init_app(app)
   
    with app.app_context():
        """Não mover esses imports para cima pois podem causar importação circular"""
        from .fretes.frete_produto import frete_bp
        from .admin.Admin import admin_bp
 
        app.register_blueprint(admin_bp)
        app.register_blueprint(frete_bp)
        
       

    return app
