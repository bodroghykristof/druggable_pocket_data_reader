from sys_sql_io import file_splitter
import util.logger as logger
import engine
from queries import sql_reader


def main():
    processed_snapshots = sql_reader.processed_snapshots()
    # logger.intro()
    first, last, step = engine.ask_for_parameters()
    atoms_are_read = sql_reader.atoms_exist_in_table()
    input_file = engine.ask_for_input_file()
    # logger.prepare()
    # logger.clear_logs()
    last_pocket_index = file_splitter.split_input_file(input_file, first, last, step)

    if not atoms_are_read:
        atoms = engine.read_atoms(first)
        engine.write_atoms(atoms)
    else:
        logger.info(f'Atoms have already been written to database, skipping reading atoms phase')

    for snapshot in range(first, last_pocket_index + 1, step):

        if snapshot in processed_snapshots:
            logger.info(f'Snapshot {snapshot} has already been processed. Skipping...')
            continue

        logger.info(f'Preparing to process snapshot {snapshot}')
        engine.hunt_pockets(snapshot)

        atom_positions = engine.read_atom_positions(snapshot)
        engine.write_atom_positions(snapshot, atom_positions)
        pockets = engine.read_pockets(snapshot)

        pocket_index = 1
        for pocket in pockets:
            pocket_atoms = engine.read_pocket_atoms(snapshot, pocket_index, pocket)
            pocket_id = engine.write_pockets(snapshot, pocket_index, pocket)
            filling_spheres = engine.read_filling_sphere(snapshot, pocket_id, pocket_index)
            engine.write_pocket_atoms(snapshot, pocket_atoms, pocket_id)
            engine.write_filling_spheres(snapshot, filling_spheres, pocket_id)
            pocket_index += 1


if __name__ == '__main__':
    main()
