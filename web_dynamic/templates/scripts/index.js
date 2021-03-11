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
  const out = $('ul.slides');
  out.empty();
  for (i = 0; i < data.length; i++) {
    let inner = `<li class='slide'><div class='slide-content'><h2 class='slide-title'>${data[i].name}</h2>`;
    inner += `<p class='industries'><strong>Industry: </strong>${data[i].industries}</p>`;
    inner += `<p class='tech-stack'><strong>Tech Stack: </strong>${data[i].tech_stack}</p>`;
    inner += `<p class='employees'><strong>Number of Employees: </strong>${data[i].employee_count}</p>`;
    inner += `<p class='co-link'><strong>Website: </strong><a href='${data[i].website}'>${data[i].website}</a></p>`;
    inner += `<p class='job-link'><strong>Job Board Link: </strong><a href='${data[i].jobs_board}'>${data[i].jobs_board}</a></p></div>`;
    inner += `<p class='company-logo'><img src='images/logos/${data[i].logo_file}' alt='${data[i].name} Logo'></p></li>`;
    out.append(inner);
  }
}

function failure () {
  console.log('No company data found.');
}
