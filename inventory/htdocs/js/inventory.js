function init_inventory(title, url) {
    $(".inventory-create").click(function() {
        prewikka_widget({
            url: url,
            dialog: {
                title: title
            }
        });
    });
};
