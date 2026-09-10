# Convolutional Neural Networks

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

## How convolution works

A convolution layer slides learned kernels over an image, producing feature
maps. Early filters often respond to edges and textures; deeper filters combine
those patterns. Pooling or strided convolution reduces spatial size, while
normalization and regularization can improve optimization. A final classifier
maps learned features to class probabilities.


The source session uses MNIST and CIFAR-10, then demonstrates VGG16
transfer-learning and YOLO object detection. Those are distinct workloads:
classification predicts labels for a whole image, while detection predicts
locations and labels for multiple objects.

## Source session

[`cnn_session_source.ipynb`](notebooks/cnn_session_source.ipynb) is the
preserved, broad hands-on notebook. It covers:

1. loading and exploring MNIST;
2. training a simple CNN and visualizing predictions;
3. comparing a VGG16 transfer-learning model;
4. repeating the classification workflow on CIFAR-10; and
5. optional YOLOv8 detection and segmentation.

⚠️ The original notebook says a GPU is required, installs packages in notebook
cells, and imports optional tools before they are needed. A GPU is useful for
VGG16/YOLO and larger images, but the MNIST model is CPU-capable. The original
also depends on remote dataset/model downloads; expect runtime and licensing
differences outside Colab.

## Runnable companion

[`cnn_mnist.py`](cnn_mnist.py) intentionally focuses on the core CNN idea:
MNIST normalization, a small convolutional model, and one evaluation pass.
TensorFlow is imported only after argument parsing, and no VGG/YOLO dependency
is required.

```bash
python machine-learning/deep-learning/cnn/cnn_mnist.py --epochs 1
```

Use more epochs for learning rather than benchmarking. The first run may
download MNIST through Keras.

## Practical checks

- Preserve the channel dimension (`(height, width, channels)`).
- Normalize pixel values consistently.
- Keep a test set untouched while selecting augmentation and architecture.
- Inspect class-wise metrics, not only aggregate accuracy.
- Compare augmentation and transfer learning against a simple baseline.

## Shape and computation

For an input of height `H`, width `W`, channels `C`, a kernel with spatial size
`K`, stride `S`, and padding `P` produces approximately
`floor((H+2P−K)/S)+1` positions per spatial dimension. Each learned filter is
shared across locations, so the parameter count is `K×K×C` plus a bias rather than
one parameter per pixel. Padding preserves spatial extent when chosen to match the
kernel and stride; pooling or stride trades resolution for receptive field.

## Practical training sequence

1. Verify labels, class balance, image dimensions, channel order, and license.
2. Split by image or subject before normalization and augmentation.
3. Normalize pixels consistently and apply only label-preserving augmentation to
   training images.
4. Train a small CNN baseline, track validation curves, and inspect predictions.
5. Compare transfer learning only after freezing the feature extractor and checking
   preprocessing expected by the base model.
6. Tune thresholds and evaluate the untouched test set once, with class-wise errors.

Transfer learning can be effective with limited data, but weights may be trained on
another domain and carry licensing or distribution assumptions. Object detection
and segmentation require different labels and metrics from image classification;
do not treat a YOLO demo as a prerequisite for understanding convolution.

## ⚠️ Source mapping and corrections

`cnn_session_source.ipynb` is the preserved session for MNIST, CIFAR-10, VGG16, and
optional YOLO work; `cnn_mnist.py` is the CPU-capable companion. The source installs
optional packages and assumes a GPU/download access. The companion keeps TensorFlow
lazy and makes no VGG/YOLO dependency mandatory. Use `workflow.md` to prevent
test-as-validation leakage and to record resize, normalization, augmentation, and
split policy.

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
