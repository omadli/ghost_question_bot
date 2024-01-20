import logging
from aiogram import Dispatcher

from settings import DEBUG
from middlewares.logging_updates import LoggingUpdatesMiddleware


def set_logger(dp: Dispatcher):
    log_level = logging.INFO
    if DEBUG:
        log_level = logging.DEBUG
        # dp.update.middleware.register(LoggingUpdatesMiddleware())

    logging.basicConfig(
        format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
        level=log_level,
    )
