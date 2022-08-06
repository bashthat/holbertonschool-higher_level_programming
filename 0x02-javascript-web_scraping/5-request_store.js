#!/usr/bin/node
// borrowing patterns of thought from previous exercises
// count requests
// counst fs
const request = require('request');
// write file
request.get(process.argv[2], function (err, response, bod) {
  if (err) {
    console.log(err);
  } // error handling
  // handling arguments
  const taskfunction = {};
  for (const task of JSON.parse(bod)) {
    if (task.completed === true) {
      if (task.Id in taskfunction) {
        taskfunction[task.Id] += 1;
      } else { // parse and complete task
        taskfunction[task.Id] = 1;
      } // end if else
    } // creating object with completed tasks
  }
  console.log(taskfunction);
}); // word
