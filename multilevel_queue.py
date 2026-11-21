from collections import deque

ACIL_ONCELIK = 1   # önceliği 1 olan işlemler acil kuyruğa gider
QUANTUM = 2        # acil kuyruktaki Round Robin'in süre dilimi


def acil_mi(islem):
    return islem.oncelik == ACIL_ONCELIK


def parca_ekle(sonuc, ad, baslangic, bitis):
    # Aynı işlem kesintisiz devam ediyorsa yeni parça açma, son parçayı uzat
    if sonuc and sonuc[-1][0] == ad and sonuc[-1][2] == baslangic:
        sonuc[-1] = (ad, sonuc[-1][1], bitis)
    else:
        sonuc.append((ad, baslangic, bitis))


def multilevel_queue(islemler):
    gelecekler = sorted(islemler, key=lambda i: i.varis)  # henüz gelmemiş işlemler
    kalan = {i.ad: i.sure for i in islemler}               # her işlemin kalan süresi
    acil_kuyruk = deque()
    normal_kuyruk = deque()
    sonuc = []

    zaman = 0
    calisan = None   # şu an CPU'daki işlem
    dilim = 0        # çalışan işlem bu turda kaç birim çalıştı (Round Robin için)

    def gelenleri_al():
        while gelecekler and gelecekler[0].varis <= zaman:
            islem = gelecekler.pop(0)
            if acil_mi(islem):
                acil_kuyruk.append(islem)
            else:
                normal_kuyruk.append(islem)

    while gelecekler or acil_kuyruk or normal_kuyruk or calisan:
        # 1) Bu ana kadar gelen işlemleri kuyruklarına koy
        gelenleri_al()

        # 2) Kesme: normal işlem çalışıyorken acil iş gelirse normal işlem bekler
        if calisan and not acil_mi(calisan) and acil_kuyruk:
            normal_kuyruk.appendleft(calisan)
            calisan = None

        # 3) CPU boşsa sıradakini seç (önce acil, sonra normal)
        if calisan is None:
            if acil_kuyruk:
                calisan = acil_kuyruk.popleft()
            elif normal_kuyruk:
                calisan = normal_kuyruk.popleft()
            else:
                zaman += 1   # kimse yok, CPU boşta bekler
                continue
            dilim = 0

        # 4) Seçilen işlemi 1 birim çalıştır
        parca_ekle(sonuc, calisan.ad, zaman, zaman + 1)
        kalan[calisan.ad] -= 1
        dilim += 1
        zaman += 1

        # 5) İşlem bitti mi, ya da acil işlemin süre dilimi doldu mu?
        if kalan[calisan.ad] == 0:
            calisan = None
        elif acil_mi(calisan) and dilim == QUANTUM:
            gelenleri_al()                 # bu anda gelenler önce sıraya girer
            acil_kuyruk.append(calisan)    # sonra süresi dolan işlem sona geçer
            calisan = None

    return sonuc


if __name__ == "__main__":
    from islem import Islem

    print("Test 1: repodaki örnek veri")
    islemler = [
        Islem("P1", 0, 8, 1),
        Islem("P2", 1, 4, 2),
        Islem("P3", 2, 2, 1),
    ]
    for parca in multilevel_queue(islemler):
        print(parca)

    print()
    print("Test 2: acil işlem, çalışan normal işlemi böler")
    islemler = [
        Islem("N1", 0, 5, 2),
        Islem("A1", 2, 3, 1),
    ]
    for parca in multilevel_queue(islemler):
        print(parca)

    print()
    print("Test 3: CPU boş kalırsa saat atlar")
    islemler = [
        Islem("P1", 0, 2, 2),
        Islem("P2", 5, 3, 1),
    ]
    for parca in multilevel_queue(islemler):
        print(parca)

    print()
    print("Test 4: acil kuyrukta Round Robin")
    islemler = [
        Islem("A1", 0, 3, 1),
        Islem("A2", 0, 3, 1),
    ]
    for parca in multilevel_queue(islemler):
        print(parca)
