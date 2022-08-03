#!/usr/bin/node

function getsecond()
arr = []; {
    let max = arr[0];
    let max2 = arr[0];

    for (let x = 0; x < arr.length; x++) {
        if (arr[x] > max) {
            max2 = max;
            max = arr[x];
        } else if (arr[x] > max2) {
            max2 = arr[x];
        }
    }
    return max2;
}