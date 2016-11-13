#Anonymark

##Description
Encryption service to mark artwork with a digital signature. The hash of the original file will provide the verification for validating the owner. The image is decrypted using the original image in our chrome extension to reveal the true owner

##Example
We take a PNG file:
![alt tag](test_suite/6.png)

Then we encrypt it with our algortithm:
![alt tag](test_suite/example_encrypted.png)

Only the user with the actual original file will be able to decrpyt the file and get the message:

> Aiden Cullo and Ethan Schoen brevi manu

##Installing
Run `pip3 install -r requirements.txt`

##Running
Anonymark [filename].png/jpg

###Created by
* Ethan Schoen (EthanSchoen)
* Aiden Cullo (cullo7)
