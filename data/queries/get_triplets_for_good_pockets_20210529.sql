select get_combinations(array_agg(distinct a.amino_acid_id), 3) as amino_acids
from pocket p
join pocket_atom pa on p.id = pa.pocket_id
join atom a on pa.atom_id = a.id
where p.druggability_score > 0.5
group by p.id, p.druggability_score
order by p.druggability_score desc;