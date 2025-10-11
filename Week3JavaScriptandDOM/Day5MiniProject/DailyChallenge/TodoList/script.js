
// Daily Challenge — Todo List
// IDs used: taskForm, taskInput, listTasks

// Data model
const tasks = []; // Each item: { task_id:number, text:string, done:boolean }
let nextId = 0;

// DOM refs
const form = document.getElementById('taskForm');
const input = document.getElementById('taskInput');
const list = document.getElementById('listTasks');

// Render one task row
function renderTask(task) {
  const row = document.createElement('div');
  row.className = 'task' + (task.done ? ' done' : '');
  row.dataset.taskId = String(task.task_id); // data-task-id

  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.checked = task.done;
  checkbox.setAttribute('aria-label', 'Mark as done');

  const label = document.createElement('label');
  label.textContent = task.text;

  const delBtn = document.createElement('button');
  delBtn.className = 'delete';
  delBtn.setAttribute('aria-label', 'Delete task');
  delBtn.innerHTML = '<i class="fa-solid fa-xmark" aria-hidden="true"></i>';

  row.append(checkbox, label, delBtn);
  list.prepend(row); // newest on top
}

// Add task
function addTask(text) {
  const trimmed = String(text).trim();
  if (!trimmed) {
    alert('Please enter a task.');
    return;
  }
  const task = { task_id: nextId++, text: trimmed, done: false };
  tasks.push(task);
  renderTask(task);
  input.value = '';
  input.focus();
}

// Toggle done
function doneTask(taskId, checked) {
  const idNum = Number(taskId);
  const task = tasks.find(t => t.task_id === idNum);
  if (!task) return;
  task.done = Boolean(checked);
  const row = list.querySelector(`[data-task-id="${taskId}"]`);
  if (row) row.classList.toggle('done', task.done);
}

// Delete task
function deleteTask(taskId) {
  const idNum = Number(taskId);
  const idx = tasks.findIndex(t => t.task_id === idNum);
  if (idx !== -1) tasks.splice(idx, 1);
  const row = list.querySelector(`[data-task-id="${taskId}"]`);
  if (row) row.remove();
}

// Submit handler
form.addEventListener('submit', (e) => {
  e.preventDefault();
  addTask(input.value);
});

// Event delegation for delete clicks (and checkbox changes)
list.addEventListener('click', (e) => {
  // Handle delete via the button or its child icon
  const btn = e.target.closest && e.target.closest('button.delete');
  if (btn) {
    const row = btn.closest('.task');
    if (!row) return;
    deleteTask(row.dataset.taskId);
  }
});

list.addEventListener('change', (e) => {
  if (e.target.matches('input[type="checkbox"]')) {
    const row = e.target.closest('.task');
    if (!row) return;
    doneTask(row.dataset.taskId, e.target.checked);
  }
});

// Convenience: Esc clears input
input.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') input.value = '';
});
