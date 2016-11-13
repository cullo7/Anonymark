from PIL import Image
import io
import sys
import math
import hashlib
import urllib.request,io
import base64
import os

message = "Aiden Cullo and Ethan Schoen Brevi manu"
l = len(message)

def encrypt(orig, savefile, idfk):
    im = Image.open(orig)
    pixelMap = im.load()
    proto = Image.open(idfk)
    img = Image.new(proto.mode, im.size)
    img.format = im.format
    pixelsNew = img.load()
    c = 0
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            lst = [0,0,0,0]
            print(pixelMap[j,i])
            if type(pixelMap[j,i]) ==  int:
                #print(str(im.palette.palette[pixelMap[j,i]*3])+" "+str(im.palette.palette[pixelMap[j,i]*3+1])+" "+str(im.palette.palette[pixelMap[j,i]*3+2]))
                lst[0] = im.palette.palette[pixelMap[j,i]*3]+ int(math.floor(ord(message[c%l])/100)) if im.palette.palette[pixelMap[j,i]*3] < 245 else im.palette.palette[pixelMap[j,i]*3]- int(math.floor(ord(message[c%l])/100))
                lst[1] = im.palette.palette[pixelMap[j,i]*3+1]+ int(math.floor((ord(message[c%l]) % 100)/10)) if im.palette.palette[pixelMap[j,i]*3+1] < 245 else im.palette.palette[pixelMap[j,i]*3+1]- int(math.floor((ord(message[c%l]) % 100)/10))
                lst[2] = im.palette.palette[pixelMap[j,i]*3+2]+ int(ord(message[c%l]) % 10) if im.palette.palette[pixelMap[j,i]*3+2] < 245 else im.palette.palette[pixelMap[j,i]*3+2]- int(ord(message[c%l]) % 10)
            else:
                lst[0] = pixelMap[j,i][0]+ int(math.floor(ord(message[c%l])/100)) if pixelMap[j,i][0] < 245 else pixelMap[j,i][0] - int(math.floor(ord(message[c%l])/100))
                lst[1] = pixelMap[j,i][1]+ int(math.floor((ord(message[c%l]) % 100)/10)) if pixelMap[j,i][1] < 245 else pixelMap[j,i][1] - int(math.floor((ord(message[c%l]) % 100)/10)) 
                lst[2] = pixelMap[j,i][2]+ int(ord(message[c%l]) % 10) if pixelMap[j,i][2] < 245 else pixelMap[j,i][2] - int(ord(message[c%l]) % 10) 
                lst[3] = pixelMap[j,i][3]
            pixelsNew[j,i] =tuple(lst)  
            # print(pixelsNew[i, j])
            print("\n")
            c+=1
    im.close()
    img.show()
    img.save("encrypt.png")
    img.close()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Incorrect Command")
        print("Command Syntax : Anonymark [name of file].png/jpg")
        exit()
    encrypt(sys.argv[3], sys.argv[2], sys.argv[1]);
