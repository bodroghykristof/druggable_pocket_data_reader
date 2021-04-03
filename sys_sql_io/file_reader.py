# READ VARIOUS FILE TYPES INTO MODEL OBJECTS
from model.atom import Atom
from model.atom_position import AtomPosition
from model.pocket import Pocket
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


def read_from_info_txt_file(path, snapshot):
    pockets = []
    pocket_lines = []
    info_file = open(path, "r")
    while True:
        line = info_file.readline()
        if not line:
            break
        if line.startswith("Pocket"):
            pocket = create_pocket_from_lines(pocket_lines, snapshot)
            if pocket is not None:
                pockets.append(pocket)
            pocket_lines.clear()
        else:
            pocket_lines.append(line)
    info_file.close()
    return pockets


def create_pocket_from_lines(lines, snapshot):
    if len(lines) == 0:
        return None
    pocket = Pocket()
    pocket.snapshot = snapshot
    pocket.total_sasa = get_value_for_pocket_line(lines[3])
    pocket.polar_sasa = get_value_for_pocket_line(lines[4])
    pocket.apolar_sasa = get_value_for_pocket_line(lines[5])
    pocket.volume = get_value_for_pocket_line(lines[6])
    pocket.polar_atom_proportion = get_value_for_pocket_line(lines[15])
    pocket.alpha_sphere_density = get_value_for_pocket_line(lines[16])
    pocket.center_alpha_sphere_max_dist = get_value_for_pocket_line(lines[17])
    pocket.flexibility = get_value_for_pocket_line(lines[18])
    return pocket


def get_value_for_pocket_line(line):
    return line.split()[-1]
