// Day 1 TypeScript examples

// Simple typed function
function greet(name: string): string {
	return `Hello, ${name}!`;
}

console.log(greet("World"));

// Loop example
for (let i = 0; i < 5; i++) {
	console.log(`Index: ${i}`);
}

// Interface and object example
interface Student {
	id: number;
	name: string;
	active: boolean;
}

const students: Student[] = [
	{ id: 1, name: "Alice", active: true },
	{ id: 2, name: "Bob", active: false },
];

students
	.filter(s => s.active)
	.forEach(s => console.log(`Active student: ${s.name}`));