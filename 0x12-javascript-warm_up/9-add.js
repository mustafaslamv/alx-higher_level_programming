#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);
if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  add(a, b);
}
