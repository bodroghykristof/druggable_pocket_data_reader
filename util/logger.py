"""This file is a general logger used to persist log messages in the filesystem."""

import time
import util.date_time as date_time
from util.constants import *

INFO_FILE = LOG_DIR + 'info.log'
"""Destination file for log with 'info' severity"""

ERROR_FILE = LOG_DIR + 'error.log'
"""Destination file for log with 'error' severity"""


def info(message):
    """Log messages with 'info' severity and also display them on the console
    in a real-time manner"""

    log = f'INFO - {date_time.get_time()} - {message}'
    print(log)
    persist_log(log, INFO_FILE)


def warning(message):
    """Display a warning on the console without persisting"""

    print(f'WARNING - {date_time.get_time()} - {message}')


def error(message):
    """Log messages with 'error' severity and also display them on the console
    in a real-time manner"""

    log = f'ERROR - {date_time.get_time()} - {message}'
    print(log)
    persist_log(log, ERROR_FILE)


def intro():
    """Display a short introduction messages before running the program"""

    print('''FPOCKET DATA READER\n''')
    time.sleep(1)
    print('''    As a first step you can define the snapshot interval which you would like to process.
    For larger input files it is advised to split the task into smaller subprocesses to reduce the likelihood
    of unexpected errors such as electric network or other types of hardware malfunctions.\n''')
    time.sleep(5)


def prepare():
    """Inform the user about some basic details of the upcoming process."""

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
    """Empty all log files"""

    open(INFO_FILE, 'w').close()
    open(ERROR_FILE, 'w').close()


def persist_log(log, file):
    """Append the given log message to the content of the corresponding log file"""

    with open(file, "a") as log_file:
        log_file.write(log + "\n")
    log_file.close()
