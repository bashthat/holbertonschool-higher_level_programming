#!/usr/bin/node
// first argument is integer
if (!parseInt(process.argv[2])) {
console.log ("Not a number");
} else {
console.log ("My number: %d", parseInt(process.argv[2]));
}