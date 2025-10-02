// Day 1 TypeScript examples

// Simple typed function
export function greet(name: string): string {
        return `Hello, ${name}!`;
}

export interface Student {
        id: number;
        name: string;
        active: boolean;
}

export const students: Student[] = [
        { id: 1, name: "Alice", active: true },
        { id: 2, name: "Bob", active: false },
];

export function getActiveStudents(list: Student[]): Student[] {
        return list.filter(student => student.active);
}

if (require.main === module) {
        console.log(greet("World"));

        for (let i = 0; i < 5; i++) {
                console.log(`Index: ${i}`);
        }

        getActiveStudents(students).forEach(student =>
                console.log(`Active student: ${student.name}`)
        );
}
