#!/usr/bin/node

const fs = require('fs');

const [filePath, content] = process.argv.slice(2);
if (!filePath || !content) {
  console.error('Usage: node script.js <file-path> <content>');
  process.exit(1);
}

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error('Error writing to file:', err);
  } else {
    console.log(`Content has been written to ${filePath}`);
  }
});
