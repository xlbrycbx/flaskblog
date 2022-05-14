from flask import Flask

import settings
from exts import db


def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config.from_object(settings)
    app.register_blueprint()
    db.init_app(app)
    return app