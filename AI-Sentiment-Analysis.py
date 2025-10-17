import string

positive_words = {"good", "happy", "love", "great", "fantastic"}
negative_words = {"bad", "sad", "terrible", "hate", "awful"}

def analyze_sentiment(text):
    sentences = [s.strip() for s in text.replace('!', '.').replace('?', '.').split('.') if s]
    results = []

    for sentence in sentences:

        words = [w.strip(string.punctuation).lower() for w in sentence.split()]

        pos_count = sum(1 for w in words if any(w.startswith(p) for p in positive_words))

        neg_count = sum(1 for w in words if any(w.startswith(n) for n in negative_words))

        if pos_count > neg_count:
            results.append("Positive")
        elif neg_count > pos_count:
            results.append("Negative")
        else:
            results.append("Neutral")

    return results

text = input("Enter your text (Multiple sentences are allowed): ")
sentiments = analyze_sentiment(text)

for i, sentiment in enumerate(sentiments, 1):
    print(f"Sentence {i}: {sentiment}")
