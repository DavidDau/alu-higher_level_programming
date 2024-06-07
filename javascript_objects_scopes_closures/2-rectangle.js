#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      // initialize instance attributes if w and h are positive integers
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if w and h is not a positive integer
      Object.create(null);
    }
  }
}
module.exports = Rectangle;
