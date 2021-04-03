# WRITE MODEL OBJECTS INTO SQL TABLES
from sys_sql_io.sql_connection_handler import connection_handler


@connection_handler
def insert_atom_into_table(cursor, atom):
    insert_query = """
               INSERT INTO atom
                (id, atom_type, amino_acid_name, protein_id, amino_acid_id, occupancy, temperature_factor, atom_symbol)
                VALUES(%(id_)s, %(atom_type)s, %(amino_acid_name)s, %(protein_id)s, %(amino_acid_id)s, %(occupancy)s, 
                %(temperature_factor)s, %(atom_symbol)s)
                    """
    cursor.execute(insert_query,
                   vars(atom))
