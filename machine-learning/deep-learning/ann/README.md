# Artificial Neural Networks

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

## Core idea

A dense layer computes `activation(Wx + b)`. Stacking layers lets the model
learn nonlinear combinations of features. ReLU is a practical hidden-layer
default; the output layer depends on the target:


| Task | Output | Typical loss |
| --- | --- | --- |
| Binary classification | One sigmoid unit | Binary cross-entropy |
| Multiclass classification | One softmax unit per class | Sparse or categorical cross-entropy |
| Regression | One linear unit | Mean squared or mean absolute error |

Standardize numeric features when their scales differ. Use dropout or weight
regularization only as needed, and prefer early stopping based on validation
loss over blindly choosing a large epoch count.

## Source notebooks and data

- [`ANN.ipynb`](notebooks/ANN.ipynb) is
  the original dense binary classifier. It is useful for seeing the Keras API,
  but its validation choice is a leakage-prone shortcut.
- [`Study ANN.ipynb`](<notebooks/Study ANN.ipynb>) demonstrates a
  three-class target and one-hot encoding.
- [`Practice ANN.ipynb`](<notebooks/Practice ANN.ipynb>) is a churn
  preprocessing study using [`customer_churn.csv`](data/customer_churn.csv).
  It depends on `scikeras` and contains exploratory cells.
- [`Deep_Learning_Keras_Demo.ipynb`](notebooks/Deep_Learning_Keras_Demo.ipynb)
  is the most complete session: breast-cancer classification, California
  housing regression, curves, dropout, Adam, and early stopping.
- [`model1.pkl`](model1.pkl) is the original serialized experiment artifact.
  ⚠️ It is not a reproducible model contract; prefer saving a model together
  with its preprocessing, library versions, and evaluation record.

## Runnable companion

[`ann_iris.py`](ann_iris.py) reproduces the smallest useful ANN example with
an explicit train/validation/test split. It imports TensorFlow lazily:

```bash
python machine-learning/deep-learning/ann/ann_iris.py
```

Install `tensorflow scikit-learn` only when running it. The script prints the
test accuracy and does not download or read a local dataset.

## Learning checklist

1. Establish a non-neural baseline.
2. Split before fitting preprocessing.
3. Choose output shape and loss from the target.
4. Track validation metrics and stop on validation loss.
5. Inspect a confusion matrix, class balance, and failure cases.
6. Tune a decision threshold only against validation data.

⚠️ A high accuracy score can hide poor minority-class recall. For churn or
medical classification, select metrics and thresholds using the actual cost of
false positives and false negatives.

## Choosing capacity and regularization

The number of parameters grows with layer widths, so capacity should follow the
amount and complexity of labeled data. Start with one or two hidden layers and
inspect learning curves. Underfitting suggests a representation, optimization, or
capacity problem; overfitting suggests more data, simpler capacity, early stopping,
weight decay, dropout, or augmentation where valid. Dropout changes training
behavior and should not be treated as a universal fix.

Use a validation split or cross-validation on the training portion to choose
architecture, epoch budget, learning rate, and threshold. Keep the test set out of
those decisions. For imbalanced classification, use class-aware metrics or weights
and inspect the confusion matrix; accuracy alone may reward predicting the majority.

## Source mapping and corrections

The four notebooks listed above correspond to the preserved ANN sessions; the
conceptual layers/activation/loss material is also summarized in
`deep-learning/reference/`. `ann_iris.py` is the smallest executable companion.
⚠️ The breast-cancer source notebook uses the test split as validation during
training, and the churn notebook mixes exploratory cells and optional `scikeras`.
Recreate those experiments with `workflow.md`, a separate validation set, and an
explicit dependency record. `model1.pkl` is an historical artifact, not a portable
model contract.

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
