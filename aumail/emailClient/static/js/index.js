$(document).ready(function() {

    // Used for getting all the emails from the emails json
    get_emails();

    // 10 seconds interval for refreshing new emails
    setInterval(function () {
        // Used for verifying new recieved emails in the emails json
        get_emails();
    }, 10000);

    // Used for multiple checkboxing all the emails
    $("#functionality #checkall").live("click", function(){
        if($(this).is(":checked")) {
            $("#emails .email").addClass("selected");
            $("#emails input").prop("checked", true);
        } else {
            $("#emails .email").removeClass("selected");
            $("#emails input").prop("checked", false);
        }
    });

    // Used for adding background color on email checkbox activate
    $('#emails .email .click_me').live('click', function() {
        var email = $(this).parent().parent();
        if($(this).is(":checked")) {
            email.addClass("selected");
        } else {
            email.removeClass('selected');
        }
    });
});
