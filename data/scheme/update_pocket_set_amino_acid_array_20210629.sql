UPDATE pocket p
SET amino_acids = (
    select
       array_agg(distinct a.amino_acid_id) as amino_acids
    from pocket p2
    join pocket_atom pa on p2.id = pa.pocket_id
    join atom a on pa.atom_id = a.id
    where p2.id = p.id
    )
WHERE druggability_score > 0.5;