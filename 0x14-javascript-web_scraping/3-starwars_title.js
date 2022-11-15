#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2] + '/';

request(url, function (error, response, body) {
  if (error === null) {
    const rbody = JSON.parse(body);
    console.log(rbody.title);
  } else {
    console.log(error);
  }
});
