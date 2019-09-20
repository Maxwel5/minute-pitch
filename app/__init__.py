from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from config import Config
from flask_login import login_manager,LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE

app =  Flask(__name__)
db = SQLAlchemy(app)
simple = SimpleMDE()
mail = Mail()
bootstrap = Bootstrap()
photos = UploadSet('photos',IMAGES)
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)
    configure_uploads(app,photos)

    return app