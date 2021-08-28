class PocketAtom:
    """Represents a pocket and an atom residing within it. This entity corresponds
    to a record of a cross-reference table joining together pockets with their residing atoms."""

    def __init__(self, pocket_id, atom_id):
        self.pocket_id = pocket_id
        self.atom_id = atom_id
