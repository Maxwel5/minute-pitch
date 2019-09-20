from app import create_app, db
from flask_script import Manager, Server
from app.models import User
from flask_migrate import Migrate, MigrateCommand

app = create_app('production')
manager =  Manager(app)
migrate = Migrate(app,db)
manager.add_command('runserver',Server(use_debugger=True))
manager.add_command('db',MigrateCommand)

@manager.shell
def add_shell_context():
    return {"db":db,"User":User,"app":app}

if __name__=="__main__":
    manager.run()