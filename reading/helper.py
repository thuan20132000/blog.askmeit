

import local_config
import datetime
import os
import inspect
import logging

def log_message(message):
    log = open(local_config.PATH_WORK_DIR+"/logs/logs.txt", 'a')
    # message_parse =
    func = inspect.currentframe().f_back.f_code
    co_name = func.co_name
    f_name = func.co_filename
    co_line = func.co_firstlineno

    log.write(f'\n {str(datetime.datetime.now())} : {message} at {co_line} - {co_name} - {f_name}')
