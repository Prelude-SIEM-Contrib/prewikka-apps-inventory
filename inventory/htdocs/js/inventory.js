$(document).on("click", "button.create", function() {
    $("div#inventory-dialog").last().dialog({
        "buttons": [{
            "class": 'btn btn-default',
            "text": "OK",
            "click": function() {
                $(this).find("form").submit();
            }
        }]
    });
});
