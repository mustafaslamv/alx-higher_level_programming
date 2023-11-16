#!/usr/bin/node

function factorial (number) {
  number = parseInt(number);
  if (number == NaN) {
    return 1;
  } else if (number == 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}
const result = factorial(333);
console.log(result);
