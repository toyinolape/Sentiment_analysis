#!/usr/bin/env python3

import pandas as pd
import numpy as np
from textblob import TextBlob 
import pickle
from flask import Flask, jsonify, request, render_template, url_for
import json
from joblib import dump, load

app=Flask(__name__)


@app.route('/')
def welcome():
    return render_template("./index.html")
    

@app.route('/sentiments', methods = ["POST","GET"])
def sentiments():
    # execute when sentiments is clicked
    if request.method == "POST":
        
        try:
            text = request.form.get("Text")
            polarity1 = TextBlob(text).sentiment.polarity
            if polarity1 >= 0.7:
                polarity1 = "Positive"
            elif polarity1 >= 0.4:
                polarity1 = "Neutral"
            else:
                polarity1 = "Negative"
            return render_template("result.html", polarity = polarity1)
        except:
            return"<h2> Recheck your code block </h2>"
    else:
        return"<h2>Also recheck</h2>"


if __name__== '__main__':
    app.run(debug =True)