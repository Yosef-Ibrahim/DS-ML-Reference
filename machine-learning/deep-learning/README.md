# Deep Learning

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

This directory is a normalized, public-facing home for the Deep Learning material
from the original training folder. It covers artificial neural networks (ANNs),
convolutional neural networks (CNNs), and a practical experiment workflow.

## Guides

- [Overview](overview.md): concepts, prerequisites, and a map of the source material.
- [Artificial Neural Networks](ann/README.md): dense networks, output choices, and the ANN sessions.
- [Convolutional Neural Networks](cnn/README.md): convolution, image classification, transfer learning, and CNN notes.
- [Practical workflow](workflow.md): a reproducible, leakage-safe model development process.


## Layout

```text
ann/
  data/customer_churn.csv
  notebooks/                 # preserved teaching notebooks
  ann_iris.py                # small runnable companion
cnn/
  notebooks/                 # preserved teaching notebook
  cnn_mnist.py               # small runnable companion
reference/                   # source PDF/PPTX files
```

The `*_source.ipynb` files retain the original sessions. The Python companions
are deliberately shorter and corrected for fresh, non-notebook execution.

## Running examples

```bash
python machine-learning/deep-learning/ann/ann_iris.py
python machine-learning/deep-learning/cnn/cnn_mnist.py
```

Install only what the example needs. TensorFlow is imported inside `main`, so
reading the source or running `--help` does not require TensorFlow.

## Study route

Begin with [`overview.md`](overview.md) to connect tensors, losses, validation, and
the preserved sessions. Read [`ann/README.md`](ann/README.md) first because a dense
network exposes the common forward-pass and optimization vocabulary. Then use
[`cnn/README.md`](cnn/README.md) to see how locality and shared filters change the
inductive bias, and finish with [`workflow.md`](workflow.md) to turn an experiment
into a defensible artifact.

For either model family, follow the same loop: define the target and unit of
analysis, split before fitting preprocessing, establish a non-neural baseline,
choose output/loss/metric together, monitor validation behavior, inspect errors,
and evaluate the final test set once. A GPU, a larger network, or more epochs is not
evidence of a better experiment.

## Source-to-companion map

The `*_source.ipynb` files preserve the original sessions and their exploratory
order. `ann/ann_iris.py` and `cnn/cnn_mnist.py` are intentionally smaller runnable
companions: they make imports explicit, avoid optional workloads, and are suitable
for checking the core API. The `reference/` files hold the original conceptual PDF
and slide material. Use the source session for context and the companion plus guides
for current, leakage-safe practice.

## Environment and reproducibility

TensorFlow is optional for reading this directory and is imported lazily by the
companions. MNIST may download on first run; larger transfer-learning and detection
experiments can require network access, substantial memory, licenses, and a GPU.
Record Python/TensorFlow versions, random seeds, data split, preprocessing, model
shape, optimizer, learning rate, epoch budget, and best validation checkpoint.
Never commit downloaded credentials, private data, or opaque model tokens.

## ⚠️ Correction notes

The preserved notebooks are exploratory records: some use a test split as validation,
install optional dependencies in cells, or download data and weights implicitly.
Keep those limitations visible, use a separate validation split, and make optional
GPU, transfer-learning, and detection work explicit before reusing a session.

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
