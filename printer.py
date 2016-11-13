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
for i in range(104):
    for j in range(1):
        print(pixelMap[i,j])
        print(im.palette.palette[pixelMap[i,j]*len(im.mode)])
        print(im.palette.palette[pixelMap[i,j]*len(im.mode)+1])
        print(im.palette.palette[pixelMap[i,j]*len(im.mode)+2])
        print('\n')

print(im.palette.palette)
