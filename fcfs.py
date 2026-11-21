def fcfs(islemler):
  
    sirali = sorted(islemler, key=lambda i: i.varis)

    sonuc = []
    zaman = 0  

    for islem in sirali:
     
        if zaman < islem.varis:
            zaman = islem.varis

        baslama = zaman
        zaman = zaman + islem.sure     
        sonuc.append((islem.ad, baslama, zaman))

    return sonuc
