ALTER TABLE IF EXISTS ONLY public.atom DROP CONSTRAINT IF EXISTS pk_atom_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.atom_position DROP CONSTRAINT IF EXISTS pk_atom_position_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.atom_position DROP CONSTRAINT IF EXISTS fk_atom_position_atom_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.pocket DROP CONSTRAINT IF EXISTS pk_pocket_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.pocket_atom DROP CONSTRAINT IF EXISTS fk_pocket_atom_pocket_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.pocket_atom DROP CONSTRAINT IF EXISTS fk_pocket_atom_atom_id CASCADE;

DROP TABLE IF EXISTS public.atom_position;
CREATE TABLE atom_position (
    id serial primary key,
    snapshot integer,
    atom_id integer,
    pos_x decimal,
    pos_y decimal,
    pos_z decimal
);


DROP TABLE IF EXISTS public.atom;
CREATE TABLE atom (
    id serial primary key,
    atom_type varchar(10),
    amino_acid_name varchar(3),
    protein_id varchar(1),
    amino_acid_id integer,
    occupancy decimal,
    temperature_factor decimal,
    atom_symbol varchar(3)
);

ALTER TABLE ONLY atom_position
    ADD CONSTRAINT fk_atom_position_atom_id FOREIGN KEY (atom_id) REFERENCES atom(id) ON DELETE CASCADE;


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

DROP TABLE IF EXISTS public.pocket_atom;
CREATE TABLE pocket_atom (
    id serial primary key,
    pocket_id integer,
    atom_id integer
);

ALTER TABLE ONLY pocket_atom
    ADD CONSTRAINT fk_pocket_atom_pocket_id FOREIGN KEY (pocket_id) REFERENCES pocket(id) ON DELETE CASCADE;

ALTER TABLE ONLY pocket_atom
    ADD CONSTRAINT fk_pocket_atom_atom_id FOREIGN KEY (atom_id) REFERENCES atom(id) ON DELETE CASCADE;