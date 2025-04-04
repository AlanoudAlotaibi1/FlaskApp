from flask import Flask 
import os
from flask_sqlalchemy import SQLAlchemy  
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate 
from flask_ckeditor import CKEditor
from flask_modals import Modal
from flask import Markup
from flask_mail import Mail
from appFlask.config import Config
from flask_admin import Admin


db = SQLAlchemy()

bcrypt= Bcrypt()
migrate = Migrate(db)
login_manager = LoginManager()
modal = Modal()
ckeditor = CKEditor()
login_manager.login_view = 'users.login' ## this for if we try to access page without user premession
login_manager.login_message_category = 'info'
mail = Mail()
admin = Admin()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from appFlask.adminbp.routes import MyAdminIndexView

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    modal.init_app(app)
    mail.init_app(app)
    admin.init_app(app, index_view=MyAdminIndexView())

    from appFlask.main.routes import main
    from appFlask.users.routes import users
    from appFlask.lessons.routes import lessons
    from appFlask.courses.routes import courses_bp
    from appFlask.errors.handlers import errors
    from appFlask.adminbp.routes import adminbp
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(lessons)
    app.register_blueprint(courses_bp)
    app.register_blueprint(errors)
    app.register_blueprint(adminbp)

    return app