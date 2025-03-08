from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: may need to run pip install vaderSentiment

#reconfigure input to work with rest of code
sentences = ["You have no rizz", "Skibbity toilet Ohio.","KJ is gorgeous","WHAT IS YOUR PROBLEM"]

analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)

    #MAIN OUTPUT: negative, neutral, positive sentiment ratings and compound total
    print("{:-<65} {}".format(sentence, str(vs)))

    compound = vs.get('compound')
    if compound < -0.03:
        sentiment = "The overall sentiment of the message is: NEGATIVE"
    elif compound >= -0.03 and compound <= 0.03:
        sentiment = "The overall sentiment of the message is: NEUTRAL"
    elif compound > 0.03:
        sentiment = "The overall sentiment of the message is: POSITIVE"

    #MAIN OUTPUT: compount rating translated to neg, neut, or pos
    print(sentiment)