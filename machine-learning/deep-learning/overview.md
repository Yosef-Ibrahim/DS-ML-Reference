# Deep Learning Overview

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

## What deep learning adds

Deep learning uses layers of parameterized functions to learn representations
from data. A network computes a forward pass, measures error with a loss
function, and uses backpropagation plus an optimizer to update its weights.

The useful mental model is:

1. Inputs are represented as numeric tensors.
2. Layers transform those tensors.
3. The output layer represents the prediction distribution.
4. The loss supplies a training signal.
5. Validation data guides decisions; an untouched test set estimates final
   generalization.

An ANN (dense network) is a strong baseline for tabular features. A CNN adds
local connectivity and shared filters, making it a natural fit for images and
other grid-like signals.

## Prerequisites

Be comfortable with Python, NumPy arrays, train/validation/test splits,
standardization, classification metrics, and basic linear algebra. The examples
use scikit-learn datasets so no credentials or private data are needed.

## Source-session map

| Preserved source | What it demonstrates | Important reading note |
| --- | --- | --- |
| [`ANN.ipynb`](ann/notebooks/ANN.ipynb) | Loads Wisconsin breast-cancer data, scales it, and trains a binary dense classifier. | ⚠️ It validates on the test split during training. Use a separate validation split as shown in [`workflow.md`](workflow.md). |
| [`Study ANN.ipynb`](ann/notebooks/Study%20ANN.ipynb) | Three-class Iris classification with an ANN and one-hot targets. | Check that the scaler is fit only on training rows and that the final test set is not used for tuning. |
| [`Practice ANN.ipynb`](ann/notebooks/Practice%20ANN.ipynb) | Attempts preprocessing and a Keras classifier for `customer_churn.csv`. | ⚠️ It imports optional packages and mixes exploratory output with execution. Treat it as a study record; start from the cleaned workflow before reuse. |
| [`Deep_Learning_Keras_Demo.ipynb`](ann/notebooks/Deep_Learning_Keras_Demo.ipynb) | A more complete classification and California-housing regression workflow with early stopping. | ⚠️ `fetch_california_housing()` downloads data on first use; this is intentional but requires network access. |
| [`cnn_session_source.ipynb`](cnn/notebooks/cnn_session_source.ipynb) | MNIST CNN, VGG16 transfer learning, CIFAR-10, and an optional YOLO section. | ⚠️ It assumes a GPU and installs/imports optional packages up front. The companion runs CPU-safe MNIST and makes optional work explicit. |

The original teaching slides remain in [`reference/`](reference/). The ANN
deck is the conceptual source for layers, activations, losses, dropout,
initialization, and optimizers. The CNN PDF and deck provide the visual
explanation of filters, feature maps, pooling, and transfer learning.

## ⚠️ Corrections to carry forward

- Do not fit preprocessing transformers on validation or test data.
- Do not report the test score repeatedly while choosing epochs, architecture,
  thresholds, or preprocessing.
- A probability threshold of `0.5` is a policy choice, not a universal truth.
- A GPU is helpful for larger CNNs but is not required for the small MNIST
  companion.
- Transfer-learning weights and YOLO are optional extras, not prerequisites for
  understanding convolution.

## Suggested order

Read this overview, then [ANN](ann/README.md), run the Iris companion, read
[CNN](cnn/README.md), and finish with the [practical workflow](workflow.md).

## Core mathematical picture

For an input tensor `x`, each layer applies a parameterized map such as
`h=φ(Wx+b)`; the network composes these maps into `f_θ(x)`. Training minimizes an
empirical loss `L(θ)=1/n Σ ℓ(f_θ(x_i), y_i)` using gradients from backpropagation.
The optimizer, initialization, batch size, and learning rate affect the path to a
solution, while the validation set helps choose among paths and architectures.

The output layer must represent the target: a sigmoid probability for binary
classification, softmax probabilities for mutually exclusive classes, or a linear
value for regression. Cross-entropy evaluates distributions; MAE/MSE evaluate
numeric errors. A metric used for reporting need not be the differentiable loss used
for optimization, but both should serve the decision.

## Questions to ask while reading a session

- Which rows are used to learn preprocessing, and which rows are held out?
- Is “validation” actually an untouched test set being used repeatedly?
- Does the output shape match the label encoding?
- Do learning curves show underfitting, overfitting, or unstable optimization?
- Are errors concentrated in a class, subgroup, or input regime?

⚠️ A session can be valuable as a record while still being unsafe as a template.
Rebuild leakage-prone or download-heavy cells from `workflow.md` before applying
them to a new project.

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
