#!/usr/bin/node
exports.logMe = function (item) {
  if (!this.count) {
    // Initialize the count if it doesn't exist
    this.count = 0;
  }
  console.log(`${this.count}: ${item}`);
  this.count++;
};
