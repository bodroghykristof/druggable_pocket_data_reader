# READ VARIOUS FILE TYPES INTO MODEL OBJECTS
from model.atom import Atom


def read_atoms_from_pdb(path):
    atoms = []
    pdb_file = open(path, 'r')
    while True:
        line = pdb_file.readline()
        if not line:
            break
        else:
            try:
                atom = create_atom_from_pdb_line(line)
                if atom is not None:
                    atoms.append(atom)
            except IndexError:
                print("Could not extract atom data from line")
    pdb_file.close()
    return atoms


def create_atom_from_pdb_line(line):
    property_array = line.split()
    if property_array[0] != "ATOM":
        return None
    _id = property_array[1]
    atom_type = property_array[2]
    amino_acid_name = property_array[3]
    protein_id = property_array[4]
    amino_acid_id = property_array[5]
    occupancy = property_array[9]
    temperature_factor = property_array[10]
    atom_symbol = property_array[11]
    atom = Atom(_id, atom_type, amino_acid_name, protein_id, amino_acid_id, occupancy, temperature_factor, atom_symbol)
    return atom
