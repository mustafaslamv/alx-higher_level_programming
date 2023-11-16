#!/usr/bin/node
const arr = process.argv;
arr.splice(0, 2);
const len = arr.length;
if (len === 0 || len === 1) {
  console.log(0);
} else {
  arr.sort();
  console.log(arr[len - 1]);
}
