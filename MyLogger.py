#the MyLogger class to implement a singleton pattern. The singleton pattern ensures that only one
# instance of the MyLogger class is created and shared across different modules that import it.

# TODO : add caller class name to each log message
# plusieurs façons d'obtenir cette variable dans le stack :

import logging
import inspect
from pathlib import Path

class MyLogger:
    _instance = None

    #a = street
    _previous_frame = inspect.currentframe().f_back
    _caller_filename = Path(_previous_frame.f_code.co_filename).name
    #print(caller_filename)
    def __new__(cls, filename=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logger = logging.getLogger(__name__)
            cls._instance.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s ; %(levelname)7s ; %(message)s')

            # Create console handler and set level to debug
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(formatter)
            cls._instance.logger.addHandler(ch)

            # Create file handler and set level to debug
            if filename:
                fh = logging.FileHandler(filename,encoding='utf-8')
                fh.setLevel(logging.DEBUG)
                fh.setFormatter(formatter)
                cls._instance.logger.addHandler(fh)

        return cls._instance

    def info(self, msg, *args, **kwargs):

        #logging the name of the module where the log call was made
        previous_frame = inspect.currentframe().f_back
        caller_module = Path(previous_frame.f_code.co_filename).name
        self.logger.info(f'{caller_module:<13} ; {msg}', *args, **kwargs)

    def warning(self, msg, *args, **kwargs):

        #logging the name of the module where the log call was made
        previous_frame = inspect.currentframe().f_back
        caller_module = Path(previous_frame.f_code.co_filename).name
        self.logger.warning(f'{caller_module:<13} ; {msg}', *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        #logging the name of the module where the log call was made
        previous_frame = inspect.currentframe().f_back
        caller_module = Path(previous_frame.f_code.co_filename).name
        self.logger.error(f'{caller_module:<13} ; {msg}', *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        #logging the name of the module where the log call was made
        previous_frame = inspect.currentframe().f_back
        caller_module = Path(previous_frame.f_code.co_filename).name
        self.logger.debug(f'{caller_module:<13} ; {msg}', *args, **kwargs)
