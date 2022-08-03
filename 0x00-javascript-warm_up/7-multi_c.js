#!/usr/bin/node
// printing C is fun
const array = process.argv[2]; {
if (isNaN(array))
    {console.log('Missing number of occurrences');
} else {
    for (let x = array; x > 0; x--) {
        console.log('C is fun');
    }
}}