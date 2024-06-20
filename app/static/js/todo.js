function completed() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        window.location.href = "/todo-list";
    }
    xhttp.open("GET", window.location.href + '/completed', true); xhttp.send();
}
function post_edits() {
    // if the user clicks on the save button ↓
    var descr = document.getElementById('paragraph_edit');
    var title = document.getElementById('top_pannel_edit');
    // I get the title and description objects!

    const xhttp = new XMLHttpRequest();
    // create the ajax call object
    xhttp.onload = function () {
        window.location.reload(); 
    }
    xhttp.open(
        "POST",
        window.location.href + '/edited',
        true
    );
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xhttp.send("title=" + title.value + "&description=" + descr.value);
    // finally send the data back to the server
}; // I make the save button effective

function edit() {
    var title = document.getElementById('top_pannel');
    var edit_button = document.getElementById('edit_todo_item');
    var completed_button = document.getElementById('completed');
    var descr = document.getElementById('descr');

    title.innerHTML = '<input type="text" id="top_pannel_edit" placeholder="new title"></input>';
    descr.innerHTML = '<textarea id="paragraph_edit" placeholder="new description"></textarea>';
    // I turn the title and description elements into textboxes for editing!

    edit_button.value = "Save";
    // I change the 'edit' button to say save!
    edit_button.onclick = post_edits

    completed_button.value = "Cancel";
    // I also switch the 'completed' button to 'cancel'
    completed_button.addEventListener('click', function () {
        // if the user clicks on the save button ↓
        window.location.reload()
        // by reloading the page the data resets
    });
}