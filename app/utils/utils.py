# -*- coding: UTF-8 -*-

import logging
from logging.handlers import RotatingFileHandler


def logger(filename, logbasic):
    """
    logger method that outputs to both console and file
    loglevel : critical, error, warning, info or debug
    from Sam & Max : http://sametmax.com/ecrire-des-logs-en-python/
    """
    logger = logging.getLogger('activity')
    if not len(logger.handlers):
        logger.setLevel(logbasic)
        formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

        file_handler = RotatingFileHandler(filename,
                                           'a',
                                           1000000,
                                           1)
        file_handler.setLevel(logbasic)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        if logbasic == logging.DEBUG:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logbasic)
            logger.addHandler(stream_handler)
    return logger
