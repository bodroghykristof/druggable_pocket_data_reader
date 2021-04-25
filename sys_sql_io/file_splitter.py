import util.logger as logger
import os

INPUT_FILE = "resources/sample_data/first_ten.pdb"


def split_input_file(start=1, end=0):
    count = 1
    destination_file = None

    with open(INPUT_FILE, "r") as input_file:
        line = input_file.readline()

        while line:

            line = input_file.readline()

            if count >= start and (end == 0 or count <= end):
                if not destination_file:
                    destination_file = open(f'resources/sample_data/snapshot_{count}.pdb', "a+")
                destination_file.write(line)
                if line.startswith("END"):
                    destination_file.close()
                    destination_file = None
                    logger.info(f'File ready: {count}')
                    count += 1
                    if end != 0 and count > end:
                        break

            else:
                if line.startswith("END"):
                    count += 1

            # if line.startswith("END"):
            #     if start <= count:
            #         destination_file.close()
            #     count += 1
            #     if count >= start and (end == 0 or count <= end):
            #         logger.info(f'File ready: {count - 1}')
            #         destination_file = open(f'resources/sample_data/snapshot_{count}.pdb', "a+")
            #     if count > end != 0:
            #         break
        if destination_file:
            destination_file.close()
        input_file.close()
        last_file = f'resources/sample_data/snapshot_{count}.pdb'
        if os.path.isfile(last_file):
            os.remove(last_file)
