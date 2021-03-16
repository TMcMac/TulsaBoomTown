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
    const card = sanitize(data[i]);
    let inner = `<div class='slide-content'><h3 class='slide-title'>${card[0]}</h3>`;
    if (card[1])
      inner += `<p><strong>Company: </strong>${card[1]}</p>`;
    if (card[2])
      inner += `<p><strong>Job Type: </strong>${card[2]}</p>`;
    if (card[3])
      inner += `<p><strong>Job Category: </strong>${card[3]}</p>`;
    if (card[4])
      inner += `<p><strong>Job Location: </strong>${card[4]}</p>`;
    if (card[5])
      inner += `<p><strong>Publication Date: </strong>${card[5]}</p>`;
    if (card[6])
      inner += `<p><a href='${card[6]}'><strong>Apply Now!</strong></a></p></div>`;
    out.append(inner);
  }
}

function sanitize (data) {
  const out = [];
  out[0] = data.title;
  out[1] = data.company_name;
  out[2] = data.job_type;
  out[3] = data.category;
  out[4] = data.candidate_required_location;
  out[5] = data.publication_date;
  out[6] = data.url;

  if (!out[0])
    out[0] = "Employee";
  if (out[2])
    out[2] = out[2].replace("_", " ");
  if (out[5]) {
    out[5] = out[5].slice(5, 7) + "/" + out[5].slice(8, 10) + "/" + out[5].slice(0, 4);

  return out;
  }
}

function failure () {
  console.log('No job data found.');
}
