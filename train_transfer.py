from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping
from model_transfer import create_transfer_model
import matplotlib.pyplot as plt
import os

# Veri yolları
train_dir = "data/train"
test_dir = "data/test"

# Ayarlar
img_height, img_width = 224, 224  # MobileNetV2 için önerilen boyut
batch_size = 16
epochs = 30

# Veri artırma
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=25,
    zoom_range=0.2,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)
test_datagen = ImageDataGenerator(rescale=1./255)

# Veri yükleme
train_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)
test_data = test_datagen.flow_from_directory(
    test_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)

# Modeli oluştur
model = create_transfer_model(input_shape=(img_height, img_width, 3), num_classes=len(train_data.class_indices))

# Erken durdurma
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Eğitim
history = model.fit(
    train_data,
    epochs=epochs,
    validation_data=test_data,
    callbacks=[early_stop]
)

# Kaydet (.keras)
model.save("fruit_transfer_model.keras")

# Grafik
plt.plot(history.history['accuracy'], label='Train')
plt.plot(history.history['val_accuracy'], label='Validation')
plt.title("Doğruluk")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

# Eğitim Özeti
print("\n--- Eğitim Özeti ---")
for epoch in range(len(history.history['accuracy'])):
    print(f"Epoch {epoch+1}: "
          f"Train Acc = {history.history['accuracy'][epoch]:.2f}, "
          f"Val Acc = {history.history['val_accuracy'][epoch]:.2f}")

print("\nFinal Eğitim Doğruluğu: {:.2f}".format(history.history['accuracy'][-1]))
print("Final Doğrulama Doğruluğu: {:.2f}".format(history.history['val_accuracy'][-1]))
