#!/usr/bin/node
// printing number of arguments already passed
let int = 0;
exports.logMe = function (xyz) {
  console.log(int + ': ' + xyz);
  int++;
};
