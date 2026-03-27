import string

# Simple stopwords list
stop_words = {
    "is", "am", "are", "the", "a", "an", "and", "or",
    "in", "on", "at", "to", "for", "of", "with", "this"
}

def clean_text(text):
    # 1. Lowercase
    text = text.lower()

    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 3. Tokenization
    words = text.split()

    # 4. Remove stop words
    filtered_words = [word for word in words if word not in stop_words]

    # Join back
    return " ".join(filtered_words)


# Test
input_text = input("Enter text: ")
cleaned = clean_text(input_text)

print("\nCleaned Text:")
print(cleaned)