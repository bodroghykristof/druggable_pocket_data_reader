from util import logger
from util import user_input
from sys_sql_io import file_reader, sql_writer
from util.constants import *
import subprocess


def ask_for_parameters():
    while True:
        first_snapshot = user_input.ask_for_positive_numeric_input_with_default("First snapshot", 1)
        last_snapshot = user_input.ask_for_positive_numeric_input_with_default("Last snapshot", "last")
        if last_snapshot == "last":
            last_snapshot = 0
        step = user_input.ask_for_positive_numeric_input_with_default("Step", 1)
        if last_snapshot < first_snapshot and last_snapshot != 0:
            print("Last snapshot number should not be less than last")
            continue
        break
    return first_snapshot, last_snapshot, step


def ask_for_input_file():
    return user_input.ask_not_empty_simple_input("Please enter the name of the input file")


def hunt_pockets(snapshot):
    logger.info(f'Preparing to hunt pockets for snapshot {snapshot}')
    path = get_input_pdb_filename(snapshot)
    subprocess.run(["fpocket", "-f", path])
    logger.info(f'Pocket hunting has been finished for snapshot {snapshot}')


def read_atoms(first):
    logger.info("Reading atom base data from pdb file...")
    path = get_input_pdb_filename(first)
    atoms = file_reader.read_from_pdb_pqr(path, "ATOM")
    logger.info("Atoms have been successfully read")
    return atoms


def write_atoms(atoms):
    logger.info("Inserting atoms into database...")
    for atom in atoms:
        sql_writer.insert_atom_into_table(atom)
    logger.info("Atoms have been successfully inserted")


def read_atom_positions(snapshot):
    logger.info(f'Reading atom positions for snapshot {snapshot}...')
    path = get_output_pdb_filename(snapshot)
    atom_positions = file_reader.read_from_pdb_pqr(path, "POSITION", snapshot)
    logger.info(f'Atom positions have been successfully read for snapshot {snapshot}...')
    return atom_positions


def write_atom_positions(snapshot, atom_positions):
    logger.info(f'Writing atom positions to database for snapshot {snapshot}...')
    for position in atom_positions:
        sql_writer.insert_atom_position_into_table(position)
    logger.info(f'Atom positions have been successfully persisted for snapshot {snapshot}...')


def read_pockets(snapshot):
    logger.info(f'Reading pockets for snapshot {snapshot}...')
    path = get_info_file_name(snapshot)
    pockets = file_reader.read_from_info_txt_file(path, snapshot)
    logger.info(f'Pockets have been successfully read for snapshot {snapshot}...')
    return pockets


def read_pocket_atoms(snapshot, pocket_index, pocket):
    logger.info(f'Reading atoms in pocket number {pocket_index} for snapshot {snapshot}...')
    path = get_pocket_pdb_file_name(snapshot, pocket_index)
    pocket_atoms = file_reader.read_from_pocket_pdb_file(path, pocket)
    logger.info(f'Atoms have been successfully read in pocket number {pocket_index} for snapshot {snapshot}')
    return pocket_atoms


def write_pockets(snapshot, pocket_index, pocket):
    logger.info(f'Inserting pocket number {pocket_index} into database for snapshot {snapshot}...')
    pocket_id = sql_writer.insert_pocket_into_table(pocket)
    logger.info(f'Pocket number {pocket_index} have been successfully inserted into database for snapshot {snapshot}')
    logger.info(f'Generated ID for pocket: {pocket_id}')
    return pocket_id


def read_filling_sphere(snapshot, pocket_id, pocket_index):
    logger.info(f'Reading filling spheres for snapshot {snapshot}...')
    path = get_pocket_pqr_file_name(snapshot, pocket_index)
    filling_spheres = file_reader.read_from_pdb_pqr(path, "FILLING_SPHERE", snapshot, pocket_id)
    logger.info(f'Filling spheres haven been successfully persisted in snapshot {snapshot} (pocket ID: {pocket_id})')
    return filling_spheres


def write_pocket_atoms(snapshot, pocket_atoms, pocket_id):
    logger.info(f'Inserting pocket atoms for pocket with ID {pocket_id} in snapshot {snapshot} into database...')
    for pocket_atom in pocket_atoms:
        pocket_atom.pocket_id = pocket_id
        sql_writer.insert_pocket_atom_into_table(pocket_atom)
    logger.info(f'Pocket atoms haven been successfully persisted for pocket with ID {pocket_id} in snapshot {snapshot}')


def write_filling_spheres(snapshot, filling_spheres, pocket_id):
    logger.info(f'Writing filling spheres for pocket with ID {pocket_id} in snapshot {snapshot}...')
    for filling_sphere in filling_spheres:
        sql_writer.insert_filling_sphere_into_table(filling_sphere)
    logger.info(
        f'Filling spheres haven been successfully persisted for pocket with ID {pocket_id} in snapshot {snapshot}')