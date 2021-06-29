create function get_combinations(source anyarray, size integer) returns SETOF anyarray
    language sql
as
$$
with recursive combinations(combination, indices) as (
   select source[i:i], array[i] from generate_subscripts(source, 1) i
   union all
   select c.combination || source[j], c.indices || j
   from   combinations c, generate_subscripts(source, 1) j
   where  j > all(c.indices) and
          array_length(c.combination, 1) < size
 )
 select combination from combinations
 where  array_length(combination, 1) = size;
$$;

create or replace view best_triplets as
    select
       amino_acids,
       count(*) as occurance,
       array_agg(score) as scores,
       array_agg(snapshot) as snapshots
    from(
        select get_combinations(array_agg(distinct a.amino_acid_id), 3) as amino_acids,
               p.druggability_score as score,
               p.snapshot
        from pocket p
        join pocket_atom pa on p.id = pa.pocket_id
        join atom a on pa.atom_id = a.id
        where p.druggability_score > 0.5
        group by p.id, p.druggability_score
        order by p.druggability_score desc) as get_triplets
    group by amino_acids
order by occurance desc, max(score) desc;

select * from best_triplets;