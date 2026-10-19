from islem import Islem

def dosyadan_oku(dosya_adi):
    islemler = []
    with open(dosya_adi, "r", encoding="utf-8") as f:
        for satir in f:
            satir = satir.strip()
            if satir == "":
                continue
            ad, varis, sure, oncelik = satir.split(",")
            islemler.append(Islem(ad, int(varis), int(sure), int(oncelik)))
    return islemler

islemler = dosyadan_oku("islemler.txt")
print("Okunan işlemler:")
for i in islemler:
    print(i.ad, "varış:", i.varis, "süre:", i.sure, "öncelik:", i.oncelik)