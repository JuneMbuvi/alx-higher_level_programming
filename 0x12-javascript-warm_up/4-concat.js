#!/usr/bin/node

const args = process.argv.slice(2);
const argOne = args[0];
const argTwo = args[1];

if (argOne === undefined && argTwo === undefined) {
  console.log('undefined' + ' ' + 'is' + ' ' + 'undefined');
} else {
  console.log(argOne + ' ' + 'is' + ' ' + argTwo);
}
