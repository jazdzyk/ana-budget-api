import logging
import traceback

from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound

from constants import keys, config

log = logging.getLogger(__name__)
api = Api(version="1.0", title="Ana-Budget API",
          description="A REST API for Ana-Budget - a web app which serves as the analytics tool for personal budget.")


@api.errorhandler
def default_error_handler(err):
    message = "An unhandled exception occurred."
    log.exception(message)

    if not config.FLASK_DEBUG:
        return {keys.MESSAGE: message}, 500


@api.errorhandler(NoResultFound)
def db_not_found_error_handler(err: NoResultFound):
    """No results were found in the database."""
    log.warning(traceback.format_exc())
    return {keys.MESSAGE: "A database result was required but none was found."}, 404
