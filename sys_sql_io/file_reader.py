# READ VARIOUS FILE TYPES INTO MODEL OBJECTS
from model.atom import Atom
from model.atom_position import AtomPosition
from util.exceptions import AtomDataParseException


def read_from_pdb(path, action, snapshot):
    entities = []
    pdb_file = open(path, "r")
    while True:
        line = pdb_file.readline()
        if not line:
            break
        else:
            property_array = line.split()
            if property_array[0] != "ATOM":
                raise AtomDataParseException("Line for atom or atom position should start with the phrase ATOM")
            entity = create_entity_from_pdb_line(property_array, action, snapshot)
            entities.append(entity)
    pdb_file.close()
    return entities


def create_entity_from_pdb_line(property_array, action, snapshot):
    if action == "ATOM":
        return create_atom_from_pdb_line(property_array)
    elif action == "POSITION":
        return create_atom_position_from_pdb_line(property_array, snapshot)
    else:
        raise AtomDataParseException("Invalid action - only atom or atom position can be extracted from PDB format")


def create_atom_from_pdb_line(property_array):
    try:
        _id = property_array[1]
        atom_type = property_array[2]
        amino_acid_name = property_array[3]
        protein_id = property_array[4]
        amino_acid_id = property_array[5]
        occupancy = property_array[9]
        temperature_factor = property_array[10]
        atom_symbol = property_array[11]
        atom = Atom(_id, atom_type, amino_acid_name, protein_id, amino_acid_id,
                    occupancy, temperature_factor, atom_symbol)
        return atom
    except IndexError:
        raise AtomDataParseException("Could not parse atom - the provided file is not valid PDB format")


def create_atom_position_from_pdb_line(property_array, snapshot):
    try:
        atom_id = property_array[1]
        pos_x = property_array[6]
        pos_y = property_array[7]
        pos_z = property_array[8]
        atom_position = AtomPosition(snapshot, atom_id, pos_x, pos_y, pos_z)
        return atom_position
    except IndexError:
        raise AtomDataParseException("Could not parse atom position - the provided file is not valid PDB format")
