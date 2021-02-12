import logging.config
import os

from flask import Flask, Blueprint

from api.restplus_definition import api
from constants import keys, config
from database import db

app = Flask(__name__)

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "../logging.conf"))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(app: Flask):
    if config.FLASK_DEBUG:
        server_name, database_uri = config.FLASK_SERVER_URL_DEBUG, config.SQLALCHEMY_DATABASE_URI_DEBUG
    else:
        server_name, database_uri = config.FLASK_SERVER_URL, config.SQLALCHEMY_DATABASE_URI

    app.config[keys.SERVER_NAME] = server_name
    app.config[keys.SQLALCHEMY_DATABASE_URI] = database_uri
    app.config[keys.SQLALCHEMY_TRACK_MODIFICATIONS] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config[keys.SWAGGER_UI_DOC_EXPANSION] = config.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    app.config[keys.RESTPLUS_VALIDATE] = config.RESTPLUS_VALIDATE
    app.config[keys.RESTPLUS_MASK_SWAGGER] = config.RESTPLUS_MASK_SWAGGER
    app.config[keys.ERROR_404_HELP] = config.RESTPLUS_ERROR_404_HELP


def init_app(app: Flask):
    configure_app(app)

    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api.init_app(blueprint)
    api.add_namespace()  # TODO: fill with namesapce
    app.register_blueprint(blueprint)

    db.init_app(app)


if __name__ == '__main__':
    init_app(app)
    log.info(f"Server started at http://{app.config[keys.SERVER_NAME]}/api/")
    app.run(debug=config.FLASK_DEBUG)
