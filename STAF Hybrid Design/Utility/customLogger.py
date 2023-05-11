import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
        LOG_FILENAME = datetime.now().strftime('.\\Log\\logfile_%d_%m_%Y_%H_%M_%S.log')
        file_handler = TimedRotatingFileHandler(LOG_FILENAME,when='D', interval=1, backupCount=3, encoding='utf-8', delay=False)
        stream_handler = logging.StreamHandler()
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        #logger.addHandler(stream_handler)
        return logger