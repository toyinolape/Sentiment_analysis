# Stutern Final Project
This is a complete Data Science project on Sentimental Analysis. Below is a overview of Sentimental Analhysis and its applications.

## Sentiment Analysis
Sentiment analysis is the process of detecting positive or negative sentiment in text. It’s often used by businesses to detect sentiment in social data, gauge brand reputation, and understand customers.

Since customers express their thoughts and feelings more openly than ever before, sentiment analysis is becoming an essential tool to monitor and understand that sentiment. Automatically analyzing customer feedback, such as opinions in survey responses and social media conversations, allows brands to learn what makes customers happy or frustrated, so that they can tailor products and services to meet their customers’ needs.

### Applications of Sentimental Analysis 
The applications of sentiment analysis are endless and can be applied to any industry, from finance and retail to hospitality and technology. Below, we’ve listed some of the most popular ways that sentiment analysis is being used in business:

- Social Media Monitoring
- Brand Monitoring
- Voice of customer (VoC)
- Customer Service
- Market Research

## Methodoloy 

* Definition of Scope
* Data Collection 
* Data Preparation 
* Machine Learning
* Web App Creation and hosting 


### Definition of Scope
The scope of the project would be focusing on the sentiments of 5 banks the Nigerian populace use. We would be Analyzing 4 commercial banks and 1 Digital bank, with the advent of the digital banks I just want to take a peak and see how well these digital banks would do against the traditional commercial banks. This would strictly focus on only banks and exclude the financial tech companies. 

### Data Collection
The data source is Twitter, a total of 1500 tweets contanting the keyword " bank_name" would be scraped through the Twitter API by first creating a developer account then using the tweepy module to request for these twetts. 

### Data Preparation 
Next, the data is cleaned to remove "@" handles, emojis, url links etc. The data is then vectorized (i.e put in a bag of words model) to determine the sentiment of the tweets for the banks. The dataset is also tranformed to enable wordcloud visualization using wordcloud module.

![Wordcloud of Guaranty Trust Bank](https://github.com/toyinolape/Sentiment_analysis/blob/master/img/review2.png)

### Machine Learning 
We would utilize the "Textblob" library to determine the sentiment of the tweets that have been cleaned. Polarity above 0.7 would be considered postive, polarity between the range 0.7 - 0.4 are neutral and all below 0.4 would be negative.



### Web App
We would be making a web app using the python library "Flask" which is a Python web framework built with a small core and easy-to-extend philosophy. The textblob module would then be used to predict the polarity of a text or sentence entered into the web app. 

To run the web app, you can follow the steps below 

The command is used to install the virtual environment
```
python3 -m pip install --user virtualenv

```
Use the next command to first create your virtual environment where “stu_env” is the name of my virtual environment:
```
python3 -m venv Stuternenv
```

Then activate the virtual environment that was just created.
```
source stu_env/bin/activate
```
Then the code block below installs the required modules/libraries the web app depends on.

```
pip3 install -r requirements.txt
```

Run the web app on your local device by executing the script on python3 then copy the http link for a demo on your web browser.

```
(stu_env) C/Users/Sentiment_analysis$ python3 app.py

```

![Web App](https://github.com/toyinolape/Sentiment_analysis/blob/master/img/senti2.PNG)

The result of the sentence that was keyed into the web app above is as follows;
![Result](https://github.com/toyinolape/Sentiment_analysis/blob/master/img/senti1.PNG)


#### Hosting on Azure Web App Service

This web app would be hosted on Azure web app service. First an Azure subscription is created and an Azure Web App Service Rsource was used to host the website. 

[Bank Sentiment Web App](https://sentimentanalysis1.azurewebsites.net/)
