#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter for occurences
  let count = 0;
  // Iterate though the list
  for (const element of list) {
    if (element === searchElement) {
      // Increment the count if the element matches the search element
      count++;
    }
  }

  return count;
};
