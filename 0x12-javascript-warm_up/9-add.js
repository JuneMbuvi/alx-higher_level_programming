#!/usr/bin/node

const args = process.argv.slice(2);
const a = args[0];
const b = args[1];
const newInt = parseInt(a);
const newIntTwo = parseInt(b);

function add (a, b) {
  console.log(a + b);
}
if (!isNaN(newInt) || !isNaN(newIntTwo)) {
  add(newInt, newIntTwo);
} else {
  console.log(NaN);
}
