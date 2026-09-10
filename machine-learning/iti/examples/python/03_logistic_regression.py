"""Binary classification with probabilities and confusion-matrix metrics."""
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, stratify=data.target, random_state=42
)
model = Pipeline([("scale", StandardScaler()), ("classifier", LogisticRegression(max_iter=2000))])
model.fit(X_train, y_train)
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]
print("confusion matrix:\n", confusion_matrix(y_test, predictions))
print({"accuracy": accuracy_score(y_test, predictions), "precision": precision_score(y_test, predictions),
       "recall": recall_score(y_test, predictions), "roc_auc": roc_auc_score(y_test, probabilities)})
