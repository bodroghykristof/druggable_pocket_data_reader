from file_system_io import file_splitter
import util.logger as logger
from service.data_reader import data_reader_engine
from sql.data_reader import sql_reader


def read_data():
    """This function is the entry point of data_reader module of the application. It splits the original
    huge input file into smaller segments, runs fpocket on them and analyses the resulting output files.
    It parses the content of the files into model objects and saves these objects into SQL tables."""

    processed_snapshots = sql_reader.processed_snapshots()
    logger.intro()
    first, last, step = data_reader_engine.ask_for_parameters()
    atoms_are_read = sql_reader.atoms_exist_in_table()
    input_file = data_reader_engine.ask_for_input_file()
    logger.prepare()
    logger.clear_logs()
    last_pocket_index = file_splitter.split_input_file(input_file, first, last, step)

    if not atoms_are_read:
        atoms = data_reader_engine.read_atoms(first)
        data_reader_engine.write_atoms(atoms)
    else:
        logger.info(f'Atoms have already been written to database, skipping reading atoms phase')

    for snapshot in range(first, last_pocket_index + 1, step):

        if snapshot in processed_snapshots:
            logger.info(f'Snapshot {snapshot} has already been processed. Skipping...')
            continue

        logger.info(f'Preparing to process snapshot {snapshot}')
        data_reader_engine.hunt_pockets(snapshot)

        atom_positions = data_reader_engine.read_atom_positions(snapshot)
        data_reader_engine.write_atom_positions(snapshot, atom_positions)
        pockets = data_reader_engine.read_pockets(snapshot)

        pocket_index = 1
        for pocket in pockets:
            pocket_atoms = data_reader_engine.read_pocket_atoms(snapshot, pocket_index, pocket)
            pocket_id = data_reader_engine.write_pockets(snapshot, pocket_index, pocket)
            filling_spheres = data_reader_engine.read_filling_sphere(snapshot, pocket_id, pocket_index)
            data_reader_engine.write_pocket_atoms(snapshot, pocket_atoms, pocket_id)
            data_reader_engine.write_filling_spheres(snapshot, filling_spheres, pocket_id)
            pocket_index += 1
