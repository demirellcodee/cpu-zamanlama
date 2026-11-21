def multilevel_queue(islemler, esik=1):
    # İki kuyruk var:
    #   Acil kuyruk   : önceliği esik veya daha küçük olanlar (1 = en acil)
    #   Normal kuyruk : diğerleri
    # CPU boşalınca önce acil kuyruğa bakılır. Acilde gelmiş iş varsa o çalışır.
    # Yoksa normal kuyruktan çalışır. Her kuyruk kendi içinde FCFS'dir.
    acil = sorted([i for i in islemler if i.oncelik <= esik], key=lambda i: i.varis)
    normal = sorted([i for i in islemler if i.oncelik > esik], key=lambda i: i.varis)

    sonuc = []
    zaman = 0

    while len(acil) > 0 or len(normal) > 0:
        # Acil kuyrukta gelmiş iş var mı?
        if len(acil) > 0 and acil[0].varis <= zaman:
            secilen = acil.pop(0)
        # Yoksa normal kuyrukta gelmiş iş var mı?
        elif len(normal) > 0 and normal[0].varis <= zaman:
            secilen = normal.pop(0)
        else:
            # Kimse gelmedi, saati ilk gelecek işe atla
            gelecekler = []
            if len(acil) > 0:
                gelecekler.append(acil[0].varis)
            if len(normal) > 0:
                gelecekler.append(normal[0].varis)
            zaman = min(gelecekler)
            continue

        baslama = zaman
        zaman = zaman + secilen.sure
        sonuc.append((secilen.ad, baslama, zaman))

    return sonuc
