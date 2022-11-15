#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const fileName = argv[2];
const string = argv[3];
fs.writeFile(fileName, string, 'utf-8', function (err) {
  if (err) return console.log(err);
});
