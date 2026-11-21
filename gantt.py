import matplotlib.pyplot as plt

def _ciz(eksen, sonuc, baslik):
    # Her işleme bir satır veriyoruz (P1 -> 0, P2 -> 1 ...)
    adlar = []
    for ad, baslama, bitis in sonuc:
        if ad not in adlar:
            adlar.append(ad)
    for ad, baslama, bitis in sonuc:
        eksen.barh(adlar.index(ad), bitis - baslama, left=baslama, edgecolor="black")
    eksen.set_yticks(range(len(adlar)))
    eksen.set_yticklabels(adlar)
    eksen.set_xlabel("Zaman (saniye)")
    eksen.set_title(baslik)

def gantt_ciz(sonuc, baslik="Gantt Şeması", goster=True):
    sekil, eksen = plt.subplots()
    _ciz(eksen, sonuc, baslik)
    if goster:
        plt.show()
    return sekil

def gantt_hepsi(sonuclar, goster=True):
    # sonuclar: {"FCFS": [...], "SJF": [...], ...} hepsini alt alta çizer
    sekil, eksenler = plt.subplots(len(sonuclar), 1, figsize=(8, 2.5 * len(sonuclar)))
    for eksen, (ad, sonuc) in zip(eksenler, sonuclar.items()):
        _ciz(eksen, sonuc, ad)
    sekil.tight_layout()
    if goster:
        plt.show()
    return sekil
