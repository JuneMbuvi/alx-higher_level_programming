#!/usr/bin/node

const args = process.argv.slice(2);
const x = args[0];
const newInt = parseInt(x);

if (!isNaN(newInt)) {
  for (let i = 0; i < newInt; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
