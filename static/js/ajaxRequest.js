$(document).ready(function() {
    $('#agregar-viatico').click(function() {
        $.ajax({
            url: "{% url 'empleado:agregarViatico'  idEvento=evento.id %}",
            type: 'POST',
            dataType: 'json',
            success: function(data) {
                // Maneja la respuesta JSON aquí
                // ...
            },
            error: function(xhr, textStatus, error) {
                // Maneja los errores aquí
                // ...
            }
        });
    });
});