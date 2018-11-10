# python standard
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# third-party
from flask_script import Manager, Server
from flask_migrate import MigrateCommand

# locals
from dynamic import create_app

config_name = os.getenv('FLASK_CONFIG') or "development"
app = create_app(config_name)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(
    use_debugger = True,
    use_reloader = True,
    host = os.getenv('IP', '0.0.0.0'),
    port = int(os.getenv('PORT', 5000))
))

if __name__ == '__main__':
    manager.run()