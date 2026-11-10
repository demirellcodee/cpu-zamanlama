import matplotlib.pyplot as plt  # Grafik çizimi için Matplotlib kütüphanesini ekliyoruz

def gantt_ciz(sonuc):
    # 1. Gelen veriden benzersiz işlem isimlerini (P1, P2 vb.) çıkarıyoruz
    adlar = []
    for ad, baslama, bitis in sonuc:
        if ad not in adlar:
            adlar.append(ad)  # Listede yoksa ekle (çiftlemeyi önle)

    # 2. Grafik penceresini ve koordinat eksenini oluşturuyoruz
    sekil, eksen = plt.subplots()

    # 3. Her bir işlemi zaman eksenine yatay çubuk (barh) olarak yerleştiriyoruz
    for ad, baslama, bitis in sonuc:
        satir = adlar.index(ad)  # İşlemin dikeydeki satır indeksini buluyoruz
        eksen.barh(satir, bitis - baslama, left=baslama)  # Yükseklik, Genişlik (Süre), Başlangıç Saniyesi

    # 4. Eksen etiketlerini ve başlıkları ayarlıyoruz
    eksen.set_yticks(range(len(adlar)))  # Y eksenine işlem sayısı kadar çentik koy
    eksen.set_yticklabels(adlar)         # Çentiklerin yanına işlem isimlerini yaz (P1, P2)
    eksen.set_xlabel("Zaman (saniye)")   # Yatay eksen ismi
    eksen.set_title("Gantt Şeması")      # Grafik ana başlığı
    plt.show()                           # Grafiği ekranda göster

# TEST BÖLÜMÜ: Dosyayı doğrudan çalıştırırsak örnek veriyi çizer
if __name__ == "__main__":
    ornek_veri = [("P1", 0, 8), ("P2", 8, 12), ("P1", 12, 15)]  # (İşlem Adı, Başlama, Bitiş)
    gantt_ciz(ornek_veri)
