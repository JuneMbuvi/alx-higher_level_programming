#!/usr/bin/node

const args = process.argv.slice(2);
const argOne = args[0];
const newInt = parseInt(argOne);
if (isNaN(newInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${newInt}`);
}
