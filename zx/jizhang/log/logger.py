# coding：utf-8
import logging
# from zx.settings import BASE_DIR


logger = logging.getLogger('jizhang')
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
fh = logging.FileHandler('jizhang.log')
fh.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s %(levelname)s [FILE:%(filename)s LINE:%(lineno)s] %(message)s')
sh.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(sh)
logger.addHandler(fh)

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# sh = logging.StreamHandler()
# sh.setLevel(logging.DEBUG)
#
# log_name = BASE_DIR + '\jizhang\log\\'  +  'jizhang.log'
# print('log_name', log_name)
# fh = logging.FileHandler(log_name)
# fh.setLevel(logging.WARNING)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# sh.setFormatter(formatter)
# fh.setFormatter(formatter)
# logger.addHandler(sh)
# logger.addHandler(fh)
