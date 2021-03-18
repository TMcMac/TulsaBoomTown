let index = -1;
let limit;
$(document).ready(function () {

  $('button.right').click(function () {
    move_index(1);
  });

  $('button.left').click(function () {
    move_index(-1);
  });

  $.ajax({
    url: 'https://tulsaboomtown.tech/api/companies',
    type: 'GET',
    success: function (data) {
      populate(data);
      move_index(1);
    },
    error: function () {
      failure();
    }
  });

});

function move_index (offset) {
  const prev = $('ul.slides li')[index];
  index = index + offset;
  if (index === -1) {
    index = limit;
  } else if (index === limit + 1) {
    index = 0;
  }
  const next = $('ul.slides li')[index];
  $(prev).addClass('exit');
  $(next).addClass('enter');
  $(prev).removeClass('enter');
  $(prev).removeClass('exit');
}

function populate (data) {
  let i;
  const out = $('ul.slides');
  out.empty();
  limit = data.length - 1;
  for (i = 0; i < data.length; i++) {
    const card = sanitize(data[i]);
    let inner = `<li class='slide'><div class='slide-content'><h2 class='slide-title'>${card[0]}</h2>`;
    inner += `<p class='industries'><strong>Industry: </strong>${card[1]}</p>`;
    if (card[2])
      inner += `<p class='tech-stack'><strong>Tech Stack: </strong>${card[2]}</p>`;
    if (card[3])
      inner += `<p class='employees'><strong>Number of Employees: </strong>${card[3]}</p>`;
    inner += `<p class='co-link'><strong>Website: </strong><a href='${card[4]}'>${card[4]}</a></p>`;
    if (card[5])
      inner += `<p class='job-link'><strong>Job Board Link: </strong><a href='${card[5]}'>${card[5]}</a></p></div>`;
    inner += `<p class='company-logo'><img src='images/logos/${card[6]}' alt='${card[0]} Logo'></p></li>`;
    out.append(inner);
  }
}

function sanitize (data) {
  const out = [];
  out[0] = data.name;
  out[1] = data.industries;
  out[2] = data.tech_stack;
  out[3] = data.employee_count;
  out[4] = data.website;
  out[5] = data.jobs_board;
  out[6] = data.logo_file;

  return out;
}

function failure () {
  console.log('No company data found.');
}
