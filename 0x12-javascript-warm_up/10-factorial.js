#!/usr/bin/node
const number = Number(process.argv[2]);

function factorial (number) {
  number = parseInt(number);
  if (isNaN(number)) {
    return 1;
  } else if (number == 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}
const result = factorial(number);
console.log(result);
