from flask import Flask
# from flask import config
from config import config_options
from flask_bootstrap import Bootstrap
from config import Config
from flask_login import login_manager,LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
import app

db = SQLAlchemy(app)
mail = Mail()
photos = UploadSet('photos',IMAGES)
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"
def create_app():
    app =  Flask(__name__)
    app.config.from_object(Config)
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
    return app