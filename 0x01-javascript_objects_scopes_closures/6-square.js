#!/usr/bin/node
// https://www.geeksforgeeks.org/program-print-rectangle-pattern/
const lastsquare = require('./5-square');
module.exports = class Square extends lastsquare {
  charPrint (c) { // charPrint(c) to print a square
    if (!c) {
      c = 'X';
    } // defining the square character
    // printing the square given parameters
    let acc;
    for (let x = 0; x < this.height; x++) {
      acc = '';
      for (let y = 0; y < this.width; y++) {
        acc += c;
      } // printing the square
      console.log(acc);
    }
  }
};
