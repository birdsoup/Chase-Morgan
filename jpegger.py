#!/usr/bin/env python
from PIL import Image
import StringIO


def jpegify(filename):
    output = StringIO.StringIO()
 

    img = Image.open(filename)
    img.save(output, format="JPEG")

    for i in range(100):
        im = Image.open(output)
        im.save(output, format="JPEG", quality=10)

    img_final = Image.open(output)
    img_final.save(filename + "_output", format="JPEG", quality=1)
