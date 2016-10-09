$(function () {
    $('#jaxInput').on('keyup', function () {
        var jaxValue = $('#jaxInput').val();

        jaxValue = jaxValue.replace(/(?:\r\n|\r|\n)/g, '<br>');

        $('.renderJax').html(jaxValue);
        MathJax.Hub.queue.Push(["Typeset", MathJax.Hub, "renderJax"]);
    });

    var hostname = window.location.hostname;

    $("#createBin").click(function () {
        var binData = $('#jaxInput').val();

        if (binData.length < 1) {
            // Ignore empty bin creation
            return;
        }

        $.ajax({
            type: "POST",
            url: "/create_bin",
            data: {
                "binData": binData
            },

            success: function (data) {
                $("#binLink").html("Bin Created: <a target='_blank' href='/" + data + "'>http://" + hostname + "/" + data + "</a>");
            },

            error: function () {
                $("#binLink").html("An error occurred while saving your bin.");
            }
        });
    });
});
