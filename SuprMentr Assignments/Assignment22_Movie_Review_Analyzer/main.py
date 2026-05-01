# Simple Sentiment Analyzer (Rule-Based)

positive_words = {
    "good", "great", "amazing", "awesome", "love", "excellent", "fantastic", "nice"
}

negative_words = {
    "bad", "worst", "boring", "terrible", "hate", "awful", "poor", "waste"
}

def analyze_sentiment(review):
    review = review.lower().split()
    
    pos_count = 0
    neg_count = 0

    for word in review:
        if word in positive_words:
            pos_count += 1
        elif word in negative_words:
            neg_count += 1

    if pos_count > neg_count:
        return "Positive 😊"
    elif neg_count > pos_count:
        return "Negative 😞"
    else:
        return "Neutral 😐"


# Test on 5 reviews
reviews = [
    "This movie was amazing and awesome",
    "Worst movie ever it was boring",
    "The film was good but a bit slow",
    "I love this movie it was fantastic",
    "It was okay not good not bad"
]

for i, review in enumerate(reviews):
    print(f"\nReview {i+1}: {review}")
    print("Sentiment:", analyze_sentiment(review))