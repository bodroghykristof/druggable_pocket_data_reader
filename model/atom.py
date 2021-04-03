class Atom:

    def __init__(self, id_, atom_type, amino_acid_name, protein_id, amino_acid_id, occupancy,
                 temperature_factor, atom_symbol):
        self.id_ = id_
        self.atom_type = atom_type
        self.amino_acid_name = amino_acid_name
        self.protein_id = protein_id
        self.amino_acid_id = amino_acid_id
        self.occupancy = occupancy
        self.temperature_factor = temperature_factor
        self.atom_symbol = atom_symbol
