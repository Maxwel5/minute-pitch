from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from app import create_app, db
from app.models import User

app=create_app()
manager =  Manager(app)
migrate = Migrate(app,db)
manager.add_command('runserver',Server(use_debugger=True))
manager.add_command('db',MigrateCommand)

if __name__=="__main__":
    manager.run()