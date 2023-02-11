function displayRunConf() {
    $.ajax({
        type: "POST",
        url: "/routerrunconf",
        data: {"command" : "show running-config"},
    })
}