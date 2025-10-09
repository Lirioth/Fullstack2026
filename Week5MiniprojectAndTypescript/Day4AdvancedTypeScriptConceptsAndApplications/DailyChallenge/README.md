
# TypeGuardUnion — Daily Challenge: Type Guard with Union Types

Single-file TypeScript solution demonstrating discriminated unions and custom type guards.

## File
- `TypeGuardUnion.ts` — types (`User | Product | Order`), guard predicates, and `handleData` implementation with graceful fallback.

## Requirements
- Node.js 18+

## Run with ts-node
```bash
npx ts-node TypeGuardUnion.ts
```

## Compile and run with tsc
```bash
npx tsc TypeGuardUnion.ts
node TypeGuardUnion.js
```

## Notes
- Uses discriminated unions via the `type` field and predicate functions (`isUser`, `isProduct`, `isOrder`).
- `handleData` returns an array of messages and handles unexpected cases by returning a descriptive string instead of throwing.

---

## 📜 License

This exercise follows the repository-wide MIT terms; see the [LICENSE](../../../LICENSE) file for details.
