#!/usr/bin/node
const fs = require("fs");
const filepath = process.argv[2]; // Get the file path from command line arguments

// Read the file asynchronously
fs.readFile(filepath, "utf-8", (err, data) => {
  if (err) {
    console.error(err); // Print the error object if reading fails
  } else {
    console.log(data); // Print the file conten
  }
});
