// todo list with BONUS: objects, doneTask, deleteTask

// my tasks as objects
// example: { task_id: 0, text: "Buy milk", done: false }
const tasks = [];

// get elements
const form = document.getElementById('taskForm');
const input = document.getElementById('taskInput');
const list = document.getElementById('listTasks');

// id counter starts at 0
let nextId = 0;

// add a new task (object) and render it
function addTask(text) {
  // create the object
  const task = {
    task_id: nextId++, // unique id
    text: text,
    done: false // default
  };

  // save in array
  tasks.push(task);

  // show on the page
  renderTask(task);
}

// build one row in the DOM
function renderTask(task) {
  // main row
  const row = document.createElement('div');
  row.className = 'task';
  // add data attribute with the same value as task_id
  row.dataset.taskId = String(task.task_id);

  // checkbox
  const check = document.createElement('input');
  check.type = 'checkbox';
  check.id = 'task-' + task.task_id;
  check.checked = task.done; // if true, keep it checked

  // label
  const label = document.createElement('label');
  label.htmlFor = check.id;
  label.textContent = task.text;

  // delete button (Font Awesome "X")
  const btn = document.createElement('button');
  btn.className = 'deleteBtn';
  btn.innerHTML = '<i class="fa-solid fa-xmark" aria-hidden="true"></i>';

  // set initial done style if needed
  if (task.done) {
    row.classList.add('done');
  }

  // when checkbox changes => toggle done
  check.addEventListener('change', function () {
    doneTask(task.task_id, check.checked, row);
  });

  // when delete is clicked => remove
  btn.addEventListener('click', function () {
    deleteTask(task.task_id, row);
  });

  // put elements inside row
  row.appendChild(check);
  row.appendChild(label);
  row.appendChild(btn);

  // add row to the list
  list.appendChild(row);
}

// toggle done property in the object and update the DOM
function doneTask(id, isDone, rowEl) {
  // find the object in the array
  const task = tasks.find(t => t.task_id === id);
  if (!task) return; // simple guard

  // update object
  task.done = isDone;

  // update DOM style
  if (isDone) {
    rowEl.classList.add('done');
  } else {
    rowEl.classList.remove('done');
  }
}

// delete a task by id from array and from DOM
function deleteTask(id, rowEl) {
  // remove from array
  const index = tasks.findIndex(t => t.task_id === id);
  if (index > -1) {
    tasks.splice(index, 1);
  }

  // remove from DOM
  if (rowEl && rowEl.parentNode) {
    rowEl.parentNode.removeChild(rowEl);
  }
}

// handle form submit
form.addEventListener('submit', function (e) {
  e.preventDefault(); // stop page refresh

  // read text
  const text = input.value.trim();

  // basic validation
  if (text === '') {
    alert('Please write a task :)');
    return;
  }

  // add task
  addTask(text);

  // reset input
  input.value = '';
  input.focus();
});
