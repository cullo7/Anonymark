from PIL import Image
import io
import sys

message = "Aiden Cullo Brevi manu."
l = len(message)
im = Image.open(sys.argv[1])
pixelMap = im.load()
print(im.size[0])
print(im.size[1])
img = Image.new(im.mode, im.size)
pixelsNew = img.load()
c = 0
for j in range(im.size[1]):
    for i in range(im.size[0]):
        print(i , ' ' , j ,' ' , pixelMap[i,j])
        print('\n')
