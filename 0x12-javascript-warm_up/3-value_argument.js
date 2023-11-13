#!/usr/bin/node

const args = process.argv.slice(2);
const argOne = args[0];

if (argOne === undefined) {
  console.log('No argument');
} else {
  console.log(argOne);
}
