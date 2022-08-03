#!/usr/bin/node
// finding the second biggest number
function secondBiggest(x, y) {
    return x - y; 
}
const x = parseInt(process.argv[2]);
let y = parseInt(process.argv[3]);
if (isNaN(x) || isNaN(y)) {
    console.log(1);
}