# Daily Challenge — SQL Puzzle (PostgreSQL)

This pack contains:
- `sql_puzzle.sql` — tables, sample data, the four queries (Q1–Q4), and **predicted outputs** in comments, plus a safe `NOT EXISTS` rewrite.
- `README.md` — how to run.

Emojis are used, no hearts.

## How to run (pgAdmin or psql)

### pgAdmin
1. Open the **Query Tool** in the database of your choice.
2. Click the **open** (folder) icon and load `sql_puzzle.sql`.
3. Run it. You’ll see result grids for each query.

### psql
```bash
psql -d your_db -f sql_puzzle.sql
```

## Expected answers (before running)
- Q1 → **0**
- Q2 → **2**
- Q3 → **0**
- Q4 → **2**

Why: `NULL` inside a `NOT IN` list makes the predicate evaluate to `UNKNOWN` for every row; only the versions whose subquery returns `{5}` behave as intended. See comments inside the SQL for a concise explanation and a safer `NOT EXISTS` pattern. ✅
