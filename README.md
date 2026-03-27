# decentralized-threat-intel
Decentralized Threat Intelligence software with AI and blockchain integration

# Decentralized Threat Intelligence System

## Features
- URL classification using ML
- Detects phishing, malware, benign URLs

## How to run
1. Install dependencies from requirements.txt

2. Dataset

Download dataset from Kaggle:
https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset

Place it in:
data/malicious_phish.csv

3. Run train.py to save the model
## Note
The trained model (.pkl) is not included due to size limits.

To generate it:
python src/train.py

4. Run predict.py

# NEW STUFF 1

## Running the Project (Flask API)

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd <repo-name>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask server

```bash
python app.py
```

### 4. Test the API

Send a POST request to:

```
http://127.0.0.1:5000/predict
```

Example JSON:

```json
{
  "url": "example.com"
}
```
