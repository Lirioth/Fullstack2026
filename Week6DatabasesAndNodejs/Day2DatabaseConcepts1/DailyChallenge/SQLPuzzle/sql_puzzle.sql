-- =============================================================
-- 🧩 Daily Challenge — SQL Puzzle (PostgreSQL)
-- Focus: NOT IN with NULLs, three-valued logic
-- =============================================================

-- Clean slate (safe to re-run)
DROP TABLE IF EXISTS FirstTab;
DROP TABLE IF EXISTS SecondTab;

-- Create tables
CREATE TABLE FirstTab (
  id   integer,
  name VARCHAR(10)
);

CREATE TABLE SecondTab (
  id integer
);

-- Seed data
INSERT INTO FirstTab (id, name) VALUES
  (5,'Pawan'),
  (6,'Sharlee'),
  (7,'Krish'),
  (NULL,'Avtaar');

INSERT INTO SecondTab (id) VALUES
  (5),
  (NULL);

-- Inspect data
SELECT * FROM FirstTab ORDER BY id NULLS LAST;
SELECT * FROM SecondTab ORDER BY id NULLS LAST;

-- =============================================================
-- Questions
-- =============================================================

/*
Q1. What will be the OUTPUT of:
  SELECT COUNT(*)
  FROM FirstTab AS ft
  WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );

Prediction: 0
Reason: Subquery set = {NULL}. Any comparison x NOT IN (NULL) is UNKNOWN → filtered out by WHERE.
*/
SELECT COUNT(*) AS q1_count
FROM FirstTab AS ft
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );

/*
Q2. What will be the OUTPUT of:
  SELECT COUNT(*)
  FROM FirstTab AS ft
  WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );

Prediction: 2 (ids 6 and 7). Row with id=5 fails; id=NULL is UNKNOWN.
*/
SELECT COUNT(*) AS q2_count
FROM FirstTab AS ft
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );

/*
Q3. What will be the OUTPUT of:
  SELECT COUNT(*)
  FROM FirstTab AS ft
  WHERE ft.id NOT IN ( SELECT id FROM SecondTab );

Prediction: 0
Reason: Subquery set = {5, NULL}. Presence of NULL poisons NOT IN: all comparisons become UNKNOWN.
*/
SELECT COUNT(*) AS q3_count
FROM FirstTab AS ft
WHERE ft.id NOT IN ( SELECT id FROM SecondTab );

/*
Q4. What will be the OUTPUT of:
  SELECT COUNT(*)
  FROM FirstTab AS ft
  WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );

Prediction: 2 (ids 6 and 7). Subquery set = {5}.
*/
SELECT COUNT(*) AS q4_count
FROM FirstTab AS ft
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );

-- =============================================================
-- Safer rewrite using NOT EXISTS (avoids NULL trap)
-- Equivalent to Q3 but correct:
-- "count rows in FirstTab with non-null id that are not present in SecondTab"
-- =============================================================
SELECT COUNT(*) AS not_exists_count
FROM FirstTab ft
WHERE ft.id IS NOT NULL
  AND NOT EXISTS (
    SELECT 1 FROM SecondTab st
    WHERE st.id = ft.id
  );

-- Show which rows those are (for clarity)
SELECT ft.*
FROM FirstTab ft
WHERE ft.id IS NOT NULL
  AND NOT EXISTS (
    SELECT 1 FROM SecondTab st
    WHERE st.id = ft.id
  )
ORDER BY ft.id;
