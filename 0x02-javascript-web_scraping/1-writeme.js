#!/usr/bin/node
/* https://www.codegrepper.com/code-examples/javascript/
javascript+write+to+text+file
https://www.tabnine.com/code/javascript/functions/fs/writeFile
*/
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3],
  function (error) {
    if (error) {
      console.log(error);
    }
  }); // word
