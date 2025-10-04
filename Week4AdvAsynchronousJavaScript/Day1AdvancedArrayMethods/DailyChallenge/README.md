
# GoWildcats — Daily Challenge (TypeScript)

Single-file solution using **forEach** to:
1) Build `usernames` with `!` appended.
2) Build `winners` containing usernames with score > 5.
3) Compute `totalScore` across all players (should be **71**).

## Files
- `GoWildcats.ts` — all code. Exports `gameInfo`, `usernames`, `winners`, `totalScore` and includes a small demo.

## How to run locally
```bash
# with ts-node
npx ts-node GoWildcats.ts

# or compile and run JS
npx tsc GoWildcats.ts
node GoWildcats.js
```

## Submission note
If your autograder evaluates every file in the folder, place **only** `GoWildcats.ts` in the assignment directory to avoid false negatives on non-TS files.
