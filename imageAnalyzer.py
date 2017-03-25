from PIL import Image 
import os
import operator

import pyocr
import pyocr.builders
import io


tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()[1]

final_text = []


memes = [Image.open("memes/"+filename) for filename in os.listdir('memes/')]#get list of meme images

for filename in os.listdir('memes/'):
        imageTxtFile = open("chase/"+filename+".chase","w")
        meme = Image.open("memes/"+filename)
        txt = tool.image_to_string(meme,lang=lang,builder=pyocr.builders.TextBuilder())
        try:
            imageTxtFile.write(txt)
        except UnicodeEncodeError:
            print(filename)

#print(imageFeatures)
