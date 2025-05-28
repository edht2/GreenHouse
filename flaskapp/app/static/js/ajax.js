
const server_status = 0;
const server_response = [1,1,1];

function callServer(x, y) {


    console.log("callServer engaged. ")
    x = 5
    y = 6
    let data = ('x:' + x + ', ' + 'y:' + y)
    console.log("callServer engaged. " + data)
    
    const requestXML = new XMLHttpRequest(), method = 'GET', url = '/greenhouse_ajax';
    requestXML.open(method, url, true);
    
    
    
    requestXML.onreadystatechange = function () {
        console.log("request.readyState: " + requestXML.readyState);
        if(requestXML.readyState === XMLHttpRequest.DONE)
        {
            var status = requestXML.status;
            var server_status = status
            console.log('requestXML.status is... ' + server_status)
            if (status === 0 || (status >= 200 && status < 400)) {
                //The request has been completed successfully
                //console.log("The request has been completed successfully: " + requestXML.responseText);
                var val=requestXML.responseText;
                //spin.text.setText(val);
                console.log('value unparsed by JSON = ' + val);
                //spin.text.data.set('icons', JSON.parse(val));
                let server_response = JSON.parse(val);
                let cz1_temp = server_response.cz1_temp;
                console.log('value parsed by JSON = ' + cz1_temp);
                cz1_temp = server_response.cz1_temp + '°C';
                let cz1_temp_div = document.getElementById("cz1_temp");
                cz1_temp_div.innerHTML = cz1_temp;

                let cz1_rh = server_response.cz1_rh + '%';
                let cz1_rh_div = document.getElementById("cz1_rh");
                cz1_rh_div.innerHTML = cz1_rh;

                let cz1_bed1 = server_response.cz1_bed1 + '%';
                let cz1_bed1_div = document.getElementById("cz1_bed1");
                cz1_bed1_div.innerHTML = cz1_bed1;

                let cz1_bed2 = server_response.cz1_bed2 + '%';
                let cz1_bed2_div = document.getElementById("cz1_bed2");
                cz1_bed2_div.innerHTML = cz1_bed2;

                let cz1_bed3 = server_response.cz1_bed3 + '%';
                let cz1_bed3_div = document.getElementById("cz1_bed3");
                cz1_bed3_div.innerHTML = cz1_bed3;




                let cz2_temp = server_response.cz2_temp + '°C';
                let cz2_temp_div = document.getElementById("cz2_temp");
                cz2_temp_div.innerHTML = cz2_temp;

                let cz2_rh = server_response.cz2_rh + '%';
                let cz2_rh_div = document.getElementById("cz2_rh");
                cz2_rh_div.innerHTML = cz2_rh;        
                
                let cz2_bed4 = server_response.cz2_bed4 + '%';
                let cz2_bed4_div = document.getElementById("cz2_bed4");
                cz2_bed4_div.innerHTML = cz2_bed4;

                let cz2_bed5 = server_response.cz2_bed5 + '%';
                let cz2_bed5_div = document.getElementById("cz2_bed5");
                cz2_bed5_div.innerHTML = cz2_bed5;

                let cz2_bed6 = server_response.cz2_bed6 + '%';
                let cz2_bed6_div = document.getElementById("cz2_bed6");
                cz2_bed6_div.innerHTML = cz2_bed6;

                let cz2_bed7 = server_response.cz2_bed7 + '%';
                let cz2_bed7_div = document.getElementById("cz2_bed7");
                cz2_bed7_div.innerHTML = cz2_bed7;

                let cz2_bed8 = server_response.cz2_bed8 + '%';
                let cz2_bed8_div = document.getElementById("cz2_bed8");
                cz2_bed8_div.innerHTML = cz2_bed8;
                
            } else {
                // Oh no! There has been an error with the request!
            }
        }
    };  
    



    console.log("sending data to python server on 127.0.0.1")
    requestXML.send();  
    
    
    }
    


    
    
    function call_back() {
        console.log('This is a callback function on timer...' );
    }

    setInterval(callServer, 3000); // Call the async function


    