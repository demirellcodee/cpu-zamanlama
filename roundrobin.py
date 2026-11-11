# round_robin(islemler, kuantum) → Gantt listesi döndürür
# Her eleman: (işlem_adı, başlangıç_zamanı, bitiş_zamanı)
def round_robin(islemler, kuantum=3):
    # 1) İşlemleri varış sırasına göre sırala
    islemler_sirali = sorted(islemler, key=lambda x: x.varis)
    # 2) Her işlemin ne kadar CPU süresi kaldığını tut
    kalan = {i.ad: i.sure for i in islemler_sirali}
    kuyruk   = []   # Hazır kuyruk (çalışmayı bekleyenler)
    sonuclar = []   # Gantt chart: [(ad, baslangic, bitis), ...]
    zaman    = 0    # Şu anki CPU saati
    index    = 0    # Sıradaki eklenmemiş işlem
    # 3) Başta zaten gelmiş olan işlemleri kuyruğa ekle
    while index < len(islemler_sirali) and islemler_sirali[index].varis <= zaman:
        kuyruk.append(islemler_sirali[index])
        index += 1
    # 4) Ana döngü: kuyruk veya bekleyen işlem varken çalış
    while kuyruk or index < len(islemler_sirali):
        if not kuyruk:
            # CPU boş → bir sonraki işlemin gelmesini bekle (zaman atla)
            zaman = islemler_sirali[index].varis
            while index < len(islemler_sirali) and islemler_sirali[index].varis <= zaman:
