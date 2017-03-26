from PIL import Image
import os
import operator

import pyocr
import pyocr.builders


def getBoxCoordinates(filepath):
        tool = pyocr.get_available_tools()[0]
        lang = tool.get_available_languages()[1]
        meme = Image.open(filepath)

        boxs = tool.image_to_string(meme,lang="eng",builder=pyocr.builders.WordBoxBuilder())
        return boxs



