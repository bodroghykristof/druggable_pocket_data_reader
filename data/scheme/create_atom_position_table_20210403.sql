ALTER TABLE IF EXISTS ONLY public.atom_position DROP CONSTRAINT IF EXISTS pk_atom_position_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.atom_position DROP CONSTRAINT IF EXISTS fk_atom_position_atom_id CASCADE;

DROP TABLE IF EXISTS public.atom_position;
CREATE TABLE atom_position (
    id serial primary key,
    snapshot integer,
    atom_id integer,
    pos_x decimal,
    pos_y decimal,
    pos_z decimal
);

ALTER TABLE ONLY atom_position
    ADD CONSTRAINT fk_atom_position_atom_id FOREIGN KEY (atom_id) REFERENCES atom(id) ON DELETE CASCADE;