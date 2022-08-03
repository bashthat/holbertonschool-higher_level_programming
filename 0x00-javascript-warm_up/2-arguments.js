#!/usr/bin/node
// utilizing argv and nested loops.
if (process.argv.length === 2) {
	console.log('No arguemnt');
} else if (process.argv.length === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}

