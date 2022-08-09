#!/usr/bin/node
// borrowing patterns of thought from previous exercises
// count requests
// counst fs

const fs = require('fs');
// const url = process.argv[2];
// const count = process.argv[3];
const request = require('request');
//request.get('http://loripsum.net/api', function (error, response, body) {
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(process.argv[3], body, (error) => {
    if (error) {
      console.log(error);
 // Print the google web page.
  }});
});
// write file
//request(url, function (err, response, bod) {
//  if (err) {
//    console.log(err);
//  } else {
  // error handling
  // handling arguments

//    fs.writeFile(count, bod, 'utf8', function (err) {
//      if (err) {
//        console.log(err);
//      }
//    });
//  } // error handling
//}
//); 
