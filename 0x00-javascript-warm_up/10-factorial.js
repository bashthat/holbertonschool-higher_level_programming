#!/usr/bin/node
// computing and prints factorial of a number
function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log(1);
} else {
  console.log(factorial(x));
}
