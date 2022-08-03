#!/usr/bin/node
/*  class square extends */
const Rectangle = require('./4-rectangle');
// https://googlechrome.github.io/samples/classes-es6/index.html
// class Square extends Rectangle {
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
