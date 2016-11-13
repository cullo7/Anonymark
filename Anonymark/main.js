function decryptor(url, file_str) {
    var canvas = document.createElement("canvas");
    var ctx = canvas.getContext("2d");
    var key_canvas = document.createElement("canvas");
    var key_ctx = key_canvas.getContext("2d");
    var image = new Image();
    var key_img = new Image();
    key_img.src = file_str;
        var message = "";
    image.onload = function () {
        ctx.drawImage(image, 0, 0);
        key_ctx.drawImage(key_img, 0, 0);
        // desaturation colors
        var imgData = ctx.getImageData(0, 0, image.width, image.height);
        var data = imgData.data;
        var key_data = (key_ctx.getImageData(0, 0, key_img.width, key_img.height)).data;
        var num = 0;
        console.log(data.length)
        for (var i = 0; i < data.length/100; i += 4) {
            num = 0;
            console.log(i)
            console.log(data[i]+" "+data[i+1]+" "+data[i+2])
            console.log(key_data[i]+" "+key_data[i+1]+" "+key_data[i+2])
            console.log("\n")
            num += Math.abs(data[i] - key_data[i])*100;
            num += Math.abs(data[i + 1] - key_data[i + 1])*10;
            num += Math.abs(data[i + 2] - key_data[i + 2]);
            message += String.fromCharCode(num);
            //console.log(data[i],'~~~~~~~' ,key_data[i]);
            console.log(num);
            if (num == 46) {
                break;
            }
        }
        //console.log(message);
    }
    image.crossOrigin = "anonymous";
    image.src = url;
    document.getElementById('decoded').innerHTML = message;
}
