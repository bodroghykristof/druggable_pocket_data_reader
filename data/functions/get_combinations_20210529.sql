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

alter function get_combinations(anyarray, integer) owner to bodroghy;