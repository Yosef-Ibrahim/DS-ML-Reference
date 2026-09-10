"""Leakage-safe end-to-end classification workflow."""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, stratify=data.target, random_state=42
)
model = Pipeline([("scale", StandardScaler()), ("classifier", LogisticRegression(max_iter=1000))])
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("accuracy:", round(accuracy_score(y_test, predictions), 3))
print(classification_report(y_test, predictions, target_names=data.target_names))
