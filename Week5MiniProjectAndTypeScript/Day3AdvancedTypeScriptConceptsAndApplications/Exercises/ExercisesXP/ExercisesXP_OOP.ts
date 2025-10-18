// ExercisesXP OOP — TypeScript (Exercises 1–5) — Single File
// -----------------------------------------------------------
// Keep ONLY this file in your submission folder if your autograder scans all files.
// This file uses classes, interfaces, access modifiers, readonly, inheritance, and static members.
// A small demo is provided at the bottom under a safe Node guard.

// =====================================
// Exercise 1: Class with Access Modifiers
// =====================================
export class Employee {
  // private: only visible inside Employee
  private name: string;
  private salary: number;

  // public: visible everywhere
  public position: string;

  // protected: visible in this class and subclasses
  protected department: string;

  constructor(name: string, salary: number, position: string, department: string) {
    this.name = name;
    this.salary = salary;
    this.position = position;
    this.department = department;
  }

  // Public method can read private field `name`
  public getEmployeeInfo(): string {
    return `Employee: ${this.name} (${this.position})`;
  }

  // Protected helper for subclasses
  protected getDepartment(): string {
    return this.department;
  }
}

// =====================================
// Exercise 2: Readonly Properties in a Class
// =====================================
export class Product {
  public readonly id: number; // cannot be reassigned after construction
  public name: string;
  public price: number;

  constructor(id: number, name: string, price: number) {
    this.id = id;
    this.name = name;
    this.price = price;
  }

  public getProductInfo(): string {
    return `${this.name} - $${this.price.toFixed(2)}`;
  }
}

// Attempting to modify `id` would cause a compile-time error (uncomment to see the error):
// const p = new Product(1, "Book", 19.99);
// p.id = 2; // Error: Cannot assign to 'id' because it is a read-only property.

// ===========================
// Exercise 3: Class Inheritance
// ===========================
export class Animal {
  public name: string;
  constructor(name: string) {
    this.name = name;
  }
  public makeSound(): string {
    return "(generic sound)";
  }
}

export class Dog extends Animal {
  constructor(name: string) {
    super(name);
  }
  // Override
  public override makeSound(): string {
    return "bark";
  }
}

// =====================================
// Exercise 4: Static Properties & Methods
// =====================================
export class Calculator {
  // Static methods: callable without an instance
  public static add(a: number, b: number): number {
    return a + b;
  }
  public static subtract(a: number, b: number): number {
    return a - b;
  }
}

// ======================================================
// Exercise 5: Extending Interfaces (Optional & Readonly)
// ======================================================
export interface User {
  readonly id: number;
  name: string;
  email: string;
}

export interface PremiumUser extends User {
  membershipLevel?: "silver" | "gold" | "platinum";
}

export function printUserDetails(u: PremiumUser): void {
  const level = u.membershipLevel ? ` | Membership: ${u.membershipLevel}` : "";
  console.log(`User #${u.id}: ${u.name} <${u.email}>${level}`);
}

// ------------------------
// Optional demo (guarded):
// ------------------------
declare const require: any | undefined;
declare const module: any | undefined;

if (typeof require !== "undefined" && typeof module !== "undefined" && require.main === module) {
  // Ex1
  const emp = new Employee("Ada Lovelace", 120000, "Engineer", "R&D");
  console.log(emp.getEmployeeInfo());

  // Ex3
  const dog = new Dog("Fido");
  console.log(`${dog.name} says:`, dog.makeSound());

  // Ex4
  console.log("Calc add:", Calculator.add(10, 5));
  console.log("Calc subtract:", Calculator.subtract(10, 5));

  // Ex5
  const pu: PremiumUser = {
    id: 101,
    name: "Kevin Cusnir",
    email: "kevin@example.com",
    membershipLevel: "gold",
  };
  printUserDetails(pu);
}
