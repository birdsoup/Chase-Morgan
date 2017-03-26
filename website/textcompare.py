#!/usr/bin/env python

import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
import os


def get_similar_template(keywords):

    chase_files = os.listdir("../chase")
    chase_files = ["../chase/" + file for file in chase_files]

    chase_contents = [open(file, "r").read() for file in chase_files]

    tfidf = TfidfVectorizer(min_df=1).fit_transform([keywords] + chase_contents)

    result = (tfidf * tfidf.T).A
    result = result[0][1:]

    closest = max(result)
    index = result.tolist().index(closest)

    print closest, chase_contents[index]

    return chase_files[index]

get_similar_template("meme")