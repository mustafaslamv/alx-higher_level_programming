#!/usr/bin/node
const countNumber = Number(process.argv[2]);
if (isNaN(countNumber)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < countNumber; index++) {
    console.log('C is fun');
  }
}
