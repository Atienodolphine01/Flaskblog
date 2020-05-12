from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from config import Config,config_options
from flask_uploads import configure_uploads,UploadSet,IMAGES

profile_images = UploadSet('profileimages',IMAGES)
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.from_object(config_options[config_class])

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    configure_uploads(app,profile_images)

    from flaskblog.users.routes import users
    from flaskblog.post.routes import posts
    from flaskblog.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app