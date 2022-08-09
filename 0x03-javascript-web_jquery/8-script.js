// fetch titles and list --> swapi-api.hbtn.io/api/films/
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, stats) {
  if (stats === 'success') {
    const titles = data.results;
    for (const xyz in titles) {
      $('UL.my_list').append('<li>' + titles[xyz].title + '</li>');
    }
  }
}); // list of titles
