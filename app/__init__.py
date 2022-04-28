from app.utils.decoder import object2ClassDecoder
import os, pathlib, yaml
from flask import Flask

CURRENT_DIR = pathlib.Path(__file__).parent
ROOT_DIR = CURRENT_DIR.parent

def create_app():
    app = Flask(__name__)

    env = os.environ.get('ENV')
    if env is None:
        env = 'dev'

    CONF_FILE = ROOT_DIR / f'app/config/{env}.yaml'

    with open(CONF_FILE, "rb") as fp:
        yamlconfig = yaml.load(fp, Loader=yaml.FullLoader)

    conf = object2ClassDecoder(yamlconfig, 'Config')

    app.config.from_object(conf)
    app_ctx = app.app_context()
    app_ctx.push()
    from app.manager.db import mysqlconn

    from app.view import view, user 
    app.register_blueprint(view, url_prefix='/')

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        mysqlconn().close()

    return app