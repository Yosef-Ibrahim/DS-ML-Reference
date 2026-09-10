# Introductory neural networks

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

A feed-forward network composes `h = ϕ(Wx+b)` layers and learns by back-propagating
loss gradients. Scale inputs, use a validation strategy, set a seed, watch
convergence warnings, and use regularization or early stopping to limit overfitting.
The copied `Codes/2.3_NN` files and `Dataset_spine.csv` are preserved; their snippets
are teaching fragments, not a complete deployment project.

## Forward pass and learning

A dense layer computes `h=φ(Wx+b)`. Without a nonlinear activation, stacked dense
layers collapse into one linear transformation. ReLU `max(0,z)` is a practical
hidden-layer default; sigmoid is common for a binary output and softmax converts
multiclass logits into a distribution. Backpropagation applies the chain rule to
compute gradients, and an optimizer updates parameters such as
`W ← W − η∇W L`.

The output and loss must match the target: one sigmoid unit with binary
cross-entropy for binary labels, one softmax unit per class with cross-entropy for
mutually exclusive classes, or a linear unit with MAE/MSE for regression. Keep labels
and output shape aligned, and verify that the chosen metric reflects the decision.

## A safe experiment

1. Establish a linear/tree baseline and freeze a train/validation/test split.
2. Scale numeric inputs using training statistics; encode categories explicitly.
3. Choose a small architecture, seed, optimizer, learning rate, and batch size.
4. Track training and validation loss, using early stopping with restored best weights.
5. Diagnose underfitting versus overfitting before adding layers or epochs.
6. Evaluate the final model once and inspect class-wise failures or residuals.

Dropout, weight decay, augmentation, and early stopping are regularizers, not
guarantees. A validation curve that improves while training loss falls is expected;
the reverse can indicate a data or metric problem. Repeated experiments should
record seeds and package versions because initialization and hardware can affect
results.

## ⚠️ Correction notes and source map

The copied `2.3_NN` files and `Dataset_spine.csv` illustrate API fragments and may
assume pre-existing arrays. Start with `examples/python/` only after defining the
data contract. For the extended ANN/CNN material, use `deep-learning/overview.md`
and `deep-learning/workflow.md`. Do not use a test split as `validation_data`, and
do not interpret a single high training accuracy as generalization.

---

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
