import time
import util.date_time as date_time


def info(message):
    print(f'INFO - {date_time.get_time()} - {message}')


def warning(message):
    print(f'WARNING - {date_time.get_time()} - {message}')


def error(message):
    print(f'ERROR - {date_time.get_time()} - {message}')


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

