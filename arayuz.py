import tkinter as tk
from tkinter import messagebox
from gantt import gantt_ciz  # Yazdığımız Gantt şeması fonksiyonunu buraya bağlıyoruz

# Kullanıcının arayüzden ekleyeceği işlemleri tutacak liste
islemler = []

def pencere_ac():
    pencere = tk.Tk()
    pencere.title("CPU Zamanlama Simülatörü")
    pencere.geometry("500x520")

    # 1. Başlık
    baslik = tk.Label(pencere, text="CPU Zamanlama Simülatörü", font=("Arial", 14, "bold"))
    baslik.pack(pady=10)

    # 2. Veri Giriş Alanı (Çerçeve içinde düzenli dursun)
    giris_cercevesi = tk.Frame(pencere)
    giris_cercevesi.pack(pady=5)

    tk.Label(giris_cercevesi, text="İşlem Adı (Örn: P1):").grid(row=0, column=0, padx=5, pady=5)
    giris_ad = tk.Entry(giris_cercevesi, width=15)
    giris_ad.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(giris_cercevesi, text="Varış Zamanı (sn):").grid(row=1, column=0, padx=5, pady=5)
    giris_varis = tk.Entry(giris_cercevesi, width=15)
    giris_varis.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(giris_cercevesi, text="Çalışma Süresi (sn):").grid(row=2, column=0, padx=5, pady=5)
    giris_sure = tk.Entry(giris_cercevesi, width=15)
    giris_sure.grid(row=2, column=1, padx=5, pady=5)

    # 3. Eklenen İşlemleri Gösteren Liste
    liste_kutusu = tk.Listbox(pencere, width=45, height=6)
    liste_kutusu.pack(pady=10)

    # Buton Fonksiyonu: Girilen işlemi listeye ekler
    def islem_ekle():
        ad = giris_ad.get().strip()
        varis = giris_varis.get().strip()
        sure = giris_sure.get().strip()

        # Boş alan veya sayı yerine harf girilirse uyar
        if not ad or not varis.isdigit() or not sure.isdigit():
            messagebox.showwarning("Hata", "Lütfen geçerli işlem adı ve sayısal süreler girin!")
            return

        islemler.append((ad, int(varis), int(sure)))
        liste_kutusu.insert(tk.END, f"{ad}  |  Varış: {varis} sn  |  Süre: {sure} sn")

        # Kutuları temizle
        giris_ad.delete(0, tk.END)
        giris_varis.delete(0, tk.END)
        giris_sure.delete(0, tk.END)

    # Buton Fonksiyonu: Listeyi tamamen sıfırlar
    def listeyi_temizle():
        islemler.clear()
        liste_kutusu.delete(0, tk.END)

    # Ekleme ve Temizleme Butonları
    islem_buton_cerceve = tk.Frame(pencere)
    islem_buton_cerceve.pack(pady=5)

    tk.Button(islem_buton_cerceve, text="İşlem Ekle", command=islem_ekle, width=15).grid(row=0, column=0, padx=5)
    tk.Button(islem_buton_cerceve, text="Listeyi Temizle", command=listeyi_temizle, width=15).grid(row=0, column=1, padx=5)

    # 4. Algoritma Çalıştırma Butonları
    tk.Label(pencere, text="Algoritma Seç ve Simülasyonu Başlat:", font=("Arial", 11, "bold")).pack(pady=(15, 5))

    algo_cerceve = tk.Frame(pencere)
    algo_cerceve.pack(pady=5)

    def algoritma_calistir(algo_adi):
        if not islemler:
            messagebox.showwarning("Uyarı", "Önce en az bir işlem eklemelisiniz!")
            return

        # Şimdilik girilen işlemleri arka arkaya sıralayıp Gantt şemasına gönderiyoruz.
        # Arkadaşların algoritma dosyalarını bitirdiğinde burayı onların fonksiyonlarına bağlayacağız.
        zaman = 0
        gantt_verisi = []
        for ad, varis, sure in islemler:
            if zaman < varis:
                zaman = varis
            gantt_verisi.append((ad, zaman, zaman + sure))
            zaman += sure

        gantt_ciz(gantt_verisi)

    tk.Button(algo_cerceve, text="FCFS Çalıştır", width=18, command=lambda: algoritma_calistir("FCFS")).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(algo_cerceve, text="SJF Çalıştır", width=18, command=lambda: algoritma_calistir("SJF")).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(algo_cerceve, text="Round Robin Çalıştır", width=18, command=lambda: algoritma_calistir("RR")).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(algo_cerceve, text="Multilevel Queue", width=18, command=lambda: algoritma_calistir("MLQ")).grid(row=1, column=1, padx=5, pady=5)

    pencere.mainloop()

if __name__ == "__main__":
    pencere_ac()
