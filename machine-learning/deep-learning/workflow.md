# Practical Deep Learning Workflow

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

## 1. Define the experiment

Write down the prediction target, unit of analysis, success metric, acceptable
error trade-offs, and data provenance before writing model code. A neural

network is not a substitute for a clear target or representative data.

## 2. Inspect and split

Check missing values, duplicates, label balance, ranges, and leakage columns.
Split into train, validation, and test sets before learning any statistics.
For time-ordered data, use a chronological split; for grouped entities, keep a
group in one split.

## 3. Fit preprocessing on training data only

Fit scalers, imputers, encoders, feature selection, and augmentation policies
on training data. Apply the fitted transformations to validation and test data.
This is the most important correction to the original ANN session.

## 4. Establish a baseline

Use a simple rule or classical model first. Then add a small ANN or CNN and
record the same metrics. This distinguishes a useful representation from a
merely larger model.

## 5. Build, compile, and train

Choose the output and loss from the target distribution. Start with Adam and a
conservative learning rate, then monitor validation loss. Use early stopping
with restored best weights. Log the random seed, split, preprocessing, model
shape, package versions, and training budget.

## 6. Evaluate once

After decisions are final, evaluate on the test set once. Report uncertainty
where possible, class-wise metrics, calibration or threshold policy, and
representative errors. Do not silently replace a weak test result with a
validation result.

## 7. Save a usable artifact

Save the model together with preprocessing and a small metadata record. A
standalone pickle such as [`ann/model1.pkl`](ann/model1.pkl) may not reload
across Python or library versions and does not prove how inputs were prepared.

## Mapping to the source sessions

- The ANN notebooks show dense classification, churn preprocessing, regression,
  dropout, and early stopping.
- The CNN notebook extends the same split/compile/fit/evaluate pattern to image
  tensors, then introduces transfer learning and detection.
- [`ann/ann_iris.py`](ann/ann_iris.py) and [`cnn/cnn_mnist.py`](cnn/cnn_mnist.py)
  are intentionally small reference implementations for the two model families.

## ⚠️ Common corrections

- Do not use test data as `validation_data`.
- Do not assume GPU availability.
- Do not make TensorFlow, scikeras, VGG, or YOLO mandatory just to read or run
  a basic example.
- Do not embed credentials, private paths, or downloaded model tokens.
- Do not compare metrics from different splits or preprocessing pipelines.

## 8. Diagnose before tuning

If both training and validation loss remain high, check target quality, input scale,
capacity, and learning rate before adding regularization. If training loss keeps
falling while validation loss rises, stop at the best validation checkpoint and
consider a smaller model, weight decay, dropout, or more representative data.
Inspect learning curves and a fixed set of failure examples after every material
change; otherwise a large hyperparameter search can hide a data problem.

## 9. Make image experiments reproducible

For images, document resize/crop policy, channel order, normalization range,
augmentation operations, and whether an image or its near-duplicate can appear in
more than one split. Fit label mappings on training data and preserve the mapping
with the model. Augmentation must preserve the label: a horizontal flip is not
valid for every object or medical image. Evaluate class-wise performance and
calibration, not only top-line accuracy.

## 10. Release and monitor

A model artifact should include preprocessing, label mapping, model configuration,
best checkpoint, metrics, data window, and dependency versions. Validate the input
shape and range at serving time. Monitor input drift, missingness, confidence,
latency, and delayed labels; define a rollback artifact and retraining trigger.
Transfer-learning weights and detection models also require a license and provenance
record.

These additions connect the ANN and CNN sessions to the same evaluation discipline
used in `iti/evaluation/`; they are not claims that the original notebooks performed
all of these checks.

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
