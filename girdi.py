from islem import Islem

def dosyadan_oku(dosya_adi):
    # Dosyadaki her satırı (P1,0,8,1) bir Islem kartına çevirir
    islemler = []
    with open(dosya_adi, "r", encoding="utf-8") as f:
        for satir in f:
            satir = satir.strip()
            if satir == "":
                continue
            ad, varis, sure, oncelik = satir.split(",")
            islemler.append(Islem(ad, int(varis), int(sure), int(oncelik)))
    return islemler
