$(document).ready(function () {

  $.ajax({
    url: 'https://tulsaboomtown.tech/api/jobs',
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
  const out = $('div.job-display');
  out.empty();
  for (i = 0; i < data.length; i++) {
    console.log(data[i]);
    let inner = `<div class='slide-content'><h3 class='slide-title'>${data[i].title}</h3>`;
    inner += `<p><strong>Company: </strong>${data[i].company_name}</p>`;
    inner += `<p><strong>Job Type: </strong>${data[i].job_type}</p>`;
    inner += `<p><strong>Job Category: </strong>${data[i].category}</p>`;
    inner += `<p><strong>Job Location: </strong>${data[i].candidate_required_location}</p>`;
    inner += `<p><strong>Publication Date: </strong>${data[i].publication_date}</p>`;
    inner += `<p><a href='${data[i].url}'><strong>Apply Now!</strong></a></p></div>`;
    out.append(inner);
  }
}

function failure () {
  console.log('No job data found.');
}
