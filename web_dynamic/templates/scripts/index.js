$(document).ready(function () {

  $.get('/api/v1/status/', function (data) {

    if (data.status === 'OK') {
      console.log('API IS WORKING');
    } else {
      console.log('Doesnt work');
    }

  });

});
