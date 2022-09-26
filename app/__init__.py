from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import abort, jsonify
from config import uri_database, secret_key


#Handlers
def register_handlers(app):
    if app.config.get('DEBUG') is True:
        app.logger.debug('Skipping error handlers in Debug mode')
        return

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"Error":"not found error"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"Error":"internal error"}), 500

    @app.errorhandler(500)
    def ModuleNotFoundError(*args, **kwargs):
        return jsonify({"Error":"Server Error"}), 500

    @app.errorhandler(404)
    def page_not_found(*args, **kwargs):
        return jsonify({"Error":"EndPoint NotFound"}), 404
   
    @app.errorhandler(405)
    def method_not_allowed_page(*args, **kwargs):
  
        return jsonify({"Error":"Method not found"}), 405
        

#Factory
def create_app():
    """Declare APP e registra blueprints"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/Kabum'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = secret_key  #Token JWT

    #instancia APP/SqlAlchemy/Marshmallow
    from .extensions import db, ma, jwt, migrate
    db.init_app(app)
    ma = ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
   
    
    with app.app_context():
        """Não mover esses imports para cima pois podem causar importação circular"""
        from .fretes.frete_produto import frete_bp
        from .admin.Admin import admin_bp
        register_handlers(app)
        app.register_blueprint(admin_bp)
        app.register_blueprint(frete_bp)
        

    return app
