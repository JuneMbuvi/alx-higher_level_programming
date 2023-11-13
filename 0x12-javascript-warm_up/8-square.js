#!/usr/bin/node

const args = process.argv.slice(2);
const size = args[0];
const newInt = parseInt(size);

if (!isNaN(newInt)) {
  for (let i = 0; i < newInt; i++) {
    let Square = '';
    for (let j = 0; j < newInt; j++) {
      Square += 'X';
    }
    console.log(Square);
  }
} else {
  console.log('Missing size');
}
