#!/usr/bin/node

const originalList = require('./100-data').list;
console.log(originalList);

const newArray = originalList.map(function (value, index) {
  return (value * index);
});

console.log(newArray);
