#!/usr/bin/node
// Find the second biggest number in a list
if (process.argv.length <= 3) {
  console.log(0);
} else {
  // splice to sort the array
  const arr = process.argv.splice(2);
  arr.sort(function (a, b) {
    return a - b;
  });
  // sort and return
  console.log(arr[arr.length - 2]);
}
