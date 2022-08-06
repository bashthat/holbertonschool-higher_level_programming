#!/usr/bin/node
// borrowing patterns of thought from previous exercises
// count requests
// counst fs
const request = require('request');
const fs = require('fs');
// write file
request.get(process.argv[2], function (err, response, bod) {
  if (err) {
    console.log(err);
  } // error handling
  // handling arguments
  fs.write(process.argv[3], bod, 'utf8', function (err) {
    if (err) {
      console.log(err);
    } // error handling
  });
}); // word
