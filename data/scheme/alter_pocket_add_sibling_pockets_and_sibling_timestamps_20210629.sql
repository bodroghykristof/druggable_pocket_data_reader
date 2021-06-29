ALTER TABLE pocket
DROP COLUMN IF EXISTS sibling_pockets;

ALTER TABLE pocket
ADD COLUMN sibling_pockets integer[];

ALTER TABLE pocket
DROP COLUMN IF EXISTS sibling_timestamps;

ALTER TABLE pocket
ADD COLUMN sibling_timestamps integer[];