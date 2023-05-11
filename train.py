import pandas as pd
import numpy as np
import joblib
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Load CSV file containing URLs
data = pd.read_csv('dataset/urls.csv')

# Extract features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['URL'])
y = np.array(data['Label'])
print(X[0])
# Train random forest model
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X,y)
scores = cross_val_score(model, X, y, cv=5)
# model.predict(['https://lps.mykokodesign.com/skcr_clc_es_gt_mkd/?coc=ld_gt_ytbrf60170_...'])
# Evaluate model performance using cross-validation
print('Accuracy: %0.2f (+/- %0.2f)' % (scores.mean(), scores.std() * 2))
with open('vector.pickle','wb') as file:
    pickle.dump(file)
with open('classifier/random_forest_urls_1.pkl','wb') as file:
    pickle.dump(model, file)