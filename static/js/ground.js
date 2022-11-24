
$(document).on('submit', '#add-city', function(e){
    e.preventDefault();
    
    $.ajax({
        type: "POST",
        url: '/ground/create-city/',
        data: {
            name: $('#name').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
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

$(document).on('submit', '#add-ground', function(e){
    e.preventDefault();
    
    $.ajax({
        type: "POST",
        url: '/ground/create-ground/',
        data: {
            name: $('#name').val(),
            capacity: $('#capacity').val(),
            cityId: $('#cityId').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
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
