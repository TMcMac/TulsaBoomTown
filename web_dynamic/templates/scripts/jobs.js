let local = [];
let remote = [];

$(document).ready(function () {

  $('button.local').click(function () {
    populate_local();
  });

  $('button.remote').click(function () {
    populate_remote();
  });

  $.ajax({
    url: 'https://tulsaboomtown.tech/api/jobs',
    type: 'GET',
    success: function (data) {
      sanitize(data);
      populate_local();
    },
    error: function () {
      failure();
    }
  });

});

function populate_remote () {
  let i;
  const out = $('div.job-display');
  out.empty();
  if (!remote) {
    out.append('<p>No remote jobs available.</p>');
  } else {
    out.append('<h2 class="centered">Remote</h2>');
  }
  for (i = 0; i < remote.length; i++) {
    const card = remote[i];
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

function populate_local () {
  let i;
  const out = $('div.job-display');
  out.empty();
  if (!local) {
    out.append('<p>No local jobs available.</p>');
  } else {
    out.append('<h2 class="centered">Local</h2>');
  }
  for (i = 0; i < local.length; i++) {
    const card = local[i];
    let inner = `<div class='slide-content'><h3 class='slide-title'>${card[0]}</h3>`;
    inner += `<p><strong>Company: </strong>${card[1]}</p>`;
    inner += `<p><strong>Location: </strong>${card[2]}</p>`;
    inner += `<p><a href='${card[3]}'><strong>Apply Now!</strong></a></p></div>`;
    out.append(inner);
  }
}

function sanitize (data) {
  let card;
  let i;

  let temp = data.remote;
  for (i = 0; i < temp.length; i++) {
    card = [];
    card[0] = temp[i].title;
    card[1] = temp[i].company_name;
    card[2] = temp[i].job_type;
    card[3] = temp[i].category;
    card[4] = temp[i].candidate_required_location;
    card[5] = temp[i].publication_date;
    card[6] = temp[i].url;

    if (!card[0])
      card[0] = "Employee";
    if (card[2])
      card[2] = card[2].replace("_", " ");
    if (card[5]) {
      card[5] = card[5].slice(5, 7) + "/" + card[5].slice(8, 10) + "/" + card[5].slice(0, 4);
    }
    remote[i] = card;
  }

  temp = data.local;
  for (i = 0; i < temp.length; i++) {
    card = [];
    card[0] = temp[i].title;
    card[1] = temp[i].company;
    card[2] = temp[i].location;
    card[3] = temp[i].job_link;
    local[i] = card;
  }
}

function failure () {
  local = null;
  remote = null;
  populate_local();
}
