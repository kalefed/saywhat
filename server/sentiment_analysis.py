from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# note: may need to run pip install vaderSentiment


def analyze_sentiment(message):
    analyzer = SentimentIntensityAnalyzer()

    vs = analyzer.polarity_scores(message)

    # MAIN OUTPUT: negative, neutral, positive sentiment ratings and compound total
    # print("{:-<65} {}".format(message, str(vs)))

    compound = vs.get("compound")
    if compound < -0.02:
        return "negative"
    elif compound >= -0.02 and compound <= 0.02:
        return "neutral"
    elif compound > 0.02:
        return "positive"
    else:
        return "No sentiment detected."
