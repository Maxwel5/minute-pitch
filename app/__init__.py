from flask import Flask
from config import Config
from flask_login import login_manager,LoginManager
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy(app)
mail = Mail()
photos = UploadSet('photos',IMAGES)
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"
def create_app():
    app.config.from_object(Config)
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    return app