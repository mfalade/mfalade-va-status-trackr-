import logging

log_file_name = 'app-log.log'
logging.basicConfig(filename=log_file_name, level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
logger = logging.getLogger(__name__)
