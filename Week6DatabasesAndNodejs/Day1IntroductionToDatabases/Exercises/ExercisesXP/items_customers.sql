-- Module: items_customers.sql
-- Purpose: Create a PostgreSQL database & schema for Items/Customers, insert seed data, and run required queries.
-- Author: Kevin "Lirioth" Cusnir
-- Date: 2025-10-18 | TZ: Asia/Jerusalem
-- Notes: Safe to re-run in psql (tables are dropped if exist). In pgAdmin, create DB first, then run from STEP 2.

-- =========================================================
-- STEP 1) (psql only) Create the database (skip in pgAdmin if already created)
-- =========================================================
-- CREATE DATABASE xp_exercises;

-- =========================================================
-- STEP 2) Use the database (psql uses -d xp_exercises; in pgAdmin choose it in the browser)
-- =========================================================
-- We work inside the default schema: public

-- ---------- Safety: drop old tables to allow re-runs ----------
DROP TABLE IF EXISTS public.items CASCADE;
DROP TABLE IF EXISTS public.customers CASCADE;

-- ---------- Create tables ----------
-- Table: items
CREATE TABLE public.items (
    id     SERIAL PRIMARY KEY,
    name   TEXT NOT NULL,
    price  INTEGER NOT NULL CHECK (price >= 0)
);

-- Table: customers
CREATE TABLE public.customers (
    id          SERIAL PRIMARY KEY,
    first_name  TEXT NOT NULL,
    last_name   TEXT NOT NULL
);

-- ---------- Insert data ----------
-- Items:
INSERT INTO public.items (name, price) VALUES
    ('Small Desk', 100),
    ('Large Desk', 300),
    ('Fan', 80);

-- Customers:
INSERT INTO public.customers (first_name, last_name) VALUES
    ('Greg',    'Jones'),
    ('Sandra',  'Jones'),
    ('Scott',   'Scott'),
    ('Trevor',  'Green'),
    ('Melanie', 'Johnson');

-- ---------- Required queries ----------
-- 1) All the items
-- Expect 3 rows.
SELECT * FROM public.items ORDER BY id;

-- 2) All the items with a price above 80 (80 not included)
-- Expect 2 rows: Small Desk (100), Large Desk (300)
SELECT * FROM public.items WHERE price > 80 ORDER BY price;

-- 3) All the items with a price below or equal to 300 (300 included)
-- Expect 3 rows: Fan (80), Small Desk (100), Large Desk (300)
SELECT * FROM public.items WHERE price <= 300 ORDER BY price;

-- 4) All customers whose last name is 'Smith'
-- Expect 0 rows with the current seed (no Smith in inserts)
SELECT * FROM public.customers WHERE last_name = 'Smith' ORDER BY id;

-- 5) All customers whose last name is 'Jones'
-- Expect 2 rows: Greg Jones, Sandra Jones
SELECT * FROM public.customers WHERE last_name = 'Jones' ORDER BY first_name;

-- 6) All customers whose first name is not 'Scott'
-- Expect 4 rows (everyone except Scott Scott)
SELECT * FROM public.customers WHERE first_name <> 'Scott' ORDER BY last_name, first_name;
