import joblib
import features
import pandas as pd

model = joblib.load('phishing_model.pkl')

url = input("Enter a URL to check: ")

data = {
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

df = pd.DataFrame([data])
pred = model.predict(df)
print(pred)

def rule_based_check(url):
    if '@' in url or '$' in url:
        return 1
    return 0

if rule_based_check(url) == 1:
    print("The URL is likely a phishing attempt(rule-based)")
elif pred[0] == 1:
    print("The URL is likely a phishing attempt.")
else:
    print("The URL is likely safe.")

