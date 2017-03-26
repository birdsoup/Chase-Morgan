from flask import render_template, flash, redirect, url_for, request, g, Blueprint

from forms import SearchForm

import requests
import json
from datetime import datetime, timedelta
import calendar
import urllib
import base64


blueprint = Blueprint("views", "views")


@blueprint.route('/')
@blueprint.route('/index')
def index():
    return render_template("index.html", title='Home', from_keywords=SearchForm())

#@blueprint.route('/favicon.ico')
#def favicon():
#    return send_from_directory(os.path.join("/static/",'favicon.ico', mimetype='image/vnd.microsoft.icon'))


@blueprint.route('/from_keywords', methods=['POST'])
def from_keywords():
    #call meme generator from keywords here
    #result = generate_meme()
    form = SearchForm(request.form)
    img = base64.b64encode(open("static/harold.jpg", "r").read())
    if form.validate():
        return render_template("result.html", imgdata=img, keywords=form.keywords.data)
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

