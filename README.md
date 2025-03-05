# GUI
# Dijital Görüntü İşleme Uygulaması

Bu proje, Dijital Görüntü İşleme dersi kapsamında geliştirilmiş bir PyQt5 tabanlı masaüstü uygulamasıdır. Kullanıcılar, farklı görüntü işleme tekniklerini uygulayarak fotoğraflarını düzenleyebilir ve analiz edebilirler.

## Özellikler
- **Görüntü Yükleme ve Kaydetme**: Kullanıcı, yerel dosyalardan bir görüntü yükleyebilir ve işlenmiş görüntüyü kaydedebilir.
- **Filtreleme İşlemleri**: Gri tonlama, bulanıklaştırma, keskinleştirme ve ortalama/medyan filtreleri.
- **Dönüşümler**: Görüntüyü döndürme, yatay ve dikey çevirme.
- **Kenar Algılama**: Canny algoritması ile kenar tespiti.
- **Histogram İşlemleri**: Histogram eşitleme ve görüntü histogramını görüntüleme.
- **Renk Dönüşümleri**: RGB-HSV dönüşümleri.
- **Kontrast ve Parlaklık Ayarı**: Kullanıcı, kaydırıcılar ile kontrast ve parlaklık seviyelerini değiştirebilir.

## Kurulum

### Gerekli Bağımlılıklar
Projeyi çalıştırmak için aşağıdaki bağımlılıkları yüklemeniz gerekmektedir:

```bash
pip install PyQt5 opencv-python numpy matplotlib
```

### Çalıştırma
Projeyi başlatmak için terminalde aşağıdaki komutu çalıştırabilirsiniz:

```bash
python GUI.py
```

## Kullanım
1. **Görüntü Yükleme**: "Görüntü Yükle" butonuna basarak bir görüntü seçin.
2. **Görüntü İşleme**: Farklı işlemleri gerçekleştirmek için ilgili butonlara tıklayın.
3. **Sonucu Kaydetme**: İşlenmiş görüntüyü kaydetmek için "Görüntüyü Kaydet" seçeneğini kullanın.
4. **Ödev Sekmeleri**: Beş farklı ödev sekmesine erişerek ilgili işlemleri gerçekleştirin.

## Öğrenci Bilgileri
- **Adı**: Kerim Serkan Şahin
- **Öğrenci Numarası**: 221229040
- **Ders**: Dijital Görüntü İşleme

## Lisans
Bu proje eğitim amaçlı geliştirilmiştir ve açık kaynak olarak paylaşılmaktadır.

