from flask import Flask
import settings


from apps.user.views import user_bp1
from exts import db, bootstrap


def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config.from_object(settings.DevelopConfig)

    app.register_blueprint(user_bp1)


    db.init_app(app=app)
    bootstrap.init_app(app=app)
    return app