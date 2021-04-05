#!/usr/bin/env python3
"""
Web App on Sentimental Analysis
"""
from textblob import TextBlob
from flask import Flask, request, render_template

app=Flask(__name__)


@app.route('/')
def welcome():
    """Welcome page"""
    return render_template("./index.html")

@app.route('/sentiments', methods = ["POST","GET"])
def sentiments():
    """Execute code block to get Sentiment polarity"""
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
        except(TypeError):
            return"<h2> Recheck your code block </h2>"
    else:
        return"<h2>Also recheck</h2>"


if __name__== '__main__':
    app.run(debug =True)
