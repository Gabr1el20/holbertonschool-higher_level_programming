$('#add_item').click(() => {
    $('<li></li>').text('Item').appendTo('.my_list');
})

/* Another version
$('#add_item').click(() => {
    $('.my_list').append('<li>Item</li>')
})
*/