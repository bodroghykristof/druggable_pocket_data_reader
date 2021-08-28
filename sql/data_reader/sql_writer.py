"""This file is responsible for persisting model objects residing in the memory into the SQL database serving
the data_reader module of the application."""

from util.sql_connection_handler import connection_handler

import traceback
import util.logger as logger


@connection_handler
def insert_atom_into_table(cursor, atom):
    """Insert a new Atom entity into table 'atom'."""

    insert_query = """
               INSERT INTO atom
                (id, atom_type, amino_acid_name, protein_id, amino_acid_id, atom_symbol)
                VALUES(%(id_)s, %(atom_type)s, %(amino_acid_name)s, %(protein_id)s, %(amino_acid_id)s, %(atom_symbol)s)
                    """
    try:
        cursor.execute(insert_query,
                       vars(atom))
    except:
        logger.error(traceback.format_exc())


@connection_handler
def insert_atom_position_into_table(cursor, atom_position):
    """Insert a new AtomPosition entity into table 'atom_position'."""

    insert_query = """
               INSERT INTO atom_position
                (id, snapshot, atom_id, pos_x, pos_y, pos_z, occupancy, temperature_factor)
                VALUES(DEFAULT, %(snapshot)s, %(atom_id)s, %(pos_x)s, %(pos_y)s, %(pos_z)s,
                %(occupancy)s, %(temperature_factor)s)
                    """
    try:
        cursor.execute(insert_query,
                       vars(atom_position))
    except:
        logger.error(traceback.format_exc())


@connection_handler
def insert_pocket_into_table(cursor, pocket):
    """Insert a new Pocket entity into table 'pocket'."""

    insert_query = """
               INSERT INTO pocket
                (id, snapshot, score, druggability_score, alpha_spheres_no, total_sasa, polar_sasa, apolar_sasa, 
                volume, mean_local_hydrobhopic_density, mean_alpha_sphere_radius, mean_alpha_sphere_solvent_access, 
                hydrophobicity_score, volume_score, polarity_score, charge_score, polar_atom_proportion, 
                alpha_sphere_density, center_alpha_sphere_max_dist, flexibility, mean_b_factor, 
                pocket_volume_monte_carlo, pocket_volume_convex_hull, apolar_alpha_sphere_no)
                VALUES(DEFAULT, %(snapshot)s, %(score)s, %(druggability_score)s, %(alpha_spheres_no)s, %(total_sasa)s, 
                %(polar_sasa)s, %(apolar_sasa)s, %(volume)s, %(mean_local_hydrobhopic_density)s,
                %(mean_alpha_sphere_radius)s, %(mean_alpha_sphere_solvent_access)s, %(hydrophobicity_score)s, 
                %(volume_score)s, %(polarity_score)s, %(charge_score)s, %(polar_atom_proportion)s, 
                %(alpha_sphere_density)s, %(center_alpha_sphere_max_dist)s, %(flexibility)s, %(mean_b_factor)s, 
                %(pocket_volume_monte_carlo)s, %(pocket_volume_convex_hull)s, %(apolar_alpha_sphere_no)s)
                RETURNING id
                    """
    try:
        cursor.execute(insert_query,
                       vars(pocket))
        return cursor.fetchone()['id']
    except:
        logger.error(traceback.format_exc())


@connection_handler
def insert_pocket_atom_into_table(cursor, pocket_atom):
    """Insert a new PocketAtom entity into table 'pocket_atom'."""

    insert_query = """
               INSERT INTO pocket_atom
                (id, pocket_id, atom_id)
                VALUES(DEFAULT, %(pocket_id)s, %(atom_id)s)
                    """
    try:
        cursor.execute(insert_query,
                       vars(pocket_atom))
    except:
        logger.error(traceback.format_exc())


@connection_handler
def insert_filling_sphere_into_table(cursor, filling_sphere):
    """Insert a new FillingSphere entity into table 'filling_sphere'."""

    insert_query = """
               INSERT INTO filling_sphere
                (id, snapshot, c_or_o_value, atom_type, pocket_id, pos_x, pos_y, pos_z, occupancy, temperature_factor)
                VALUES(DEFAULT, %(snapshot)s, %(c_or_o_value)s, %(atom_type)s, %(pocket_id)s, 
                %(pos_x)s, %(pos_y)s, %(pos_z)s, %(occupancy)s, %(temperature_factor)s)
                    """
    try:
        cursor.execute(insert_query,
                       vars(filling_sphere))
    except:
        logger.error(traceback.format_exc())
