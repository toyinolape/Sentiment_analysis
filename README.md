# Sentiment Analysis
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
* Data Visualization

### Definition of Scope
The scope of the project would be focusing on the sentiments of 5 banks the Nigerian populace use. We would be Analyzing 4 commercial banks and 1 Digital bank, with the advent of the digital banks I just want to take a peak and see how well these digital banks would do against the traditional commercial banks. This would strictly focus on only banks and exclude the financial tech companies. 

### Data Collection
The data source is Twitter, a total of 1500 tweets contanting the keyword " bank_name" would be collected through the Twitter API buy first creating a developer account. Next, the data is cleaned to remove "@" handles, emojis, url links etc. 

### Data Preparation 
The data is then vectorized (i.e put in a bag of words model) to determine the sentiment of the tweets for the banks. The dataet is also tranformed to enable visualization using Data Analysis Visualization tools. 

### Machine Learning 
We would utilize the "Textblob" library to determine the sentiment of the tweets that have been cleaned.
```
def percentage(part,whole):
 return 100 * float(part)/float(whole)

def get_sentiment(corpus):
    noOfTweet = 1
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    tweet_list = []
    neutral_list = []
    negative_list = []
    positive_list = []
    for tweet in corpus:
        noOfTweet += 1
        #print(tweet.text)
        tweet_list.append(tweet)
        analysis = TextBlob(tweet)
        score = analyser().polarity_scores(tweet)
        neg = score['neg']
        neu = score["neu"]
        pos = score["pos"]
        comp = score['compound']
        polarity += analysis.sentiment.polarity

    if neg > pos:
        negative_list.append(tweet)
        negative += 1
        
    elif pos > neg:
        positive_list.append(tweet)
        positive += 1

    elif pos == neg:
        neutral_list.append(tweet)
        neutral += 1
    
    positive = percentage(positive, noOfTweet)
    negative = percentage(negative, noOfTweet)
    neutral = percentage(neutral, noOfTweet)
    polarity = percentage(polarity, noOfTweet)
    positive = format(positive, '.1f')
    negative = format(negative, '.1f')
    neutral = format(neutral, '.1f')
    return polarity, positive, negative, neutral
 
```
### Data Visualization 
Comparism between the wordcloud of the various banks are in the folder img or in the notebook.
Example of a Word Cloud is below:

[Wordcloud of Guaranty Trust Bank]('https://github.com/toyinolape/Sentiment_analysis/img/review2')