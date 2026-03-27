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
df['double_slash'] = df['url'].apply(features.has_double_slash)
df['subdomains'] = df['url'].apply(features.count_subdomains)
df['suspicious_tld'] = df['url'].apply(features.has_suspicious_tld)
df['digit_ratio'] = df['url'].apply(features.digit_ratio)
df['encoded'] = df['url'].apply(features.has_encoded_chars)
df['abnormal'] = df['url'].apply(features.abnormal_structure)

X = df[['length', 'dots', 'https', 'at', 'hyphen', 'slash', 'big', 'digits', 'keywords', 'specialchars', 'double_slash', 'subdomains', 'suspicious_tld', 'digit_ratio', 'encoded', 'abnormal']]
y = df['type']

from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier



from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    scale_pos_weight=1,  # adjust if imbalance
    eval_metric='logloss'
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

joblib.dump(model, 'phishing_model.pkl')
