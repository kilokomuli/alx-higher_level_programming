#!/usr/bin/node


const request = require('request');
const movieId = process.argv[2];
const starWarsUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(starWarsUrl, function (_err, _res, body) {
	body = JSON.parse(body);
	console.log(body.title);
});
