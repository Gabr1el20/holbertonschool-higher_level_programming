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
  /* Now it's time to handle the ENTER key press event */
  $('#language_code').keypress(function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode == '13') {
      const val = $('#language_code').prop('value');
      $.get(`https://hellosalut.stefanbohacek.dev/?lang=${val}`, (data) => {
      /* What happens here is that in some languages, the response comes in html format.
              So, the solution to bring back them in a legible format is to decodified them with
              jQuery. */
        const decodifiedData = $('<div></div>').html(data.hello).text();
        $('#hello').text(decodifiedData);
      });
    }
  });
});
