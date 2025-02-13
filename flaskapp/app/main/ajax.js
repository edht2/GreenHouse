
const server_status = 0;
const server_response = [1,1,1];

function callServer(x, y) {


    console.log("callServer engaged. ")
    
    let data = ('x:' + x + ', ' + 'y:' + y)
    console.log("callServer engaged. " + data)
    
    const requestXML = new XMLHttpRequest(), method = 'GET', url = '/slots/'+data;
    requestXML.open(method, url, true);
    
    
    
    requestXML.onreadystatechange = function () {
        console.log("request.readyState: " + requestXML.readyState);
        if(requestXML.readyState === XMLHttpRequest.DONE)
        {
            var status = requestXML.status;
            server_status = status
            console.log('requestXML.status is... ' + server_status)
            if (status === 0 || (status >= 200 && status < 400)) {
                //The request has been completed successfully
                console.log("The request has been completed successfully: " + requestXML.responseText);
                var val=requestXML.responseText;
                //spin.text.setText(val);
                console.log('value unparsed by JSON = ' + val);
                //spin.text.data.set('icons', JSON.parse(val));
                server_response = JSON.parse(val);
                //console.log('value parsed by JSON = ' + server_response[2]);
                //console.log('first reel = ' + spin.text.data.values.icons[0]);
                //console.log('second reel = ' + spin.text.data.values.icons[1]);
                //console.log('third reel = ' + spin.text.data.values.icons[2]);
                
            } else {
                // Oh no! There has been an error with the request!
            }
        }
    };  
    
    console.log("sending data to python server on 127.0.0.1")
    requestXML.send();  
    
    
    }
    


    
    
    function call_back() {
        console.log('This is a callback function on timer...' + game.time.now);
    }
    