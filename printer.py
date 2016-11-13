from PIL import Image
import io
import sys

message = "Aiden Cullo Brevi manu."
l = len(message)
im = Image.open(sys.argv[1])
pixelMap = im.load()
img = Image.new(im.mode, im.size)
pixelsNew = img.load()
c = 0
for i in range(img.size[0]):
    for j in range(img.size[1]):
        print(pixelMap[i,j])
        print(im.palette.palette[pixelMap[i,j]*3])
        print(im.palette.palette[pixelMap[i,j]*3+1])
        print(im.palette.palette[pixelMap[i,j]*3+2])
        print('\n')
