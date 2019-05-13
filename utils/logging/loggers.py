import logging
from logging.handlers import RotatingFileHandler


def create_rotating_log(path):
    logger = logging.getLogger("[BESTCOM]")
    logger.setLevel(logging.INFO)
 
    handler = RotatingFileHandler(path, maxBytes=1024*1024*3, backupCount=1)
    
    format = """%(levelname) -10s %(asctime)s %(processName) -35s %(name) -35s %(funcName) -30s %(lineno)d: %(message)s"""
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)
 
    logger.addHandler(handler)
    return logger
