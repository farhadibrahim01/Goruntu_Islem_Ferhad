import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

# Kaynak klasör (şu anda tüm meyvelerin olduğu yer)
source_dir = Path(r"C:\Users\Ferhad Ibrahimov\Downloads\archive (5)\images")

# Hedef klasörler
train_dir = Path("data/train")
test_dir = Path("data/test")

# Her sınıf için işlemleri yap
for fruit_folder in source_dir.iterdir():
    if fruit_folder.is_dir():
        # Klasör adı sadeleştirme: "apple fruit" → "apple"
        class_name = fruit_folder.name.lower().replace(" fruit", "").strip()

        # Tüm görselleri oku
        images = list(fruit_folder.glob("*.jpg"))
        train_imgs, test_imgs = train_test_split(images, test_size=0.2, random_state=42)

        # Klasörleri oluştur
        (train_dir / class_name).mkdir(parents=True, exist_ok=True)
        (test_dir / class_name).mkdir(parents=True, exist_ok=True)

        # Resimleri kopyala
        for img in train_imgs:
            shutil.copy(img, train_dir / class_name / img.name)

        for img in test_imgs:
            shutil.copy(img, test_dir / class_name / img.name)

        print(f"✓ {class_name} → Train: {len(train_imgs)} | Test: {len(test_imgs)}")
