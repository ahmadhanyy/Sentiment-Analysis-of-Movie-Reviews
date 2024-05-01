import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


# Lowercase the text
def lowercase_text(text):
    return text.lower()

# Remove punctuation from the text
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Remove stopwords from the text
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    return [i for i in tokens if not i in stop_words]

# Apply stemming to the text
def apply_stemming(text):
    stemmer= PorterStemmer()
    return [stemmer.stem(word) for word in text]

# Apply lemmatization to the text
def apply_lemmatization(text):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in text]

# Apply all preprocessing steps to the text
def preprocess_text(reviews):
    preprocessed_reviews = []
    for review in reviews:
        review = lowercase_text(review)
        review = remove_punctuation(review)
        review = remove_stopwords(review)
        review = apply_lemmatization(review)
        #review = apply_stemming(review)
        preprocessed_reviews.append(review)
    return preprocessed_reviews

