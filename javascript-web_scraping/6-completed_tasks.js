#!/usr/bin/node
const request = require("request");
const apiUrl = process.argv[2]; // Get the API URL from command line arguments

// Make a GET request to the specified API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error object if the request fails
  } else {
    const tasks = JSON.parse(body);
    const completedTasksByUser = {};

    // Count completed tasks for each user
    tasks.forEach((task) => {
      if (task.completed) {
        if (!completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId] = 1;
        } else {
          completedTasksByUser[task.userId]++;
        }
      }
    });

    console.log(completedTasksByUser);
  }
});
