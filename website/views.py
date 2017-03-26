from flask import render_template, flash, redirect, url_for, request, g, Blueprint

from forms import SearchForm

import requests
import json
from datetime import datetime, timedelta
import calendar
import urllib
import base64
import os
import textcompare
from PIL import Image, ImageFont, ImageDraw
from textcompare import get_similar_template
from whiteSpaceCalculator import getBoxCoordinates
from markov import generateMemeText
import StringIO
import base64
from jpegger import jpegify



blueprint = Blueprint("views", "views")


@blueprint.route('/')
@blueprint.route('/index')
def index():
    return render_template("index.html", title='Home', from_keywords=SearchForm())


@blueprint.route('/from_keywords', methods=['POST'])
def from_keywords():
    #call meme generator from keywords here
    #result = generate_meme()
    form = SearchForm(request.form)
    img = base64.b64encode(open("static/harold.jpg", "r").read())
    terms = form.keywords.data

    template_path = "../memes/" + get_similar_template(terms).replace("../chase/", "").replace(".chase", "")

    boxes = getBoxCoordinates(template_path)
#pyocr.builders.Box

    img = Image.open(template_path)

    io = StringIO.StringIO()

    draw = ImageDraw.Draw(img)

    box_lst = []

    highest_coord = 999999
    leftmost_coord = 999999

    for box in boxes:
        ((x1, y1), (x2, y2)) = box.position
        size = abs((x2 - x1) * (y2 - y1)) 
        box_lst.append((size, box))
        if y1 < highest_coord:
            highest_coord = y1
        if x1 < leftmost_coord:
            leftmost_coord = x1

    box_lst = sorted(box_lst)
    box_lst = box_lst[0:-1]

    boxes = [box for (size, box) in box_lst if box.content != "" and box.content != " "]

    for box in boxes:
        draw.rectangle(box.position, fill="white")

    font = ImageFont.truetype("FreeMono.ttf", 16)



    text = generateMemeText(terms)#figure out how to do text here
            #should compile a corpus of text and just markov chain a sentence

    char_length = 50
    y_offset = 0
    for sub_text in range(0, len(text), char_length):
        draw.text((leftmost_coord, highest_coord + y_offset), text[sub_text:sub_text + char_length], (0, 0, 0), font=font)
        y_offset += char_length
    img.save(io, format="JPEG", quality=100)
    jpegify(io)

    data = base64.b64encode(io.getvalue())




    if form.validate():
        return render_template("result.html", imgdata=data, keywords=terms)
    else:
        flash_errors(form)
        return render_template("index.html", title="Home", from_keywords=SearchForm())


#this function was copied from http://flask.pocoo.org/snippets/12/
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

