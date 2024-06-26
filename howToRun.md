***Detailed steps to run the project up to verifying the output with `verify_output.py`:

### 1. Clone the Repository

First, clone the repository to your local machine:

```sh
git clone https://github.com/harzjunior/financial-articles-classifier.git
cd financial-articles-classifier
```

### 2. Create and Activate a Virtual Environment

Set up a virtual environment to manage dependencies:

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Required Packages

Install the necessary Python packages from `requirements.txt`:

```sh
pip install -r requirements.txt
```

### 4. Ensure Necessary Files are Present

Make sure the following files are in the project directory:
- `financial_text_classifier.pkl`
- `financial_text_vectorizer.pkl`
- `financial_text_encoder.pkl`
- `training_set.csv`

### 5. Start the Flask Server

Run the Flask server to start the classification service:

```sh
python classify_financial_articles.py
```

You should see output indicating the server is running:

```
* Serving Flask app 'classify_financial_articles'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:49200
Press CTRL+C to quit
```

### 6. Send a POST Request to Classify Articles

In a new terminal window or tab (while keeping the server running), use `curl` to send a POST request to the server:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"inPath": "training_set.csv", "outPath": "output.csv"}' http://localhost:49200/process
```

You should receive a response indicating success:

```json
{"output":"output.csv","status":"success"}
```

### 7. Verify the Output

Create a new Python script named `verify_output.py` to load and print the contents of the `output.csv` file:

```python
import pandas as pd

# Load the output CSV
output_df = pd.read_csv('output.csv')

# Print the contents
print(output_df)
```

Run the script to verify the output:

```sh
python verify_output.py
```

You should see the classification results printed in the terminal:

```
      id              category
0    1199  Mergers_Acquisitions
1    1338                   Oil
2    1613           Commodities
3    2232            Litigation
4    1344                   Oil
...   ...                   ...
2105 1638           Commodities
2106 1095  Mergers_Acquisitions
2107 1130  Mergers_Acquisitions
2108 1294            Litigation
2109  860               Capital

[2110 rows x 2 columns]
```

### Summary

By following these steps, you should be able to:

1. Set up the project environment.
2. Start the Flask server.
3. Send a request to classify articles.
4. Verify the classification results.
