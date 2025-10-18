-- File: exercisesxpplus.sql
-- Purpose: XP+ — Students table: create table, insert rows, and run required queries.
-- Author: Kevin Cusnir
-- Date: 2025-10-18 | TZ: Asia/Jerusalem

/* ------------------------------------------------------------
   0) Create database (run ONCE as a standalone statement in pgAdmin)
      If it already exists, skip this step.
      -- CREATE DATABASE bootcamp;
   After creating the DB, connect your Query Tool to 'bootcamp'.
------------------------------------------------------------- */

/* ------------------------------------------------------------
   1) Create table
------------------------------------------------------------- */
CREATE TABLE IF NOT EXISTS public.students (
  id          SERIAL PRIMARY KEY,
  first_name  TEXT NOT NULL,
  last_name   TEXT NOT NULL,
  birth_date  DATE NOT NULL
);

/* ------------------------------------------------------------
   2) Insert the provided data (efficient multi-row insert)
      Original dates were DD/MM/YYYY — parsed with to_date.
------------------------------------------------------------- */
INSERT INTO public.students (first_name, last_name, birth_date) VALUES
  ('Marc',   'Benichou', to_date('02/11/1998','DD/MM/YYYY')),
  ('Yoan',   'Cohen',    to_date('03/12/2010','DD/MM/YYYY')),
  ('Lea',    'Benichou', to_date('27/07/1987','DD/MM/YYYY')),
  ('Amelia', 'Dux',      to_date('07/04/1996','DD/MM/YYYY')),
  ('David',  'Grez',     to_date('14/06/2003','DD/MM/YYYY')),
  ('Omer',   'Simpson',  to_date('03/10/1980','DD/MM/YYYY'));

/* 2b) Insert your own row (OPTIONAL) — edit and uncomment
-- INSERT INTO public.students (first_name, last_name, birth_date)
-- VALUES ('YourFirst','YourLast', DATE 'YYYY-MM-DD');
*/

/* ------------------------------------------------------------
   3) SELECT queries
------------------------------------------------------------- */

-- 3.1 All data
SELECT * FROM public.students ORDER BY id;

-- 3.2 All first_names and last_names
SELECT first_name, last_name FROM public.students ORDER BY id;

/* From here on, only first_name and last_name: */

-- 3.3 Student with id = 2
SELECT first_name, last_name FROM public.students WHERE id = 2;

-- 3.4 last_name = 'Benichou' AND first_name = 'Marc'
SELECT first_name, last_name
FROM public.students
WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- 3.5 last_name = 'Benichou' OR first_name = 'Marc'
SELECT first_name, last_name
FROM public.students
WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- 3.6 first_name contains the letter 'a' (case-insensitive)
SELECT first_name, last_name
FROM public.students
WHERE first_name ILIKE '%a%';

-- 3.7 first_name starts with 'a' (case-insensitive)
SELECT first_name, last_name
FROM public.students
WHERE first_name ILIKE 'a%';

-- 3.8 first_name ends with 'a' (case-insensitive)
SELECT first_name, last_name
FROM public.students
WHERE first_name ILIKE '%a';

-- 3.9 second-to-last letter of first_name is 'a' (e.g., 'Leah')
SELECT first_name, last_name
FROM public.students
WHERE first_name ILIKE '%a_';

-- 3.10 ids equal to 1 AND 3 (interpreted as "in (1,3)")
SELECT first_name, last_name
FROM public.students
WHERE id IN (1,3);

-- 3.11 birth_date >= 2000-01-01 (show all info)
SELECT *
FROM public.students
WHERE birth_date >= DATE '2000-01-01'
ORDER BY birth_date;
