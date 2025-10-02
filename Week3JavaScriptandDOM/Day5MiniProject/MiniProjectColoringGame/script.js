// state
const grid = document.getElementById('grid');
const picker = document.getElementById('colorPicker');
const sizeSel = document.getElementById('sizeSelect');
const clearBtn = document.getElementById('clearBtn');
let color = picker.value;
let drawing = false;

// build grid (responsive squares)
function build(n){
  grid.innerHTML = '';
  grid.style.gridTemplateColumns = `repeat(${n}, minmax(0, 1fr))`;
  for(let i=0;i<n*n;i++){
    const c = document.createElement('div');
    c.className = 'cell';
    c.addEventListener('mouseover', e=> drawing && paint(e));
    c.addEventListener('mousedown', paint);
    grid.appendChild(c);
  }
}

// paint cell
function paint(e){ e.target.style.background = color; }

// mouse events
document.addEventListener('mousedown', ()=> drawing = true);
document.addEventListener('mouseup',   ()=> drawing = false);
document.addEventListener('mouseleave',()=> drawing = false);

// color change
picker.addEventListener('input', e=> color = e.target.value);
document.querySelectorAll('.swatch').forEach(s=> s.onclick = ()=>{ color = s.dataset.color; picker.value = color; });

// size change
sizeSel.onchange = ()=> build(parseInt(sizeSel.value,10));

// clear
clearBtn.onclick = ()=> document.querySelectorAll('.cell').forEach(c=> c.style.background='');

// start
build(parseInt(sizeSel.value,10));
