from PIL import Image
import sys

im = Image.open(sys.argv[1],'r')
pix_val = list(im.getdata())

for val in pix_val:
    print(val)

