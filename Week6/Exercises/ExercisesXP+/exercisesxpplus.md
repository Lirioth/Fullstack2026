# exercisesxpplus — XP+ Students (PostgreSQL)

**Date:** 2025-10-18 (Asia/Jerusalem)  
**Author:** Kevin Cusnir

## What this includes
- `exercisesxpplus.sql` — creates the `students` table, inserts the six provided rows, and runs all required SELECT queries.

## Run steps (pgAdmin 4)
1. Create the database once (standalone): `CREATE DATABASE bootcamp;`
2. Connect the Query Tool to **bootcamp**.
3. Open `exercisesxpplus.sql` and click **Execute**.
4. Results appear in **Data Output**. You can also browse: Databases → bootcamp → Schemas → public → Tables → `students`.

## Query highlights
- Case-insensitive text matches use `ILIKE` (e.g., contains/starts/ends with 'a').
- “ids equal to 1 AND 3” is implemented as `WHERE id IN (1,3)`.
- Dates are parsed from DD/MM/YYYY with `to_date(...)`.
