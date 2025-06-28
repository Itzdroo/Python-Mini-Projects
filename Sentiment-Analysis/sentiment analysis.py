import nltk
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import random

# Download required datasets
nltk.download('movie_reviews')
nltk.download('punkt')

# Load the data
documents = []
labels = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append(movie_reviews.raw(fileid))
        labels.append(category)

# Shuffle data
combined = list(zip(documents, labels))
random.shuffle(combined)
documents[:], labels[:] = zip(*combined)

# Split into train and test
train_size = int(len(documents) * 0.8)
X_train = documents[:train_size]
y_train = labels[:train_size]
X_test = documents[train_size:]
y_test = labels[train_size:]

# Feature extraction
vectorizer = CountVectorizer(stop_words='english')
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# Train the classifier
classifier = MultinomialNB()
classifier.fit(X_train_features, y_train)

# Test the model
predictions = classifier.predict(X_test_features)
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy * 100:.2f}%")
