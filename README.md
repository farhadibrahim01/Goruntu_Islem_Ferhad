Görüntü İşleme ile Meyve Sınıflandırması – Transfer Learning Projesi

Bu proje, transfer öğrenimi (transfer learning) kullanarak farklı meyveleri sınıflandıran bir derin öğrenme modelini içerir. TensorFlow ve Keras kütüphaneleri kullanılarak geliştirilmiştir. Eğitim, test, tahmin ve veri hazırlama adımları dahil edilmiştir.

Gerekli Kütüphaneler

Aşağıdaki kütüphanelerin kurulması gerekmektedir. requirements.txt dosyasını kullanarak otomatik kurulum yapılabilir:

pip install -r requirements.txt

Alternatif olarak manuel kurulum:

pip install tensorflow matplotlib numpy

Klasör Yapısı

Goruntu_Islem_Proje/
├── model_transfer.py
├── train_transfer.py
├── predict.py
├── prepare_dataset.py
├── fruit_classifier_model.h5
├── requirements.txt
├── .gitignore
└── README.md

Veri Seti (data klasörü repoda yoktur)

data/ klasörü .gitignore ile hariç tutulmuştur. Kullanıcının kendi verisini eklemesi gerekir. Beklenen yapı şu şekildedir:

data/
├── train/
│ ├── apple/
│ ├── banana/
│ └── ...
└── test/
├── apple/
├── banana/
└── ...

Örnek veri seti Kaggle üzerinden indirilebilir:
https://www.kaggle.com/datasets/kaggle/fruit-images-for-object-detection

İndirilen ZIP dosyası "Goruntu_Islem_Proje/data/" klasörüne çıkarılmalıdır.

Modeli Eğitme

Veri seti hazırlandıktan sonra transfer learning modeli şu komutla eğitilir:

python train_transfer.py

Model dosyası fruit_classifier_model.h5 olarak kaydedilir.

Tahmin (Prediction)

Test klasöründe bulunan meyve görselleri ile tahmin yapmak için:

python predict.py

Kod bir görseli sınıflandırır ve sonucu matplotlib ile gösterir.

Veri Hazırlama (Opsiyonel)

Eğer elinizde karışık bir veri yapısı varsa, prepare_dataset.py dosyası veriyi train/ ve test/ klasörlerine %80 - %20 oranında böler:

python prepare_dataset.py

Önemli Notlar

data/ klasörü .gitignore içinde olduğu için GitHub'a yüklenmemektedir.

Model çıktısı olan .h5 ve .keras dosyaları da yüklenmemektedir.

.jpg, .jpeg, .png gibi resim dosyaları manuel olarak eklenmelidir.

Hazırlayan

Farhad Ibrahim
Yapay Zeka, Görüntü İşleme, Transfer Learning
GitHub: https://github.com/farhadibrahim01

