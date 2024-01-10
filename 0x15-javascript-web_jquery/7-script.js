$(function () {
  $('#character').on('click', function () {
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
      $('#character').text('Character Name: ' + data.name);
    });
  });
});
