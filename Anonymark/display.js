document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('button').addEventListener('click', function () {
        chrome.runtime.sendMessage({ action: 'browseAndUpload' });
    });
});
function renderImage(url) {
    img = document.createElement('img');
    img.src = url;
    document.body.appendChild(img);
}
