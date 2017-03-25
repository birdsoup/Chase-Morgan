from PIL import Image
import pytesseract 
import os
import indicoio
import operator

imageTxtFile = open("imageTxt.chase","w")
memes = [Image.open("memes/"+filename) for filename in os.listdir('memes/')]#get list of meme images

for meme in memes:
        meme.show()
        print(pytesseract.image_to_string(meme))

#print(imageFeatures)
