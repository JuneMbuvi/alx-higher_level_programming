$(function () {
  $('#list_movies').on('click', function () {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
      const movies = data.results;

      $('#title').empty();

      $.each(movies, function (index, movie) {
        $('#title').append('<p>Title Name: ' + movie.title + '</p>');
      });
    });
  });
});
