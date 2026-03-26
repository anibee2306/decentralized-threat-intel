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
    'specialchars': features.special_chars(url)
}

df = pd.DataFrame([data])
pred = model.predict(df)

if pred[0] == 'phishing':
    print("The URL is likely a phishing attempt.")
else:
    print("The URL is likely safe.")

