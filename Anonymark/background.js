function getClickHandler() {
    return function(info) {
        var url = 'display.html#' + info.srcUrl;
        chrome.tabs.create({url: url});
        renderImage(info);
    };
};
chrome.contextMenus.create({
    "title" : "Decrypt Image",
    "type" : "normal",
    "contexts" : ["image"],
    "onclick" : getClickHandler()
});
