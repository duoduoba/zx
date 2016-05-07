# coding：utf-8
import logging
from logging.handlers import TimedRotatingFileHandler
# from zx.settings import BASE_DIR


logger = logging.getLogger('jizhang')
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
fh = logging.FileHandler('jizhang.log')
fh.setLevel(logging.WARNING)
# rfh = TimedRotatingFileHandler('t_jizhang','S', 1, 10)
# rfh.suffix = '%Y-%m-%d.log'
# rfh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(levelname)s [FILE:%(filename)s LINE:%(lineno)s] %(message)s')
sh.setFormatter(formatter)
fh.setFormatter(formatter)
# rfh.setFormatter(formatter)
# logger.addHandler(rfh)
logger.addHandler(sh)
logger.addHandler(fh)