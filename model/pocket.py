class Pocket:

    def __init__(self, id_=0, snapshot=0, score=0, druggability_score=0, alpha_spheres_no=0, total_sasa=0, polar_sasa=0,
                 apolar_sasa=0, volume=0, mean_local_hydrobhopic_density=0, mean_alpha_sphere_radius=0,
                 mean_alpha_sphere_solvent_access=0, hydrophobicity_score=0, volume_score=0, polarity_score=0,
                 charge_score=0, polar_atom_proportion=0, alpha_sphere_density=0, center_alpha_sphere_max_dist=0,
                 flexibility=0, mean_b_factor=0, pocket_volume_monte_carlo=0, pocket_volume_convex_hull=0,
                 apolar_alpha_sphere_no=0):
        self.id_ = id_
        self.snapshot = snapshot
        self.score = score
        self.druggability_score = druggability_score
        self.alpha_spheres_no = alpha_spheres_no
        self.total_sasa = total_sasa
        self.polar_sasa = polar_sasa
        self.apolar_sasa = apolar_sasa
        self.volume = volume
        self.mean_local_hydrobhopic_density = mean_local_hydrobhopic_density
        self.mean_alpha_sphere_radius = mean_alpha_sphere_radius
        self.mean_alpha_sphere_solvent_access = mean_alpha_sphere_solvent_access
        self.hydrophobicity_score = hydrophobicity_score
        self.volume_score = volume_score
        self.polarity_score = polarity_score
        self.charge_score = charge_score
        self.polar_atom_proportion = polar_atom_proportion
        self.alpha_sphere_density = alpha_sphere_density
        self.center_alpha_sphere_max_dist = center_alpha_sphere_max_dist
        self.flexibility = flexibility
        self.mean_b_factor = mean_b_factor
        self.pocket_volume_monte_carlo = pocket_volume_monte_carlo
        self.pocket_volume_convex_hull = pocket_volume_convex_hull
        self.apolar_alpha_sphere_no = apolar_alpha_sphere_no
