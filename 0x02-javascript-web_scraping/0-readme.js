#!/usr/bin/node
/* https://www.tutorialspoint.com/
how-to-read-and-write-a-file-using-javascript */
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
