from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = '4636eb0877b0525464dc3a7645c50419'
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://dolphine:dolphine@localhost/flaskblog'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     bcrypt.init_app(app)
#     login_manager.init_app(app)

from flaskblog.users.routes import users
# from flaskblog.posts.routes import posts
from flaskblog.main.routes import main


app.register_blueprint(users)
# app.register_blueprint(posts)
app.register_blueprint(main)
