$(document).ready(function () {
  $('#btn_translate').click(() => {
    const val = $('#language_code').prop('value');

    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${val}`, (data) => {
      /* What happens here is that in some languages, the response comes in html format.
            So, the solution to bring back them in a legible format is to decodified them with
            jQuery. */
      const decodifiedData = $('<div></div>').html(data.hello).text();
      $('#hello').text(decodifiedData);
    });
  });
});
