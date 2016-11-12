function renderImage(url) {
    img = document.createElement('img');
    img.src = url;
    document.body.appendChild(img);
}
window.onload = function() {
    var url = window.location.href;
    url = url.substring(url.indexOf('#') + 1);
    renderImage(url);
};
