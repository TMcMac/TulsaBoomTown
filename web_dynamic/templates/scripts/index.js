$(document).ready(function () {

  $.get('https://tulsaboomtown.tech/status', function (data) {

    if (data.status === 'OK') {
      console.log('API IS WORKING');
    } else {
      console.log('Doesnt work');
    }

  });

});
