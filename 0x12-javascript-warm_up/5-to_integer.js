#!/usr/bin/node
const argc = process.argv;
if (argc[2] !== undefined && !isNaN(argc[2])) {
  console.log(`My number: ${Math.floor(Number(argc[2]))}`);
} else {
  console.log('Not a number');
}
