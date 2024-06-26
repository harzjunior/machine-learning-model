from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Step 2
# Load pre-trained model and transformers
model = pickle.load(open('financial_text_classifier.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open('financial_text_vectorizer.pkl', 'rb'))
label_encoder = pickle.load(open('financial_text_encoder.pkl', 'rb'))

def process(inPath, outPath):
    # Read input file
    input_df = pd.read_csv(inPath)
    # Handle missing values in the 'body' column
    input_df['body'] = input_df['body'].fillna('')
    # Vectorize the data
    features = tfidf_vectorizer.transform(input_df['body'])
    # Predict the classes
    predictions = model.predict(features)
    # Convert output labels to categories
    input_df['category'] = label_encoder.inverse_transform(predictions)
    # Save results to CSV
    output_df = input_df[['id', 'category']]
    output_df.to_csv(outPath, index=False)

@app.route('/process', methods=['POST'])
def process_request():
    data = request.get_json()
    inPath = data['inPath']
    outPath = data['outPath']
    process(inPath, outPath)
    return jsonify({'status': 'success', 'output': outPath})

if __name__ == '__main__':
    app.run(port=49200)

# Step 3
# run the following sample
# curl -X POST -H "Content-Type: application/json" -d '{"inPath": "training_set.csv", "outPath": "output.csv"}' http://localhost:49200/process
