function loadScript(url, callback) {
    // Adding the script tag to the head as suggested before
    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;
    // Then bind the event to the callback function.
    // There are several events for cross browser compatibility.
    script.onreadystatechange = callback;
    script.onload = callback;
    // Fire the loading
    head.appendChild(script);
}
function decrypt() { // call encryption JS here
    var encrypted_url = window.location.href;
    encrypted_url = url.substring(url.indexOf('#') + 1);
    img_decrypt(url, fileChooser.files[0]); // pass to other JS file
}
var script_load = function() {
    decrypt("Hello!");
};
/* Creates an `input[type="file]` */
var fileChooser = document.createElement('input');
// var file;
fileChooser.type = 'file';
fileChooser.addEventListener('change', function () {
    // var file = fileChooser.files[0];
    loadScript('resources/encrypt.js', script_load); // laod auxilary JS file
    // var reader = new FileReader();
    // reader.onloadend = function () {
    //     image_str = reader.result;
    //     loadScript('resources/encrypt.js', script_load);
    // }
    // reader.readAsDataURL(file);

    // var img = document.getElementById("hash");
    // img.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzK4Lu0EoLHfQFlkDWCLhppwbrx6dCXGsh0_6Lv4mdR-vM1IdavA";
    // var div = document.getElementById("decoded");
    // div.innerHTML = "test";
});
/* Wrap it in a form for resetting */
// var form = document.createElement('form');       Maybe these two lines are not needed
// form.appendChild(fileChooser);
/* Listen for messages from popup */
chrome.runtime.onMessage.addListener(function (msg) {
    if (msg.action === 'browseAndUpload') {
        fileChooser.click();
    }
});
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('button').addEventListener('click', function () {
        chrome.runtime.sendMessage({ action: 'browseAndUpload' });
    });
});

function renderImage(url) {
    img = document.getElementById('hash');
    img.src = url;
}
// function getClickHandler() {
//     return function(info, tab) {
//         var url = 'display.html#' + info.srcUrl;
//         chrome.tabs.create({url: url});
//     };
// };
// chrome.contextMenus.create({
//     "title" : "Decrypt Image",
//     "type" : "normal",
//     "contexts" : ["image"],
//     "onclick" : getClickHandler()
// });
var clickHandler = function(info, tab) {
        var url = 'display.html#' + info.srcUrl;
        chrome.tabs.create({url: url});
}
chrome.contextMenus.create({
    "title": "Decrypt image",
    "contexts": ["image"]
});
// Must be synchronously called on event page load,
//   for instance in the top level code
chrome.contextMenus.onClicked.addListener(clickHandler);
