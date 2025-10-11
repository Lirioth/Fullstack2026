
// Daily Challenge — Todo List
// 🧠 Features: addTask, doneTask, deleteTask; DOM updates & data attributes.

// ✅ Required: start with an empty array (can store objects for BONUS)
const tasks = []; // Each item: { task_id:number, text:string, done:boolean }
let nextId = 0;   // Simple incremental id

// DOM references
const form = document.getElementById('taskForm');
const input = document.getElementById('taskInput');
const list = document.getElementById('listTasks');

// 🧱 Render a single task row into the DOM
function renderTask(task) {
  const row = document.createElement('div');
  row.className = 'task' + (task.done ? ' done' : '');
  row.dataset.taskId = String(task.task_id); // BONUS: data-task-id

  // Checkbox (done)
  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.checked = task.done;
  checkbox.setAttribute('aria-label', 'Mark as done');

  // Label (task text)
  const label = document.createElement('label');
  label.textContent = task.text;

  // Delete button with Font Awesome "X"
  const delBtn = document.createElement('button');
  delBtn.className = 'delete';
  delBtn.setAttribute('aria-label', 'Delete task');
  delBtn.innerHTML = '<i class="fa-solid fa-xmark" aria-hidden="true"></i>';

  // Assemble
  row.appendChild(checkbox);
  row.appendChild(label);
  row.appendChild(delBtn);
  list.prepend(row); // newest on top
}

// ➕ addTask(): validate, push to array, render to DOM
function addTask(text) {
  const trimmed = String(text).trim();
  if (!trimmed) {
    alert('Please enter a task.'); // 🚦 guard
    return;
  }
  const task = { task_id: nextId++, text: trimmed, done: false };
  tasks.push(task);
  renderTask(task);
  input.value = '';
  input.focus();
}

// ✅ doneTask(): toggle done both in data & DOM
function doneTask(taskId, checked) {
  const idNum = Number(taskId);
  const task = tasks.find(t => t.task_id === idNum);
  if (!task) return;
  task.done = !!checked;
  const row = list.querySelector(`[data-task-id="${taskId}"]`);
  if (row) {
    row.classList.toggle('done', task.done);
  }
}

// ❌ deleteTask(): remove from array & DOM
function deleteTask(taskId) {
  const idNum = Number(taskId);
  const idx = tasks.findIndex(t => t.task_id === idNum);
  if (idx !== -1) tasks.splice(idx, 1);
  const row = list.querySelector(`[data-task-id="${taskId}"]`);
  if (row) row.remove();
}

// 🧵 Event wiring
form.addEventListener('submit', (e) => {
  e.preventDefault();
  addTask(input.value);
});

// Event delegation for checkbox & delete button
list.addEventListener('click', (e) => {
  const target = e.target;
  // Handle delete clicks from <button> or the <i> inside
  const btn = target.closest && target.closest('button.delete');
  if (btn) {
    const row = btn.closest('.task');
    if (!row) return;
    deleteTask(row.dataset.taskId);
  }
});

list.addEventListener('change', (e) => {
  const target = e.target;
  if (target && target.matches('input[type="checkbox"]')) {
    const row = target.closest('.task');
    if (!row) return;
    doneTask(row.dataset.taskId, target.checked);
  }
});

// 🔑 Convenience: Enter key triggers submit (already handled by form), Escape clears input
input.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') input.value = '';
});
