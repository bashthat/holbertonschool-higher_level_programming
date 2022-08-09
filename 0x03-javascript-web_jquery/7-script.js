// fetch name from swapi-api.hbtn.io/....
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, info) {
  if (info === 'success') {
    $('DIV#character').text(data.name);
  }
}); // word
