function fetchTitle() {
    var url = $("#id_url").val();
    
    if (!url) {
        alert("Please enter a valid url.");
        $("#id_url").focus();
        return;
    }
    
    $("#fetch_button").button('loading');
    $.ajax({
        url: '/bookmarks/fetchtitle?url=' + url, 
        timeout: 5000, 
        success: function(data) {
            $("#id_title").val(data);
        }, 
        complete: function(jqXHR, textStatus) {
            $("#fetch_button").button('reset');
        } 
    });
}
