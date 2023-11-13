#!/usr/bin/node

const args = process.argv.slice(2);
const a = args[0];

function factorial (a) {
  if (isNaN(a)) {
    return (1);
  }
  a = parseInt(a);
  if (a <= 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
const result = factorial(a);
console.log(result);
