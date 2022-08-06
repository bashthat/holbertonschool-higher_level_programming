#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
// let url = 'https://swapi.co/api/people/';
request(url, function (e, response, body) {
  if (e) {
    console.error('error:', e);
  } // handle JSON stringify error
  const data = JSON.parse(body).results;
  for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].characters.length; j++) {
      if (data[i].characters[j].includes('18')) {
        count++;
      } // end request
    } // end for loop
  }
  console.log(count);
}); // word
