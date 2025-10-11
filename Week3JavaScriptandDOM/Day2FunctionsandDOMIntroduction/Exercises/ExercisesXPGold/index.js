// Exercises XP Gold — JS Functions + DOM

// Exercise 1 : is_Blank
function isBlank(str) {
  return str.length === 0;
}
console.log('Exercise 1 — isBlank:', isBlank(''), isBlank('abc'));

// Exercise 2 : Abbrev_name
function abbrevName(fullName) {
  const parts = String(fullName).trim().split(/\s+/);
  if (parts.length === 0) return '';
  if (parts.length === 1) return parts[0];
  const first = parts[0];
  const lastInitial = parts[1][0] ? parts[1][0].toUpperCase() + '.' : '';
  return first + ' ' + lastInitial;
}
console.log('Exercise 2 — abbrevName:', abbrevName('Robin Singh'));

// Exercise 3 : SwapCase
function swapCase(s) {
  let out = '';
  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    const up = ch.toUpperCase();
    const low = ch.toLowerCase();
    out += ch === up ? low : up;
  }
  return out;
}
console.log('Exercise 3 — swapCase:', swapCase('The Quick Brown Fox'));

// Exercise 4 : Omnipresent value
function isOmnipresent(arrOfArrs, value) {
  if (!Array.isArray(arrOfArrs)) return false;
  for (let i = 0; i < arrOfArrs.length; i++) {
    const sub = arrOfArrs[i];
    let found = false;
    for (let j = 0; j < sub.length; j++) {
      if (sub[j] === value) { found = true; break; }
    }
    if (!found) return false;
  }
  return true;
}
console.log('Exercise 4 — isOmnipresent:', 
  isOmnipresent([[1,1],[1,3],[5,1],[6,1]], 1),
  isOmnipresent([[1,1],[1,3],[5,1],[6,1]], 6)
);

// Exercise 5 : Red table (DOM)
(function colorDiagonalRed() {
  const table = document.getElementById('grid');
  if (!table) return;
  for (let row = 0; row < table.rows.length; row++) {
    const cell = table.rows[row].cells[row];
    if (cell) {
      cell.classList.add('red');
    }
  }
})();
