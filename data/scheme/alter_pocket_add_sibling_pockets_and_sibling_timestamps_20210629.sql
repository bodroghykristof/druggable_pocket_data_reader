ALTER TABLE pocket
DROP COLUMN IF EXISTS sibling_pockets_50;

ALTER TABLE pocket
ADD COLUMN sibling_pockets_50 integer[];

ALTER TABLE pocket
DROP COLUMN IF EXISTS sibling_snapshots_50;

ALTER TABLE pocket
ADD COLUMN sibling_snapshots_50 integer[];

ALTER TABLE pocket
DROP COLUMN IF EXISTS sibling_pockets_75;

ALTER TABLE pocket
ADD COLUMN sibling_pockets_75 integer[];

ALTER TABLE pocket
DROP COLUMN IF EXISTS sibling_snapshots_75;

ALTER TABLE pocket
ADD COLUMN sibling_snapshots_75 integer[];