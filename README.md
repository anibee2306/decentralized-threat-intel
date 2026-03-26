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