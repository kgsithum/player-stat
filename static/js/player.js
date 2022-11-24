
$(document).on('submit', '#add-player', function(e){
    e.preventDefault();
    
    $.ajax({
        type: "POST",
        url: '/create/',
        data: {
            firstname: $('#firstname').val(),
            lastname: $('#lastname').val(),
            email: $('#email').val(),
            dateofbirth: $('#dateofbirth').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            isactive: $('#isactive').is(':checked')
        },
        success: function(response) {
            $('#message').addClass('alert-success');
            $('#message').html(response);
            $('#message').removeClass('d-none');
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(errorThrown);
            $('#message').addClass('alert-danger');
            $('#message').html('Something went wrong');
            $('#message').removeClass('d-none');
         }
      });
});

function loadPlayer(id) {
    $.ajax({
        url: '/player/get-player/',
        data: { id: id},
        success: function(response) {
            $('#player-data').html(response);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            $('#player-data').html('<div class="alert alert-danger" role="alert">' + errorThrown + '</div>');
         }
      });
}
