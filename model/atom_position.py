class AtomPosition:
    """Represents the position of an atom in the protein molecule at a given moment."""

    def __init__(self, snapshot, atom_id, pos_x, pos_y, pos_z, occupancy, temperature_factor):
        self.snapshot = snapshot
        self.atom_id = atom_id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.occupancy = occupancy
        self.temperature_factor = temperature_factor
