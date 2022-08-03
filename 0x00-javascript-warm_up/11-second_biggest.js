#!/usr/bin/node
// finding the second biggest number
function secondBiggest(arr) {
    let biggest = arr[0];
    let secondBiggest = arr[0];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > biggest) {
            secondBiggest = biggest;
            biggest = arr[i];
        } else if (arr[i] > secondBiggest) {
            secondBiggest = arr[i];
        }
    }
    return secondBiggest;
}
console.log(secondBiggest(arr));