from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.user.models import User

from apps import create_app
from exts import db


app = create_app()
print(app.url_map)

manager = Manager(app=app)
migrate = Migrate(app=app,db=db,render_as_batch=True)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
