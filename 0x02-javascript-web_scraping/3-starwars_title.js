#!/usr/bin/node

// #!/bin/bash
// while read LINE; do
// curl -o /dev/null --silent --head --write-out
// "%{http_code} $LINE\n" "$LINE"
// done < url-list.txt

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
// request.get('/api/films/', functions);
request.get(url + process.argv[2], function (error, response, body) {
// handling error responses
  if (error) {
    console.error('error:', error);
  } else {
    console.log(JSON.parse(body).title);
  }
}); // word
