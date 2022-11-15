#!/usr/bin/node
const argv = process.argv;
const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${argv[2]}/`;

const request = require('request');

request(urlMovie, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    try {
      const rbody = JSON.parse(body);
      for (const i of rbody.characters) {
        request(i, function (errorc, responsec, bodyc) {
          if (error) {
            console.error('error:', errorc);
          } else {
            try {
              const cbody = JSON.parse(bodyc);
              console.log(cbody.name);
            } catch (error) {
              console.error('error:', error);
            }
          }
        });
      }
    } catch (err) {
      console.error('error:', err);
    }
  }
});
