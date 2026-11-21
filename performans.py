def performans_hesapla(sonuc, islemler):
    # sonuc: [("P1", 0, 8), ...]   islemler: Islem kartları
    toplam_bekleme = 0
    toplam_donus = 0
    toplam_cevap = 0

    for islem in islemler:
        # Bu işlemin sonuç listesindeki parçaları
        parcalar = [p for p in sonuc if p[0] == islem.ad]
        ilk_baslama = parcalar[0][1]       # ilk çalışmaya başladığı an
        bitis = parcalar[-1][2]            # tamamen bittiği an

        donus = bitis - islem.varis        # dönüş süresi
        bekleme = donus - islem.sure       # bekleme süresi
        cevap = ilk_baslama - islem.varis  # cevap süresi

        toplam_bekleme += bekleme
        toplam_donus += donus
        toplam_cevap += cevap

    n = len(islemler)

    # CPU kullanımı: çalışılan süre / (son bitiş - ilk varış)
    calisilan = sum(p[2] - p[1] for p in sonuc)
    ilk_varis = min(i.varis for i in islemler)
    son_bitis = max(p[2] for p in sonuc)
    toplam_sure = son_bitis - ilk_varis

    return {
        "bekleme": toplam_bekleme / n,
        "donus": toplam_donus / n,
        "cevap": toplam_cevap / n,
        "cpu": 100 * calisilan / toplam_sure,
    }
