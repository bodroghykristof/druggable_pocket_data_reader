ALTER TABLE IF EXISTS ONLY public.filling_sphere DROP CONSTRAINT IF EXISTS fk_filling_sphere_pocket_id CASCADE;

DROP TABLE IF EXISTS public.filling_sphere;
CREATE TABLE filling_sphere (
    id serial primary key,
    snapshot integer,
    atom_type varchar(10),
    c_or_o_value varchar(1),
    pocket_id integer,
    pos_x decimal,
    pos_y decimal,
    pos_z decimal,
    occupancy decimal,
    temperature_factor decimal
);

ALTER TABLE ONLY filling_sphere
    ADD CONSTRAINT fk_filling_sphere_pocket_id FOREIGN KEY (pocket_id) REFERENCES pocket(id) ON DELETE CASCADE;