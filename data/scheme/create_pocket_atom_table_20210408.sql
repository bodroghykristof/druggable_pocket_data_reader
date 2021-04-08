ALTER TABLE IF EXISTS ONLY public.pocket_atom DROP CONSTRAINT IF EXISTS fk_pocket_atom_pocket_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.pocket_atom DROP CONSTRAINT IF EXISTS fk_pocket_atom_atom_id CASCADE;

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