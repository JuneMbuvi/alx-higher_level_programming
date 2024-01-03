#!/usr/bin/node

const request = require('request');

const[url] = process.argv.slice(2);

if (!url) {
	console.error('Usage: node script.js <URL>');
	process.exit(1);
}

//make a get request & check the status code
request.get(url, (error, response) => {
	if (error) {
		console.error('Error:', error.message);
	} else {
		console.log(`code: ${response.statusCode}`);
	}
});
