def round_robin(islemler, dilim):
    # Her işlemin kalan süresini tutan not defteri: {"P1": 8, "P2": 4, ...}
    kalan = {}
    for islem in islemler:
        kalan[islem.ad] = islem.sure

    # İşlemleri varış zamanına göre sırala (önce gelen başta)
    gelecekler = sorted(islemler, key=lambda i: i.varis)

    kuyruk = []      # CPU sırası bekleyen işlemler
    sonuc = []       # (ad, başlama, bitiş) listesi
    zaman = 0        # saat şu an kaç
    sira = 0         # gelecekler listesinde sıradaki kişi

    while sira < len(gelecekler) or len(kuyruk) > 0:

        # 1) Zamanı gelmiş işlemleri kuyruğa al
        while sira < len(gelecekler) and gelecekler[sira].varis <= zaman:
            kuyruk.append(gelecekler[sira])
            sira = sira + 1

        # 2) Kuyruk boşsa CPU boş bekler, saati sıradaki işlemin varışına atla
        if len(kuyruk) == 0:
            zaman = gelecekler[sira].varis
            continue

        # 3) Kuyruğun başındaki işlemi al
        islem = kuyruk.pop(0)

        # 4) En fazla "dilim" kadar çalıştır (işi daha azsa o kadar)
        calisma = min(dilim, kalan[islem.ad])
        baslangic = zaman
        zaman = zaman + calisma
        kalan[islem.ad] = kalan[islem.ad] - calisma
        sonuc.append((islem.ad, baslangic, zaman))

        # 5) Çalışırken yeni gelenleri kuyruğa al (önce onlar girer)
        while sira < len(gelecekler) and gelecekler[sira].varis <= zaman:
            kuyruk.append(gelecekler[sira])
            sira = sira + 1

        # 6) İşi bitmediyse sıranın sonuna geç
        if kalan[islem.ad] > 0:
            kuyruk.append(islem)

    return sonuc
