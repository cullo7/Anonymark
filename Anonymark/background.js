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


var uploadUrl = window.location.href
/* Creates an `input[type="file]` */
var fileChooser = document.createElement('input');
fileChooser.type = 'file';
fileChooser.addEventListener('change', function () {
    var file = fileChooser.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        console.log(reader.result);
        renderImage(reader.result);
    }
    reader.readAsDataURL(file);
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
