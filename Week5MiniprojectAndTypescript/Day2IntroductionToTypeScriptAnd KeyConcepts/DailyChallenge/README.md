
# UnionTypeValidator — TypeScript Daily Challenge

Single-file solution that validates a value against a list of allowed types (as strings) using `typeof` and a few safe aliases.

## Function
```ts
export function validateUnionType(value: any, allowedTypes: string[]): boolean
```
- Returns `true` if `value` matches at least one string in `allowedTypes`.
- Built-in support for: `string | number | boolean | undefined | symbol | bigint | function | object`
- Aliases handled: `array | null | date | integer`
- Any unknown type string falls back to direct `typeof` comparison.

## Files
- `UnionTypeValidator.ts` — all code in one file. Includes a guarded demo that prints validation results for various values.

## Run locally
```bash
# with ts-node
npx ts-node UnionTypeValidator.ts

# or compile and run JS
npx tsc UnionTypeValidator.ts
node UnionTypeValidator.js
```

## Submission note
If your autograder evaluates every file in the folder, place **only** `UnionTypeValidator.ts` in the assignment directory to avoid false negatives on non-TS files.
