# exercisesxpgold — Students #2 (PostgreSQL, EN)

**Date:** 2025-10-18 (Asia/Jerusalem)  
**Author:** Kevin Cusnir

## What's inside
- `exercisesxpgold.sql` — three required queries:
  1. First 4 students ordered by `last_name` (then `first_name`).
  2. Youngest student (`ORDER BY birth_date DESC LIMIT 1`).
  3. Three students skipping the first two (`ORDER BY id`, `OFFSET 2 LIMIT 3`).

## How to run in pgAdmin 4
1. Make sure the **bootcamp** database and table **public.students** already exist (from XP+).
2. In the Browser, right‑click **bootcamp** → **Query Tool**.
3. **File → Open…** → select `exercisesxpgold.sql` → **Execute** (F5).
4. See results in **Data Output**. You can also browse: Databases → bootcamp → Schemas → public → Tables → `students`.

## GitHub
```bash
git add exercisesxpgold.sql exercisesxpgold.md
git commit -m "feat(sql): XP Gold — Students #2 queries (EN)"
git push
```
