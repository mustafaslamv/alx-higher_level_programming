#!/usr/bin/node
const size = Number(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < size; index++) {
    let row = '';
    for (let index = 0; index < size; index++) {
      row += 'X';
    }
    console.log(row);
  }
}
