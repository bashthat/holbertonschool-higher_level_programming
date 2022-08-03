#!/usr/bin/node
/* class rectangle definition */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // print rectangle
  print () {
    let row;
    for (let i = 0; i < this.height; i++) {
      row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  // double rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }

  // rotate rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
};
