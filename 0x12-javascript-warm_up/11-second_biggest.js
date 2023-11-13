#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const num = args.length;

if (num < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  const secondLargest = args[1];
  console.log(secondLargest);
}
