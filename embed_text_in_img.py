#!/bin/sh

# You may need to download requests and exiftool if you don't already have them
# To pull the message, run [ exiftool FILE_NAME | grep "Comment" | cut -d ":" -f2 | while read line; do echo $line|base64 -D; done ]

import requests
import base64 as b
import subprocess
import wget

filename = 'IMAGE_FILE_NAME.jpg' #this is the file name of the image
wget.download('LINK_TO_THE_IMAGE.jpg') #link to the image you want to jam the info into

key = "YOU_MESSAGE_HERE" #the message you want to embed


key = b.b64encode(key) #encode the message into base64

subprocess.call(('exiftool ' +filename+ ' -comment=%s' % key ).split()) #put the message into the image data as a comment