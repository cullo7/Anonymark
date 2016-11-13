from PIL import Image
import io
import sys
import math
import hashlib
import urllib.request,io
import base64

message = "Aiden Cullo Brevi manu."
l = len(message)

def imgFromString(base64Str):
    base64Str = base64Str[base64Str.index(','):] # THIS IS WHY WE HAVE A PROBLEM LATER IF WE DO
    data = base64.b64decode(base64Str)
    image = Image.open(io.BytesIO(data))
    return image

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
            #print(pixelMap[i,j])
            lst = [0,0,0]
            if type(pixelMap[i,j]) ==  int:
                #print(str(im.palette.palette[pixelMap[i,j]*3])+" "+str(im.palette.palette[pixelMap[i,j]*3+1])+" "+str(im.palette.palette[pixelMap[i,j]*3+2]))
                lst[0] = im.palette.palette[pixelMap[i,j]*3]+ int(math.floor(ord(message[c%l])/100)) if im.palette.palette[pixelMap[i,j]*3] < 245 else im.palette.palette[pixelMap[i,j]*3]- int(math.floor(ord(message[c%l])/100))
                lst[1] = im.palette.palette[pixelMap[i,j]*3+1]+ int(math.floor((ord(message[c%l]) % 100)/10)) if im.palette.palette[pixelMap[i,j]*3+1] < 245 else im.palette.palette[pixelMap[i,j]*3+1]- int(math.floor((ord(message[c%l]) % 100)/10))
                lst[2] = im.palette.palette[pixelMap[i,j]*3+2]+ int(ord(message[c%l]) % 10) if im.palette.palette[pixelMap[i,j]*3+2] < 245 else im.palette.palette[pixelMap[i,j]*3+2]- int(ord(message[c%l]) % 10)
            else:
                lst[0] = pixelMap[i,j][0]+ int(math.floor(ord(message[c%l])/100)) if pixelMap[i,j][0] < 245 else pixelMap[i,j][0] - int(math.floor(ord(message[c%l])/100))
                lst[1] = pixelMap[i,j][1]+ int(math.floor((ord(message[c%l]) % 100)/10)) if pixelMap[i,j][1] < 245 else pixelMap[i,j][1] - int(math.floor((ord(message[c%l]) % 100)/10)) 
                lst[2] = pixelMap[i,j][2]+ int(ord(message[c%l]) % 10) if pixelMap[i,j][2] < 245 else pixelMap[i,j][2] - int(ord(message[c%l]) % 10) 
            pixelsNew[i,j] =tuple(lst)  
            c+=1
    im.close()
    img.show()
    img.save(savefile)
    img.close()

def decrypt(alter, orig):
    dmessage = ""
    orig_im = Image.open(orig)
    alter_im = Image.open(alter)
    #alter_im = Image.open(io.BytesIO(urllib.request.urlopen(alterURL).read()))
    alter_pixelMap = alter_im.load()
    orig_pixelMap = orig_im.load()
    for i in range(alter_im.size[0]):
        for j in range(alter_im.size[1]):
            num = 0
            if type(orig_pixelMap[i,j]) ==  int:
              num+=abs(alter_pixelMap[i,j][0]-orig_im.palette.palette[orig_pixelMap[i,j]*3])*100
              num+=abs(alter_pixelMap[i,j][1]-orig_im.palette.palette[orig_pixelMap[i,j]*3+1])*10
              num+=abs(alter_pixelMap[i,j][2]-orig_im.palette.palette[orig_pixelMap[i,j]*3+2])
            else:
              num+=abs(alter_pixelMap[i,j][0]-orig_pixelMap[i,j][0])*100
              num+=abs(alter_pixelMap[i,j][1]-orig_pixelMap[i,j][1])*10
              num+=abs(alter_pixelMap[i,j][2]-orig_pixelMap[i,j][2])
            if chr(num) == '.':
                return dmessage
            dmessage+= chr(num)
    return "Period not found"

def hash(imgURL):
    img_bytes = str(io.BytesIO(urllib.request.urlopen(imgURL).read()))
    hash_bytes = hashlib.sha512(img_bytes.encode('utf-8')).digest()
    Image.frombytes('1', (8, 8), hash_bytes).show()
    return

if __name__ == "__main__":
    encrypt(sys.argv[1], sys.argv[2], sys.argv[3]);
    print(decrypt(sys.argv[2],sys.argv[1]))
    #hash(sys.argv[1])
