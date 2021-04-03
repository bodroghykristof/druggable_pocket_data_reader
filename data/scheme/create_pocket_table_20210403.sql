ALTER TABLE IF EXISTS ONLY public.pocket DROP CONSTRAINT IF EXISTS pk_pocket_id CASCADE;

DROP TABLE IF EXISTS public.pocket;
CREATE TABLE pocket (
    id serial primary key,
    snapshot integer,
    score decimal,
    druggability_score decimal,
    alpha_spheres_no integer,
    total_sasa decimal,
    polar_sasa decimal,
    apolar_sasa decimal,
    volume decimal,
    mean_local_hydrobhopic_density decimal,
    mean_alpha_sphere_radius decimal,
    mean_alpha_sphere_solvent_access decimal,
    hydrophobicity_score decimal,
    volume_score decimal,
    polarity_score decimal,
    charge_score decimal,
    polar_atom_proportion decimal,
    alpha_sphere_density decimal,
    center_alpha_sphere_max_dist decimal,
    flexibility decimal,
    mean_b_factor decimal,
    pocket_volume_monte_carlo decimal,
    pocket_volume_convex_hull decimal,
    apolar_alpha_sphere_no integer
);