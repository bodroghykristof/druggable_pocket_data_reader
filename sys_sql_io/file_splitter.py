import util.logger as logger
from util.constants import *
import os


def split_input_file(input_file, start=1, end=0, step=1):
    count = 1
    input_path = RESOURCE_PREFIX + input_file
    destination_file = None

    with open(input_path, "r") as input_file:
        line = input_file.readline()

        while line:

            line = input_file.readline()

            if count >= start and (end == 0 or count <= end) and (count - start) % step == 0:
                if not destination_file:
                    destination_file = open(get_input_pdb_filename(count), "a+")
                destination_file.write(line)
                if line.startswith("END"):
                    destination_file.close()
                    destination_file = None
                    logger.info(f'File ready: {count}')
                    count += 1
                    if end != 0 and count >= end:
                        break

            else:
                if line.startswith("END"):
                    count += 1

        if destination_file:
            destination_file.close()
        input_file.close()
        last_file = get_input_pdb_filename(count)
        if os.path.isfile(last_file):
            os.remove(last_file)
        return count - 1
