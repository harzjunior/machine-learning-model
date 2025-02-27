# Financial Article Classification

This project involves building and deploying a machine learning model to classify financial articles into predefined categories. It includes training the model, setting up a Flask web service for classification, and verifying the output.

## Project Structure

```
lmm/
│
├── classify_financial_articles.py  # Flask web service for classifying articles
├── client.py                       # Script to send requests to the classification service
├── train.py                        # Script to train the classification model
├── verify_output.py                # Script to verify the classification results
├── financial_text_classifier.pkl   # Trained classifier model
├── financial_text_encoder.pkl      # Label encoder
├── financial_text_vectorizer.pkl   # TF-IDF vectorizer
├── training_data.csv               # Training data
└── output.csv                      # Sample output file
```

## Requirements

- Python 3.6+
- Flask
- scikit-learn
- pandas
- numpy
- requests

Install the required packages using pip:

```bash
pip install Flask scikit-learn pandas numpy requests
```

## Step-by-Step Guide

### Step 1: Train the Model

Before running the classification service, you need to train the model. The `train.py` script trains a decision tree classifier using the provided training data.

```bash
python lmm/train.py
```

This will generate three files:
- `financial_text_classifier.pkl`
- `financial_text_vectorizer.pkl`
- `financial_text_encoder.pkl`

### Step 2: Run the Classification Service

Start the Flask web service by running `classify_financial_articles.py`:

```bash
python lmm/classify_financial_articles.py
```

The service will be available at `http://127.0.0.1:49200`.

### Step 3: Classify Articles

Use the `client.py` script to send a request to the classification service. This script reads a sample input, sends it to the service, and prints the classification result.

```bash
python lmm/client.py
```

### Step 4: Verify the Output

To verify the classification results, use the `verify_output.py` script. This script reads the output CSV file generated by the classification service and prints its contents.

```bash
python lmm/verify_output.py
```

### Files and Directories

- **classify_financial_articles.py**: This file contains the Flask application that serves the classification model.
- **client.py**: This script sends a sample request to the classification service.
- **train.py**: This script trains the machine learning model using the provided training data.
- **verify_output.py**: This script verifies the classification results.
- **financial_text_classifier.pkl**: The trained classification model.
- **financial_text_vectorizer.pkl**: The TF-IDF vectorizer used for text transformation.
- **financial_text_encoder.pkl**: The label encoder used for encoding the target labels.
- **training_data.csv**: The CSV file containing the training data.
- **output.csv**: The CSV file containing the classification results.

## Usage Example

Here’s a quick example of how to run the classification service and classify a new article:

1. **Train the Model**:
    ```bash
    python lmm/train.py
    ```

2. **Run the Classification Service**:
    ```bash
    python lmm/classify_financial_articles.py
    ```

3. **Send a Request to Classify an Article**:
    ```bash
    python lmm/client.py
    ```

4. **Verify the Output**:
    ```bash
    python lmm/verify_output.py
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.