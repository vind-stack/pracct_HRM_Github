import inspect
import logging

class LogGen():

    @staticmethod
    def logGen():
        format = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")

        fileHandler = logging.FileHandler(".\\Logs\\hrm_logs.log")
        fileHandler.setFormatter(format)

        loggername = inspect.stack()[1][3]

        logger = logging.getLogger(loggername)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
