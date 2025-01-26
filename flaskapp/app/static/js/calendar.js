function saveEvent(date, input) {
    window.location.href = "/calendar/add/" + date.getDate() + "/" + (parseInt(date.getMonth())+1).toString() + "/" + date.getFullYear() + "/" + input.value;
}
function deleteEvent(date, title) {
    window.location.href = "/calendar/add/" + date.getDate() + "/" + (parseInt(date.getMonth())+1).toString() + "/" + date.getFullYear() + "/" + input.value;
}
function cancelNewEvent(originalDate, dateObj, datestr) {
    dateObj.innerHTML = originalDate;
    var removedEventListeners = dateObj.cloneNode(true);
    dateObj.parentNode.replaceChild(removedEventListeners, dateObj);

    dateObj.addEventListener('click', function(){
        addEvent(dateObj.id, datestr);
    });
}
function editEvent(date_id) {
    console.log("FGFGGFGFGF");
    const date_obj = document.getElementById(date_id);
    
    console.log(this.id);
}
function addEvent(id, strdate) {
    var date_obj = document.getElementById(id);
    const originaldate = date_obj.innerHTML;
    const sd = strdate.split("/");
    const date =  new Date(parseInt(sd[1]).toString() + "," + parseInt(sd[0]).toString() + "," + parseInt(sd[2]).toString().slice(2));

    const wrapper = document.createElement("div");
    wrapper.id = 'input_wrapper';

    // input box
    const input = document.createElement("input");
    input.className = 'event';
    input.id = 'input_box'; 

    // send button
    const send_icon = document.createElement("img");
    send_icon.src = "/static/img/icon/plus.png";
    send_icon.className = 'input_icon';
    send_icon.id = 'send';
    send_icon.addEventListener('click', function(){
        saveEvent(date, input);
    });

    // cancel button
    const cancel_icon = document.createElement("img");
    cancel_icon.src = "/static/img/icon/cancel.png"; 
    cancel_icon.className = 'input_icon';
    cancel_icon.id = 'cancel';
    cancel_icon.addEventListener('click', function(e){
        e.stopPropagation();
        cancelNewEvent(originaldate, date_obj, strdate)
    });

    wrapper.appendChild(input); wrapper.appendChild(send_icon);
    wrapper.appendChild(cancel_icon); date_obj.appendChild(wrapper);
    // add the input box with the cancel and send buttons!
    date_obj.onclick = '';
    // break the onclick
}