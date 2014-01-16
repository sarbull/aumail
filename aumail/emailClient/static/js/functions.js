function refresh_emails() {
    $.get("/email/emailList", function(data, status){
        for(var i = 0; i < data["emails"].length; i++) {
            if(data[i].new == true){
                $("#emails").prepend(' \
                    <div class="email" data-id="'+ i +'"> \
                        <span class="checkbox"><input type="checkbox" name="email1" id="email1" class="click_me" value="0"></span> \
                        <span class="subject"><a href="">' + data["emails"][i].email + '</a></span><span class="email_sender">' + data["emails"][i].sender + '</span> \
                        <span class="date_recieved">' + data["emails"][i].date_recieved + '</span> \
                        <br style="clear:both;"> \
                    </div> \
                ');
                // if(data["emails"][i].read == true) {
                //     var email = $("#emails").find("div[data-id='" + i + "']");
                //     email.children(".subject").addClass("read");
                // }
            }

        }
    }, 'json');
}

function get_emails() {
    $.get("/email/emailList", function(data, status){
        $("#emails").html("");
        for(var i = 0; i < data["emails"].length; i++) {
            $("#emails").append(' \
                <div class="email" data-id="'+ i +'"> \
                    <span class="checkbox"><input type="checkbox" name="email1" id="email1" class="click_me" value="0"></span> \
                    <span class="subject"><a href="/readmail/?id_email='+ data['emails'][i].id_email + '">' + data["emails"][i].subject + '</a></span><span class="email_sender">' + data["emails"][i].sender + '</span> \
                    <span class="date_recieved">' + data["emails"][i].date_recieved + '</span> \
                    <br style="clear:both;"> \
                </div> \
            ');
            // if(data[i].read == true) {
            //     var email = $("#emails").find("div[data-id='" + i + "']");
            //     email.children(".subject").addClass("read");
            // }
        }
    }, 'json');
}

function get_contacts() {
    $.get("/agendajson", function(data, status){
        $("#contacts").html("");
        for(var i = 0; i < data.length; i++) {
            $("#contacts").append(' \
                <div class="contact" data-id="'+ i +'"> \
                    <span class="checkbox"><input type="checkbox" name="contact1"></span> \
                    <div class="contactinfo"> \
                        <span class="name"><a href="contact-list.html?id='+ i +'">' + data[i]['fields'].name + '</a></span> \
                        <span class="email">' + data[i]['fields'].email + '</span> \
                    </div> \
                    <br style="clear:both;"> \
                </div> \
            ');
        }
    }, 'json');
}
