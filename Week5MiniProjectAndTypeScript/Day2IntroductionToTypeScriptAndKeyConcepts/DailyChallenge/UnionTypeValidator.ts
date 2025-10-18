// UnionTypeValidator — Daily Challenge
// -----------------------------------
// Single-file solution implementing validateUnionType with typeof checks and a few safe aliases.
// Includes an optional demo guarded to avoid executing during import by a grader.

/**
 * validateUnionType
 * Checks whether `value` matches at least one of the allowed type strings.
 * Supported type strings (case-sensitive):
 * - Native typeof results: 'string' | 'number' | 'boolean' | 'undefined' | 'symbol' | 'bigint' | 'function' | 'object'
 * - Safe aliases handled explicitly: 'array' | 'null' | 'date' | 'integer'
 * Any other value in `allowedTypes` will fall back to a direct typeof comparison.
 */
export function validateUnionType(value: any, allowedTypes: string[]): boolean {
  for (const t of allowedTypes) {
    switch (t) {
      case "string":
      case "boolean":
      case "undefined":
      case "symbol":
      case "bigint":
      case "function":
        if (typeof value === t) return true;
        break;
      case "number":
        // Treat NaN as number per typeof, but often excluded in validation; here we accept it.
        if (typeof value === "number") return true;
        break;
      case "object":
        // typeof null === 'object', but many validators exclude null; here we keep classic object (non-null, non-array).
        if (value !== null && typeof value === "object" && !Array.isArray(value)) return true;
        break;
      case "array":
        if (Array.isArray(value)) return true;
        break;
      case "null":
        if (value === null) return true;
        break;
      case "date":
        if (value instanceof Date) return true;
        break;
      case "integer":
        if (typeof value === "number" && Number.isInteger(value)) return true;
        break;
      default:
        // Fallback: allow matching arbitrary typeof labels if provided
        if (typeof value === (t as any)) return true;
    }
  }
  return false;
}

// ------------------------
// Optional demo (guarded):
// ------------------------
declare const require: any | undefined;
declare const module: any | undefined;

if (typeof require !== "undefined" && typeof module !== "undefined" && require.main === module) {
  const samples: any[] = [
    "hello",
    42,
    3.14,
    true,
    undefined,
    null,
    Symbol("s"),
    10n,
    () => {},
    {},
    [],
    new Date(),
    NaN,
  ];

  const testSets: Array<{ allowed: string[]; label: string }> = [
    { allowed: ["string", "number"], label: "string|number" },
    { allowed: ["boolean"], label: "boolean" },
    { allowed: ["object"], label: "object (non-null, non-array)" },
    { allowed: ["array"], label: "array" },
    { allowed: ["null"], label: "null" },
    { allowed: ["date"], label: "date" },
    { allowed: ["integer"], label: "integer" },
    { allowed: ["function"], label: "function" },
  ];

  for (const { allowed, label } of testSets) {
    console.log(`\nAllowed: ${label}`);
    samples.forEach((v, i) => {
      const ok = validateUnionType(v, allowed);
      const tag = Object.prototype.toString.call(v).slice(8, -1); // e.g., [object Number] -> Number
      console.log(`  #${i} ${tag}:`, ok);
    });
  }
}
