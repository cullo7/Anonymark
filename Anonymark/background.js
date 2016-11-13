function getClickHandler() {
    return function(info) {
        var url = 'display.html#' + info.srcUrl;
        chrome.tabs.create({url: url});
        renderImage(info);
    };
};
function decrypt(url) {
    $.ajax({
        type: "POST",
        url: "../main.py",
        data: {param: url}
    }).done(function ( o ) {
    });
}
chrome.contextMenus.create({
    "title" : "Decrypt Image",
    "type" : "normal",
    "contexts" : ["image"],
    "onclick" : getClickHandler()
});


var uploadUrl = 'https://www.example.com/uploads';
/* Creates an `input[type="file]` */
var fileChooser = document.createElement('input');
fileChooser.type = 'file';
fileChooser.addEventListener('change', function () {
    var file = fileChooser.files[0];
    var formData = new FormData();
    formData.append(file.name, file);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', uploadUrl, true);
    xhr.addEventListener('readystatechange', function (evt) {
        console.log('ReadyState: ' + xhr.readyState,
            'Status: ' + xhr.status);
    });

    xhr.send(formData);
    form.reset();   // <-- Resets the input so we do get a `change` event,
    //     even if the user chooses the same file
//~~~~~~~~~~~~~ me ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    var url = window.location.href;
    url = url.substring(url.indexOf('#') + 1);
    renderImage(url);
//~~~~~~~~~~~ end me ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
});

/* Wrap it in a form for resetting */
var form = document.createElement('form');
form.appendChild(fileChooser);

/* Listen for messages from popup */
chrome.runtime.onMessage.addListener(function (msg) {
    if (msg.action === 'browseAndUpload') {
        fileChooser.click();
    }
});
