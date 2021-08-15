import inspect
import logging
from functools import wraps


class CustomFilter(logging.Filter):

    def filter(self, record):

        record.real_filename = getattr(record,
                                       'real_filename',
                                       record.filename)
        record.real_funcName = getattr(record,
                                       'real_funcName',
                                       record.funcName)
        record.real_lineno = getattr(record,
                                     'real_lineno',
                                     record.lineno)
        return True


def get_logger():
    log_format = '[%(asctime)s] %(levelname)s\t%(real_filename)s' \
                 ' - %(real_funcName)s:%(real_lineno)s -> %(message)s'
    logging.basicConfig(format=log_format, level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.addFilter(CustomFilter())
    return logger


def log(logger):

    def _decorator(func):

        # funcのメタデータを引き継ぐ
        @wraps(func)
        def wrapper(*args, **kwargs):

            func_name = func.__name__
            # loggerで使用するためにfuncに関する情報をdict化
            extra = {
                'real_filename': inspect.getfile(func),
                'real_funcName': func_name,
                'real_lineno': inspect.currentframe().f_back.f_lineno
            }

            logger.info(f'[START] {func_name}', extra=extra)

            try:
                # funcの実行
                return func(*args, **kwargs)
            except Exception as err:
                # funcのエラーハンドリング
                logging.error(err, exc_info=True, extra=extra)
                logging.error(f'[KILLED] {func_name}', extra=extra)
            else:
                logging.info(f'[END] {func_name}', extra=extra)

        return wrapper
    return _decorator
