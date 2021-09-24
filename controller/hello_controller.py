from flask import Blueprint
from usecase.interactor.hello_usecase import Hello
from utilities.logger.logging import log, get_logger

logger = get_logger()

blueprint = Blueprint('hello_controller', __name__)


@log(logger)
@blueprint.route('/', methods=['GET', 'POST'])
def main_api_controller():
    try:
        hello = Hello()
        text = hello.hello()
        logger.info(text)
    except Exception as e:
        logger.error(e)
        return e
    return text
