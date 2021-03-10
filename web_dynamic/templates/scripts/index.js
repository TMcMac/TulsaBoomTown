$(document).ready(function () {

  $.ajax({
    url: 'https://tulsaboomtown.tech/companies',
    type: 'GET',
    success: function (data) {
      populate(data);
    },
    error: function () {
      failure();
    }
  });

});

function populate (data) {
  let i;
  console.log('Company names in our database:');

  for (i = 0; i < data.length; i++) {
    console.log(data[i].name);
  }
}

function failure () {
  console.log('No company data found.');
}
