def get_vader_sentiment_dict(row, analyzer, subreddit):

    positive_scores, negative_scores, neutral_scores, compound_scores = [], [], [], []
    if not pd.isnull(row['selftext']) and len(row['selftext'].split()) >= 5:
        for s in re.split('[.!?]', row['selftext']):
            vs = analyzer.polarity_scores(s)
            positive_scores.append(vs['pos'])
            negative_scores.append(vs['neg'])
            neutral_scores.append(vs['neu'])
            compound_scores.append( vs['compound'])

    if positive_scores and negative_scores and neutral_scores and compound_scores:
        return {'URL': row['url'], 
                'Positive Score': np.mean(positive_scores), 
                'Negative Score': np.mean(negative_scores), 
                'Neutral Score': np.mean(neutral_scores), 
                'Compound Score': np.mean(compound_scores),
                'Subreddit': subreddit}
    return None
