import time
import util.date_time as date_time
from util.constants import *


INFO_FILE = LOG_DIR + 'info.log'
ERROR_FILE = LOG_DIR + 'error.log'


def info(message):
    log = f'INFO - {date_time.get_time()} - {message}'
    print(log)
    persist_log(log, INFO_FILE)


def warning(message):
    print(f'WARNING - {date_time.get_time()} - {message}')


def error(message):
    log = f'ERROR - {date_time.get_time()} - {message}'
    print(log)
    persist_log(log, ERROR_FILE)


def intro():
    print('''FPOCKET DATA READER\n''')
    time.sleep(1)
    print('''    As a first step you can define the snapshot interval which you would like to process.
    For larger input files it is advised to split the task into smaller subprocesses to reduce the likelihood
    of unexpected errors such as electric network or other types of hardware malfunctions.\n''')
    time.sleep(5)


def prepare():
    print('''\n    Now FPOCKET DATA READER will hunt pockets for you and process data conversion.
    All pocket and atom data will be persisted into the configured database.\n''')
    time.sleep(3)
    print('''    Preparing to read data...\n''')
    time.sleep(3)
    print('''    The process may take several hours depending on the input file size and the provided parameters.
    Please do not turn off the computer or interrupt the process.
    During reading FPOCKET DATA READER will continuously inform you about the progress. The printed logs are saved into
    the corresponding file of the logs directory for later investigation.
    Have patience my friend!\n''')
    time.sleep(10)


def clear_logs():
    open(INFO_FILE, 'w').close()
    open(ERROR_FILE, 'w').close()


def persist_log(log, file):
    with open(file, "a") as log_file:
        log_file.write(log + "\n")
    log_file.close()
