class FillingSphere:
    """Represents a theoretical 'negative' of a binding pocket. This concept can be used
    to predict the VERY VERY rough structure of a potential API (active pharmaceutical ingredient)
    which could be used to target the binding pocket of the protein."""

    def __init__(self, snapshot, c_or_o_value, atom_type, pocket_id, pos_x, pos_y, pos_z, occupancy,
                 temperature_factor):
        self.snapshot = snapshot
        self.c_or_o_value = c_or_o_value
        self.atom_type = atom_type
        self.pocket_id = pocket_id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.occupancy = occupancy
        self.temperature_factor = temperature_factor
