from girdi import dosyadan_oku
from fcfs import fcfs
from sjf import sjf
from roundrobin import round_robin
from multilevelqueue import multilevel_queue
from performans import performans_hesapla
from gantt import gantt_hepsi

DILIM = 2   # Round Robin süre dilimi

def tum_algoritmalari_calistir(islemler):
    return {
        "FCFS": fcfs(islemler),
        "SJF": sjf(islemler),
        "Round Robin (dilim=%d)" % DILIM: round_robin(islemler, DILIM),
        "Multilevel Queue": multilevel_queue(islemler),
    }

def tablo_yazdir(sonuclar, islemler):
    print("%-24s %9s %9s %9s %9s" % ("Algoritma", "Bekleme", "Dönüş", "Cevap", "CPU %"))
    for ad, sonuc in sonuclar.items():
        p = performans_hesapla(sonuc, islemler)
        print("%-24s %9.2f %9.2f %9.2f %9.1f" % (ad, p["bekleme"], p["donus"], p["cevap"], p["cpu"]))

if __name__ == "__main__":
    islemler = dosyadan_oku("islemler.txt")
    print("Okunan işlemler:")
    for i in islemler:
        print(i.ad, "varış:", i.varis, "süre:", i.sure, "öncelik:", i.oncelik)
    print()

    sonuclar = tum_algoritmalari_calistir(islemler)
    for ad, sonuc in sonuclar.items():
        print(ad, ":", sonuc)
    print()
    tablo_yazdir(sonuclar, islemler)

    gantt_hepsi(sonuclar)
