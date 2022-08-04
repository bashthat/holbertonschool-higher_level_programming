#!/usr/bin/node
// utilizing argv and nested loops.
const char = process.argv;
const argslen = char.length;
// handling the cases of the arguments
if (argslen === 2) {
  console.log('No argument');
} else if (argslen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
