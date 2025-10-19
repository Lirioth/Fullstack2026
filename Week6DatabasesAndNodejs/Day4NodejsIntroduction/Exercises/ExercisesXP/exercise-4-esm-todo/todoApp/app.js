// Module: app
// Purpose: Use the TodoList class (ESM) to add/complete/list tasks.
// Author: Kevin "Lirioth" Cusnir
// Date: 2025-10-19 | TZ: Asia/Jerusalem
// Notes: Console output only, minimal & clear.

import { TodoList } from "./todo.js";

const todos = new TodoList();

// Add some tasks ✅
todos.add("Review PR #42");
todos.add("Write unit tests");
todos.add("Water the cactus 🌵");

// Mark a couple as done
todos.complete(1);
todos.complete(3);

// List everything
console.log("🧠 Current tasks:");
for (const t of todos.list()) {
  const status = t.done ? "✅ done" : "⏳ pending";
  console.log(`- [${status}] (${t.id}) ${t.text}`);
}
