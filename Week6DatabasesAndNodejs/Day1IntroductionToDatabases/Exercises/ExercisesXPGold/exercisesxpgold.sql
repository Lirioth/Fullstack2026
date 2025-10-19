-- File: exercisesxpgold.sql
-- Purpose: XP Gold — Students #2 (required queries, ENGLISH comments)
-- Author: Kevin Cusnir
-- Date: 2025-10-18 | TZ: Asia/Jerusalem

/* All queries must return first_name, last_name, and birth_date.
   Assumes table public.students exists in the 'bootcamp' database (from XP+). */

-- 1) First four students, ordered alphabetically by last_name (tie-break by first_name)
SELECT first_name, last_name, birth_date
FROM public.students
ORDER BY last_name ASC, first_name ASC
LIMIT 4;

-- 2) Youngest student (newest birth_date first)
SELECT first_name, last_name, birth_date
FROM public.students
ORDER BY birth_date DESC
LIMIT 1;

-- 3) Return three students, skipping the first two (stable order by id)
SELECT first_name, last_name, birth_date
FROM public.students
ORDER BY id ASC
OFFSET 2 LIMIT 3;
