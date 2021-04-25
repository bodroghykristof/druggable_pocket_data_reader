# CONFIGURABLE INPUT PARAMETERS
RESOURCE_PREFIX = "resources/sample_data/"
LOG_DIR = "logs/"

# READ-ONLY INPUT PARAMETERS - PLEASE DO NOT CHANGE THEM!
INPUT_FILE_EXTENSION = ".pdb"
OUTPUT_ENDING = "_out"
INFO_FILE_ENDING = "_info.txt"
POCKETS_DIR_NAME = "pockets/"
POCKET_PDB_ENDING = "_atm.pdb"
POCKET_PQR_ENDING = "_vert.pqr"


def get_working_directory(snapshot):
    return RESOURCE_PREFIX + "snapshot_" + str(snapshot) + OUTPUT_ENDING + "/"


def get_input_pdb_filename(snapshot):
    return RESOURCE_PREFIX + "snapshot_" + str(snapshot) + INPUT_FILE_EXTENSION


def get_output_pdb_filename(snapshot):
    return get_working_directory(snapshot) + "snapshot_" + str(snapshot) + OUTPUT_ENDING + INPUT_FILE_EXTENSION


def get_info_file_name(snapshot):
    return get_working_directory(snapshot) + "snapshot_" + str(snapshot) + INFO_FILE_ENDING


def get_pocket_pdb_file_name(snapshot, pocket):
    return get_working_directory(snapshot) + POCKETS_DIR_NAME + "pocket" + str(pocket) + POCKET_PDB_ENDING


def get_pocket_pqr_file_name(snapshot, pocket):
    return get_working_directory(snapshot) + POCKETS_DIR_NAME + "pocket" + str(pocket) + POCKET_PQR_ENDING
