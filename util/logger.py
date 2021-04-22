import time
import util.date_time as date_time

INFO_FILE = 'logs/info.log'
ERROR_FILE = 'logs/error.log'


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
    print('''Preparing to read data...''')
    time.sleep(1)
    print('''The process may take several hours depending on the input file size.
    Please do not turn off the computer or interrupt the process
    During reading FPOCKET DATA READER will continuously inform you about the progress
    Have patience my friend!''')
    time.sleep(5)


def clear_logs():
    open(INFO_FILE, 'w').close()
    open(ERROR_FILE, 'w').close()


def persist_log(log, file):
    with open(file, "a") as log_file:
        log_file.write(log + "\n")
    log_file.close()
