// TypeGuardUnion — Daily Challenge: Type Guard with Union Types
// -------------------------------------------------------------
// Run with:  npx ts-node TypeGuardUnion.ts
// Or compile: npx tsc TypeGuardUnion.ts && node TypeGuardUnion.js

// 1) Define the types
export type User = {
  type: 'user';
  name: string;
  age: number;
};

export type Product = {
  type: 'product';
  id: number;
  price: number;
};

export type Order = {
  type: 'order';
  orderId: string;
  amount: number;
};

export type Mixed = User | Product | Order;

// Optional helpers: runtime type guard predicates
export function isUser(x: any): x is User {
  return x && x.type === 'user' && typeof x.name === 'string' && typeof x.age === 'number';
}
export function isProduct(x: any): x is Product {
  return x && x.type === 'product' && typeof x.id === 'number' && typeof x.price === 'number';
}
export function isOrder(x: any): x is Order {
  return x && x.type === 'order' && typeof x.orderId === 'string' && typeof x.amount === 'number';
}

// 2) handleData implementation with type guards
export function handleData(items: Array<Mixed | unknown>): string[] {
  const results: string[] = [];
  for (let i = 0; i < items.length; i++) {
    const item = items[i];

    // Primary discriminant guard via `type` field + predicate checks
    if (isUser(item)) {
      results.push(`Hello ${item.name}, age ${item.age}.`);
      continue;
    }
    if (isProduct(item)) {
      results.push(`Product #${item.id} costs $${item.price.toFixed(2)}.`);
      continue;
    }
    if (isOrder(item)) {
      results.push(`Order ${item.orderId}: amount $${item.amount.toFixed(2)}.`);
      continue;
    }

    // 3) Graceful handling of unexpected cases
    // Instead of throwing, return a descriptive message
    results.push(`Unknown item at index ${i}.`);
  }
  return results;
}

// ---- Quick demo ----
if (require.main === module) {
  const data: Array<Mixed | unknown> = [
    { type: 'user', name: 'Kevin', age: 30 },
    { type: 'product', id: 101, price: 49.9 },
    { type: 'order', orderId: 'ORD-2025-0001', amount: 120.5 },
    { type: 'mystery', foo: 'bar' }, // unexpected case
  ];

  const out = handleData(data);
  for (const line of out) console.log(line);
}
