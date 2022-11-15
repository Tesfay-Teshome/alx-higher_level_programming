#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const fileName = argv[2];
fs.readFile(fileName, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  process.stdout.write(data);
});
