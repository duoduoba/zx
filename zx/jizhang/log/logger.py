# coding：utf-8
import logging
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
# from zx.settings import BASE_DIR


logger = logging.getLogger('zx')
MAXLOGSIZE = 5 * 1024 * 1024 #Bytes
BACKUPCOUNT = 4

level = logging.INFO
filename = 'zx.log'
formatter = logging.Formatter('%(asctime)s %(levelname)s [FILE:%(filename)s LINE:%(lineno)s] %(message)s')

file_handler = RotatingFileHandler(filename, mode='a', backupCount=BACKUPCOUNT, maxBytes=MAXLOGSIZE)
stream_handler = logging.StreamHandler()

stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)