#!/usr/bin/node
/* working on the module.exports methods */
module.exports = class Rectangle {
  constructor (w, h) {
    // this.width = w;
    // this.height = h;
    if (!w || !h) {
      return;
    }
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }
};
