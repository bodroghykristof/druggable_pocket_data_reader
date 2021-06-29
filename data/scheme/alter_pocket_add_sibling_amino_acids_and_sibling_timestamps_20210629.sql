ALTER TABLE pocket
DROP COLUMN IF EXISTS sibling_amino_acids;

ALTER TABLE pocket
ADD COLUMN sibling_amino_acids integer[];

ALTER TABLE pocket
DROP COLUMN IF EXISTS sibling_timestamps;

ALTER TABLE pocket
ADD COLUMN sibling_timestamps integer[];