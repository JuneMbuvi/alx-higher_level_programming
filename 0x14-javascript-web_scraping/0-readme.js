#!/usr/bin/node

const fs = require('fs');

const readFile = (fp) => {
  try {
    const info = fs.readFileSync(fp, 'utf-8');
    console.log(info);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
};

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <file_path>');
} else {
  const fp = process.argv[2];
  readFile(fp);
}
