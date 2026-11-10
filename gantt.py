import matplotlib.pyplot as plt

def gantt_ciz(sonuc):
    adlar = []
    for ad, baslama, bitis in sonuc:
        if ad not in adlar:
            adlar.append(ad)

    sekil, eksen = plt.subplots()

    for ad, baslama, bitis in sonuc:
        satir = adlar.index(ad)
        eksen.barh(satir, bitis - baslama, left=baslama)

    eksen.set_yticks(range(len(adlar)))
    eksen.set_yticklabels(adlar)
    eksen.set_xlabel("Zaman (saniye)")
    eksen.set_title("Gantt Şeması")
    plt.show()

if __name__ == "__main__":
    ornek_veri = [("P1", 0, 8), ("P2", 8, 12), ("P1", 12, 15)]
    gantt_ciz(ornek_veri)
