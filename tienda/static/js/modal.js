
$(document).ready(function() {
    $('.add-to-cart-btn').click(function() {
        var productoId = $(this).data('producto-id');
        
        $.ajax({
            type: 'POST',
            url: '/agregar_producto/' + productoId + '/',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                $('#exampleModal').modal('show');
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
