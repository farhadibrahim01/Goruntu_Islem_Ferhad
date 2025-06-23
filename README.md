Here is your **updated and clean `README.md`** for the `Goruntu_Islem_Proje` (Image Processing Project) repository, assuming the `data/` folder (with images) has been removed and users must provide their own dataset.

---

````markdown
# 🍎 Görüntü İşleme ile Meyve Sınıflandırması – Transfer Learning Projesi

Bu proje, transfer öğrenimi (transfer learning) kullanarak farklı meyveleri sınıflandıran bir derin öğrenme modelini içerir. Model, TensorFlow ve Keras kütüphaneleri kullanılarak eğitilmiştir. Proje, eğitim ve test işlemleri ile birlikte tahmin ve veri hazırlama adımlarını da içermektedir.

---

## 🛠️ Gerekli Kütüphaneler

Aşağıdaki kütüphaneleri kurmanız gerekmektedir. `requirements.txt` dosyasını kullanarak otomatik kurulum yapabilirsiniz:

```bash
pip install -r requirements.txt
````

Alternatif olarak manuel:

```bash
pip install tensorflow matplotlib numpy
```

---

## 📁 Klasör Yapısı

```bash
Goruntu_Islem_Proje/
├── model_transfer.py          # Transfer öğrenimi ile modeli eğitme
├── train_transfer.py          # Eğitim işlemlerini başlatan komut
├── predict.py                 # Eğitimli modelle tahmin
├── prepare_dataset.py         # Veriyi eğitim/test klasörlerine ayırır
├── fruit_classifier_model.h5  # Eğitimli model (isteğe bağlı)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📸 Veri Seti (data klasörü artık repoda yok)

Veri seti `.gitignore` ile hariç tutulmuştur. Kullanıcı kendi `data/` klasörünü eklemelidir. Beklenen yapı:

```bash
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

### 📥 Örnek veri:

Kaggle'dan indirilebilir örnek bir veri seti:
[https://www.kaggle.com/datasets/kaggle/fruit-images-for-object-detection](https://www.kaggle.com/datasets/kaggle/fruit-images-for-object-detection)

ZIP olarak indirilen dosyayı `Goruntu_Islem_Proje/data/` klasörüne çıkartın.

---

## ▶️ Eğitim Aşaması

Veri setiniz hazırsa aşağıdaki komutla transfer öğrenimi eğitimi başlatabilirsiniz:

```bash
python train_transfer.py
```

Model `fruit_classifier_model.h5` olarak kayıt edilir.

---

## 🔍 Tahmin (Prediction)

Test klasöründeki bir meyve resmiyle tahmin yapmak için:

```bash
python predict.py
```

Kod çalıştığında, örnek bir görseli sınıflandırır ve matplotlib ile sonucu görselleştirir.

---

## 📦 Dataset Hazırlama (Opsiyonel)

Eğer elinizde karışık halde duran veri varsa, bu script veriyi `train/` ve `test/` klasörlerine ayırmanıza yardımcı olur:

```bash
python prepare_dataset.py
```

Kod, `data/` klasöründeki resimleri otomatik olarak %80 eğitim ve %20 test olarak bölüştürür.

---

## ❗Notlar

* `data/` klasörü `.gitignore` ile korunmuştur, GitHub'a yüklenmez.
* Model dosyaları (`.h5`, `.keras`) da Git'e dahil edilmez.
* Lütfen `.zip`, `.jpg`, `.jpeg`, `.png` gibi dosyaları manuel olarak ekleyin.

---

## 👤 Hazırlayan

**Farhad Ibrahim**
Yapay Zeka / Görüntü İşleme / Transfer Learning
GitHub: [farhadibrahim01](https://github.com/farhadibrahim01)

---

```

> ✅ Bu `README.md` dosyasını doğrudan projenizin kök klasörüne yapıştırabilirsiniz.  
> ✅ Eğer istersen `.md` yerine `.txt` veya `.docx` formatında da sağlayabilirim.

Hazırsanız bir sonraki adımda GitHub'daki ZIP dosyasının boyutunun küçüldüğünü test edebilirsiniz. Yardımcı olmamı ister misiniz?
```
