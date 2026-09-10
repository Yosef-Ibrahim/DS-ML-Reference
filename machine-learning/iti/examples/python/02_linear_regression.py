"""Regression with a baseline, scaling, and regularization."""
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_regression(n_samples=300, n_features=5, noise=18, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = Pipeline([("scale", StandardScaler()), ("regressor", Ridge(alpha=1.0))])
model.fit(X_train, y_train)
predictions = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
print({"mae": mean_absolute_error(y_test, predictions), "rmse": rmse, "r2": r2_score(y_test, predictions)})
