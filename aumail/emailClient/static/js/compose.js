$(document).ready(function() {
    
    // Used to get contacts from contacts json object
    get_contacts();
    
    // Used for appending to reciever
    $("#contactlist button").live("click", function(){
        $("#contacts input:checked").each(function(){ 
            var email = $(this).parent().parent().find(".email");
            var to    = $("#to");
            if(to.val() == "") {
                to.val(to.val() + email.text());
            } else {
                to.val(to.val() + ", " + email.text());
            }
        });
    });
    
});