#!/usr/bin/node
// printing a square
const square = process.argv[2];
if (isNaN(square)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < square; x++) {
    console.log('X'.repeat(square));
  }
}
