function getemails() {
    $.get("json/emails.json", function(data, status){
        $("#emails").html("");
        for(var i = 0; i < data.length; i++) {
            $("#emails").append(' \
                <div class="email" data-id="'+ i +'"> \
                    <span class="checkbox"><input type="checkbox" name="email1" id="email1" class="click_me" value="0"></span> \
                    <span class="subject"><a href="">' + data[i].subject + '</a></span><span class="email_sender">' + data[i].email + '</span> \
                    <span class="date_recieved">' + data[i].date_recieved + '</span> \
                    <br style="clear:both;"> \
                </div> \
            ');
            if(data[i].read == true) {
                var email = $("#emails").find("div[data-id='" + i + "']");
                email.children(".subject").addClass("read");
            }
        }
    }, 'json');
}

$(document).ready(function() {
    setInterval(function () {
        getemails();
    }, 10000);
});
