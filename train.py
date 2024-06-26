from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import pandas as pd


# Step 1
# Assuming you have the data
data = pd.read_csv('training_data.csv')
X = data['body']
y = data['category']

# Vectorize the text
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(X)

# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_tfidf, y_encoded)

# Save the model, vectorizer, and encoder
with open('financial_text_classifier.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('financial_text_vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf_vectorizer, f)

with open('financial_text_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)
