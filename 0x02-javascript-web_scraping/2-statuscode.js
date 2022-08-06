#!/usr/bin/node
// utilizing the request function
const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log('code: ' + response.statusCode);
});