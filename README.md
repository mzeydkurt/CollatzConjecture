# Collatz Hipotezi Görselleştirme Projesi

Bu proje, Collatz hipotezinin Python ile uygulanmasını ve sonuçların görselleştirilmesini içerir. Kullanıcıdan alınan bir sayı için Collatz dizisini hesaplar ve bu diziyi bir grafik üzerinde gösterir.

## 📖 Collatz Hipotezi Nedir?

Collatz hipotezi, pozitif bir tam sayı üzerinde şu işlemleri yapar:
1. Eğer sayı **çift** ise, 2'ye bölünür. (n → n / 2)
2. Eğer sayı **tek** ise, 3 ile çarpılır ve 1 eklenir. (n → 3n + 1)
3. Bu işlemler, sayı 1 olana kadar devam eder.

Bu hipoteze göre, hangi pozitif sayıdan başlanırsa başlansın, sonuç her zaman 1 olacaktır. Ancak bu durum matematiksel olarak henüz kanıtlanmamıştır.

## 🚀 Özellikler

- Kullanıcıdan bir sayı alır ve Collatz dizisini hesaplar.
- Diziyi **Matplotlib** kullanarak görselleştirir.
- Birden fazla sayı için aynı grafikte karşılaştırma yapabilme imkanı sunar.

## 🛠️ Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılımlara ihtiyacınız var:

- Python 3.x
- Gerekli kütüphaneler:
  - `matplotlib`

Kütüphaneleri yüklemek için:
```bash
pip install matplotlib
