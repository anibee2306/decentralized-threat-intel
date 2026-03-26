import pandas as pd
import features

df = pd.read_csv('malicious_phish.csv')

df['length'] = df['url'].apply(features.chklength)
df['dots'] = df['url'].apply(features.chkdot)
df['https'] = df['url'].apply(features.chkhttps)
df['at'] = df['url'].apply(features.chkat)
df['hyphen'] = df['url'].apply(features.chkhyphen)
df['slash'] = df['url'].apply(features.chkslash)
df['big'] = df['url'].apply(features.chkbig)
df['digits'] = df['url'].apply(features.chkdigits)
df['keywords'] = df['url'].apply(features.chkkeywords)
df['specialchars'] = df['url'].apply(features.special_chars)

X = df[['length', 'dots', 'https', 'at', 'hyphen', 'slash', 'big', 'digits', 'keywords', 'specialchars']]
y = df['type']

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(class_weight='balanced')

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
joblib.dump(model, 'phishing_model.pkl')
