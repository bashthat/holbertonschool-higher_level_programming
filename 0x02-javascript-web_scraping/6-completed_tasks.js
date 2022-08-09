#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
// handling the argument
const url = process.arv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } // error handling
  const tasksathand = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (task.userId in tasksathand) {
        tasksathand[task.userId] += 1;
      } else {
        tasksathand[task.userId] = 1;
      }
    }
  }
  console.log(tasksathand);
});
