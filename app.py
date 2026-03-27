from flask import Flask, request, jsonify
import joblib
import pandas as pd
import features

app = Flask(__name__)

# Load model
model = joblib.load('phishing_model.pkl')

# Rule-based check
def rule_based_check(url):
    if '@' in url or '$' in url:
        return 1
    return 0

@app.route('/')
def home():
    return "Phishing Detection API is running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    # Feature extraction
    features_dict = {
        'length': features.chklength(url),
        'dots': features.chkdot(url),
        'https': features.chkhttps(url),
        'at': features.chkat(url),
        'hyphen': features.chkhyphen(url),
        'slash': features.chkslash(url),
        'big': features.chkbig(url),
        'digits': features.chkdigits(url),
        'keywords': features.chkkeywords(url),
        'specialchars': features.special_chars(url),
        'double_slash': features.has_double_slash(url),
        'subdomains': features.count_subdomains(url),
        'suspicious_tld': features.has_suspicious_tld(url),
        'digit_ratio': features.digit_ratio(url),
        'encoded': features.has_encoded_chars(url),
        'abnormal': features.abnormal_structure(url)
    }

    df = pd.DataFrame([features_dict])

    # Rule-based override
    if rule_based_check(url):
        return jsonify({'prediction': 'phishing (rule-based)'})

    pred = model.predict(df)[0]

    if pred == 1:
        result = "phishing"
    else:
        result = "safe"

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)