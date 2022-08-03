#!/usr/bin/node
function second(arr){
    let max=0, secondmax = 0
    for (x of arr){
        if (x > maxx){
            secondmax = max
            max = x
        }
    }
    for (j of arr){
        if(j>secondmax && j<max){
            secondmax =   j
        }
    }
    return secondmax;
}
console.log(second(arr));