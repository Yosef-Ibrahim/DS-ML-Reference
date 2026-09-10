"""Cross-validated search and local persistence demonstration."""
from pathlib import Path
import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, stratify=data.target, random_state=42
)
pipeline = Pipeline([("scale", StandardScaler()), ("classifier", LogisticRegression(max_iter=1000))])
search = GridSearchCV(pipeline, {"classifier__C": [0.1, 1.0, 10.0]}, cv=5, scoring="accuracy")
search.fit(X_train, y_train)
print("best parameters:", search.best_params_, "test score:", search.score(X_test, y_test))
artifact = Path("model.joblib")
joblib.dump(search.best_estimator_, artifact)
print("saved:", artifact.resolve())
