ALTER TABLE pocket
DROP COLUMN IF EXISTS amino_acids;

ALTER TABLE pocket
ADD COLUMN amino_acids integer[];