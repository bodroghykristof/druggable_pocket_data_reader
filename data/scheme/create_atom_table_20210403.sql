ALTER TABLE IF EXISTS ONLY public.atom DROP CONSTRAINT IF EXISTS pk_atom_id CASCADE;

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