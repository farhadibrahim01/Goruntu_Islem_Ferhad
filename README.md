# Fruit Classification with Transfer Learning

This project applies transfer learning using the MobileNetV2 architecture to classify fruit types based on image data. The model achieves high accuracy despite the relatively small dataset by leveraging pretrained features from the ImageNet dataset.

## Objective

To classify 9 different fruit categories using image data by training only the top layers of a MobileNetV2 network. The goal is to reach strong generalization with minimal data using transfer learning.

## Dataset

The dataset is available on Kaggle:
[https://www.kaggle.com/datasets/shreyapmaher/fruits-dataset-images](https://www.kaggle.com/datasets/shreyapmaher/fruits-dataset-images)

It contains 9 classes of fruits, including:

* apple
* banana
* cherry
* chickoo
* grapes
* kiwi
* mango
* orange
* strawberry

Each class contains a small number of high-quality `.jpg` images.

### Directory Structure (after preparation)

```
data/
├── train/
│   ├── apple/
│   ├── banana/
│   └── ...
└── test/
    ├── apple/
    ├── banana/
    └── ...
```

## Dataset Preparation

To automatically split the downloaded dataset into training and test folders, run the following script:

```bash
python prepare_dataset.py
```

This script expects the original dataset to be located at:

```
C:/Users/<username>/Downloads/archive/images/
```

It randomly shuffles and copies images into:

* `data/train/`
* `data/test/`

You only need to run this once.

## Model Architecture

The classification model uses the pretrained **MobileNetV2** as a base. The top layers are custom, consisting of:

* `GlobalAveragePooling2D`
* `Dropout(0.3)`
* `Dense(num_classes, activation='softmax')`

The base MobileNetV2 layers are frozen (non-trainable), which allows efficient training on small datasets.

## Training Configuration

* Input shape: (224, 224, 3)
* Optimizer: Adam (learning rate 0.0005)
* Loss: Categorical Crossentropy
* Metric: Accuracy
* EarlyStopping: Enabled (patience = 5)

## Results

The final model reached the following performance:

* **Training Accuracy**: 98%
* **Validation Accuracy**: 90%
* **Epochs Trained**: 30

A graphical plot of training and validation accuracy is displayed at the end of training.

## How to Run

1. **Install Requirements**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Train the Model**:

   ```bash
   python train_transfer.py
   ```

3. **Predict Single Image (Optional)**:
   Place a `.jpg` file in the root folder as `test_image.jpg` and run:

   ```bash
   python predict.py
   ```

## Files

| File                         | Description                                      |
| ---------------------------- | ------------------------------------------------ |
| `model_transfer.py`          | Defines the MobileNetV2-based model architecture |
| `train_transfer.py`          | Loads data and performs model training           |
| `predict.py`                 | Predicts the class of a single image             |
| `prepare_dataset.py`         | Splits original dataset into train/test folders  |
| `requirements.txt`           | Python dependencies                              |
| `README.md`                  | Project documentation                            |
| `fruit_transfer_model.keras` | Trained model output                             |

## Notes

* `.venv/`, `__pycache__/`, and model weights (`.keras`, `.h5`) should be excluded from version control.
* This project was implemented and tested in PyCharm using Python 3.11 and TensorFlow 2.12+.
