"""This file serves the data_reader module of the application by performing logic to
read raw data from the filesystem into model objects residing in the memory."""

from model.atom import Atom
from model.atom_position import AtomPosition
from model.pocket import Pocket
from model.pocket_atom import PocketAtom
from model.filling_sphere import FillingSphere
from util.exceptions import AtomDataParseException

import traceback
import util.logger as logger


def read_from_pdb_pqr(path, action, snapshot=0, pocket_id=0):
    """This function processes an input PDB or PQR-file and generates an array of entities. These
    result entities can have different types based on the value of parameter 'action'. The
    possible object types are Atom, AtomPosition and FillingSphere correspondingly."""

    try:
        entities = []
        pdb_file = open(path, "r")
        while True:
            line = pdb_file.readline()
            if not line:
                break
            else:
                property_array = line.split()
                if property_array[0] == "ATOM":
                    entity = create_entity_from_pdb_pqr_line(property_array, action, snapshot, pocket_id)
                    entities.append(entity)
        pdb_file.close()
        return entities
    except:
        logger.error(traceback.format_exc())


def create_entity_from_pdb_pqr_line(property_array, action, snapshot, pocket_id):
    """This function serves as an adapter to fork the execution based on the value of
    parameter 'action' and perform different logic in order to obtain the desired entity."""

    if action == "ATOM":
        return create_atom_from_pdb_line(property_array)
    elif action == "POSITION":
        return create_atom_position_from_pdb_line(property_array, snapshot)
    elif action == "FILLING_SPHERE":
        return create_filling_sphere_from_pqr_line(property_array, snapshot, pocket_id)
    else:
        raise AtomDataParseException('''Action not supported - only atom, atom_position (PDB) and 
                                    filling sphere (PQR) can be extracted''')


def create_atom_from_pdb_line(property_array):
    """Creates and Atom entity from a single line of a PDB-file by mapping separated values of the line
    with properties of Atom class."""

    try:
        _id = property_array[1]
        atom_type = property_array[2]
        amino_acid_name = property_array[3]
        protein_id = property_array[4]
        amino_acid_id = property_array[5]
        atom_symbol = property_array[11]
        atom = Atom(_id, atom_type, amino_acid_name, protein_id, amino_acid_id, atom_symbol)
        return atom
    except IndexError:
        raise AtomDataParseException("Could not parse atom - the provided file is not valid PDB format")


def create_atom_position_from_pdb_line(property_array, snapshot):
    """Creates and AtomPosition entity from a single line of a PDB-file by mapping separated values of the line
    with properties of AtomPosition class."""

    try:
        atom_id = property_array[1]
        pos_x = property_array[6]
        pos_y = property_array[7]
        pos_z = property_array[8]
        occupancy = property_array[9]
        temperature_factor = property_array[10]
        atom_position = AtomPosition(snapshot, atom_id, pos_x, pos_y, pos_z, occupancy, temperature_factor)
        return atom_position
    except IndexError:
        raise AtomDataParseException("Could not parse atom position - the provided file is not valid PDB format")


def create_filling_sphere_from_pqr_line(property_array, snapshot, pocket_id):
    """Creates and FillingSphere entity from a single line of a PQR-file by mapping separated values of the line
    with properties of FillingSphere class."""

    try:
        c_or_o_value = property_array[2]
        atom_type = property_array[3]
        pos_x = property_array[5]
        pos_y = property_array[6]
        pos_z = property_array[7]
        occupancy = property_array[8]
        temperature_factor = property_array[9]
        filling_sphere = FillingSphere(snapshot, c_or_o_value, atom_type, pocket_id, pos_x, pos_y, pos_z,
                                       occupancy, temperature_factor)
        return filling_sphere
    except IndexError:
        raise AtomDataParseException("Could not parse atom position - the provided file is not valid PQR format")


def read_from_info_txt_file(path, snapshot):
    """This function reads a given TXT-file corresponding to a snapshot
    and generates an array of Pocket entities registered in that given snapshot."""

    try:
        pockets = []
        pocket_lines = []
        info_file = open(path, "r")
        while True:
            line = info_file.readline()
            if not line:
                pocket = create_pocket_from_lines(pocket_lines, snapshot)
                pockets.append(pocket)
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
    except:
        logger.error(traceback.format_exc())


def create_pocket_from_lines(lines, snapshot):
    """Creates and Pocket entity from different lines of a TXT-file by mapping values present in the lines
    with properties of Pocket class."""

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
    """Return the last word of a line separated by whitespace characters."""

    return line.split()[-1]


def read_from_pocket_pdb_file(path, pocket):
    """Return the last word of a line separated by whitespace characters."""

    try:
        pocket_properties = []
        atoms_in_pocket = []
        general_info_lines = True
        info_file = open(path, "r")
        while True:
            line = info_file.readline()
            if not line:
                break
            if line.startswith("HEADER"):
                if general_info_lines:
                    general_info_lines = set_general_info_lines_state_while_reading(line)
                else:
                    pocket_properties.append(line)
            elif line.startswith("ATOM"):
                atoms_in_pocket.append(line)
        info_file.close()
        enrich_pocket_data_with_new_properties(pocket, pocket_properties)
        return [PocketAtom(pocket.id_, int(atom.split()[1])) for atom in atoms_in_pocket]
    except:
        logger.error(traceback.format_exc())


def set_general_info_lines_state_while_reading(current_line):
    """Checks if the iteration over the lines of the file has reached the point from where Atoms are listed
    present in the given Pocket."""

    return not current_line.startswith("HEADER Information about the pocket")


def enrich_pocket_data_with_new_properties(pocket, pocket_properties):
    """Add more data for an already processed Pocket entity fetched from the PDB-file generated by fpocket."""

    pocket.score = get_value_for_pocket_line(pocket_properties[0])
    pocket.druggability_score = get_value_for_pocket_line(pocket_properties[1])
    pocket.alpha_spheres_no = get_value_for_pocket_line(pocket_properties[2])
    pocket.mean_local_hydrobhopic_density = get_value_for_pocket_line(pocket_properties[12])
    pocket.mean_alpha_sphere_radius = get_value_for_pocket_line(pocket_properties[3])
    pocket.mean_alpha_sphere_solvent_access = get_value_for_pocket_line(pocket_properties[4])
    pocket.hydrophobicity_score = get_value_for_pocket_line(pocket_properties[6])
    pocket.volume_score = get_value_for_pocket_line(pocket_properties[8])
    pocket.polarity_score = get_value_for_pocket_line(pocket_properties[7])
    pocket.charge_score = get_value_for_pocket_line(pocket_properties[11])
    pocket.mean_b_factor = get_value_for_pocket_line(pocket_properties[5])
    pocket.mean_local_hydrobhopic_density = get_value_for_pocket_line(pocket_properties[12])
    pocket.pocket_volume_monte_carlo = get_value_for_pocket_line(pocket_properties[9])
    pocket.pocket_volume_convex_hull = get_value_for_pocket_line(pocket_properties[10])
    pocket.apolar_alpha_sphere_no = get_value_for_pocket_line(pocket_properties[13])
