#!/usr/bin/node
const arr = process.argv.slice(2).map(Number);
console.log(arr);
const len = arr.length;
if (len === 0 || len === 1) {
  console.log(0);
} else {
  arr.sort((a, b) => a - b);
  console.log(arr[len - 1]);
}
