from PIL import Image
import io
import sys
import math
import hashlib
import urllib.request,io
import base64

def encrypt(orig, savefile, idfk):
    im = Image.open(orig)
    pixelMap = im.load()
    proto = Image.open(idfk)
    img = Image.new(proto.mode, im.size)
    img.format = im.format
    pixelsNew = img.load()
    c = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixelsNew[i,j] =(255,255,255)  
    im.close()
    img.show()
    img.save("White.png")
    img.close()

if __name__ == "__main__":
    encrypt(sys.argv[1], sys.argv[2], sys.argv[3]);
