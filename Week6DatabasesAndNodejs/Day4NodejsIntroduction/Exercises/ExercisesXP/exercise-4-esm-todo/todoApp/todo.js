// Module: todo
// Purpose: Export a simple TodoList class (ES Modules).
// Author: Kevin "Lirioth" Cusnir
// Date: 2025-10-19 | TZ: Asia/Jerusalem
// Notes: In-memory only; no persistence for this tiny demo. ✅

/**
 * @typedef {Object} Task
 * @property {number} id
 * @property {string} text
 * @property {boolean} done
 */

export class TodoList {
  constructor() {
    /** @type {Task[]} */
    this.tasks = [];
    this._nextId = 1;
  }

  /**
   * Add a task.
   * @param {string} text
   * @returns {Task}
   */
  add(text) {
    if (typeof text !== "string" || !text.trim()) {
      throw new Error("Task text must be a non-empty string.");
    }
    const t = { id: this._nextId++, text: text.trim(), done: false };
    this.tasks.push(t);
    return t;
  }

  /**
   * Mark a task as complete.
   * @param {number} id
   * @returns {boolean} true if toggled
   */
  complete(id) {
    const t = this.tasks.find(x => x.id === id);
    if (!t) return false;
    t.done = true;
    return true;
  }

  /**
   * List all tasks.
   * @returns {Task[]}
   */
  list() {
    return [...this.tasks];
  }
}
