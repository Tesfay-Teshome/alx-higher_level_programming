#!/usr/bin/node
const argv = process.argv;
const url = argv[2];
const id = '18';
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const rbody = JSON.parse(body);
    let count = 0;
    for (const i of rbody.results) {
      for (const j of i.characters) {
        if (j.search(id) > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
