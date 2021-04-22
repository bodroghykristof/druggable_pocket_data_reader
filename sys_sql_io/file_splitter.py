import util.logger as logger

INPUT_FILE = "resources/sample_data/first_ten.pdb"


def split_input_file():
    count = 1
    with open(INPUT_FILE, "r") as input_file:
        destination_file = open(f'resources/sample_data/snapshot_{count}.pdb', "a+")
        line = input_file.readline()
        while line:
            line = input_file.readline()
            if line.startswith("END"):
                destination_file.close()
                logger.info(f'File ready: {count}')
                count += 1
                destination_file = open(f'resources/sample_data/snapshot_{count}.pdb', "a+")
            else:
                destination_file.write(line)
        destination_file.close()
        input_file.close()
