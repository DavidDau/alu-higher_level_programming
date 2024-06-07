#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      // Initialize instance attributes if w and h are positive integers
      this.width = w;
      this.height = h;
    } else {
      // Handle the case when w or h is not a positive integer
      throw new Error('Width and height must be positive integers');
    }
  }

  print () {
    // Print the rectangle using the character 'X'
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
