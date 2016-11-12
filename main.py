from PIL import Image
import sys
import imagehash

message = "Aiden Cullo Brevi manu."
l = len(message)

def encrypt(img, savefile):
    im = Image.open(img)
    pixelMap = im.load()
    img = Image.new(im.mode, im.size)
    pixelsNew = img.load()
    c = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            lst = list(pixelsNew[i,j])
            lst[0] = pixelMap[i,j][0]+ int(ord(message[c%l])/100)
            lst[1] = pixelMap[i,j][1]+ int((ord(message[c%l]) % 100)/10)
            lst[2] = pixelMap[i,j][2]+ int(ord(message[c%l]) % 10)
            pixelsNew[i,j] = tuple(lst)
            c+=1
    im.close()
    img.show()       
    img.save(savefile) 
    img.close()

def decrypt(img, orig):
    dmessage = ""
    im1 = Image.open(img)
    im2 = Image.open(orig)
    pixelMap1 = im1.load()
    pixelMap2 = im2.load()
    for i in range(im1.size[0]):
        for j in range(im1.size[1]):
            num = 0
            num+=(pixelMap1[i,j][0]-pixelMap2[i,j][0])*100
            num+=(pixelMap1[i,j][1]-pixelMap2[i,j][1])*10
            num+=(pixelMap1[i,j][2]-pixelMap2[i,j][2])
            if chr(num) == '.':
                return dmessage
            dmessage+=chr(num)

def hash(img):
    return imagehash.average_hash(Image.open(img))

if __name__ == "__main__":
    encrypt(sys.argv[1], sys.argv[2]);
    print(decrypt(sys.argv[2],sys.argv[1]))
    print(hash(sys.argv[2]))
