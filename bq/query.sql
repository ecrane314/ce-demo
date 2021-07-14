CREATE OR REPLACE TABLE
  `nlp.top-50-ent-per-unit` AS
SELECT
  unit,
  permission_groups,
  `groups`,
  entity.name,
  CAST(COUNT(entity.name) AS int) AS mentions
FROM
  `sc-nlp.nlp.nlp_raw_test_512`,
  UNNEST(entities) AS entity
WHERE
  mentions>=50
GROUP BY
  unit,
  permission_groups,
  `groups`,
  entity.name
ORDER BY
  `groups`,
  mentions DESC
LIMIT
  10000

 #entities.name
  #entities.type
  #entities.mentions.text.content