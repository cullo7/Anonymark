var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

var image = new Image();
image.onload = function () {
    ctx.drawImage(image, 0, 0);

    // desaturation colors
    var imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    var data = imgData.data;

    for (var i = 0; i < data.length; i += 4) {
			console.log(data[i])
      console.log(data[i+1])
      console.log(data[i+2])
      console.log(data[i+3])
    }

    // write the modified image data
    ctx.putImageData(imgData, 0, 0);

}
image.crossOrigin = "anonymous";
image.src = "https://dl.dropboxusercontent.com/u/139992952/stackoverflow/colorhouse.png";
