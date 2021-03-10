let display = {};

$(document).ready(function () {

  $.get('https://tulsaboomtown.tech/companies', function (data) {

    display = data;

  });

});

$(document).ajaxStop(function () {

  console.log(display);

});
