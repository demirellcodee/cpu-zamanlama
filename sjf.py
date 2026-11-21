def sjf(islemler):
    bekleyenler = list(islemler)   
    sonuc = []
    zaman = 0

    while len(bekleyenler) > 0:
       
        hazir = []
        for islem in bekleyenler:
            if islem.varis <= zaman:
                hazir.append(islem)

      
        if len(hazir) == 0:
            en_erken = min(i.varis for i in bekleyenler)
            zaman = en_erken
            continue

     
        secilen = min(hazir, key=lambda i: (i.sure, i.varis))
        bekleyenler.remove(secilen)

        baslama = zaman
        zaman = zaman + secilen.sure
        sonuc.append((secilen.ad, baslama, zaman))

    return sonuc
