import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from islem import Islem
from girdi import dosyadan_oku
from fcfs import fcfs
from sjf import sjf
from round_robin import round_robin
from multilevel_queue import multilevel_queue
from performans import performans_hesapla
from gantt import _ciz

class Uygulama:
    def __init__(self, pencere):
        self.pencere = pencere
        pencere.title("CPU Zamanlama Simülatörü")
        pencere.geometry("950x780")

        # --- Üst kısım: işlem girişi ---
        giris = tk.LabelFrame(pencere, text="İşlem ekle")
        giris.pack(fill="x", padx=10, pady=5)

        self.kutular = {}
        for sutun, ad in enumerate(["Ad", "Varış", "Süre", "Öncelik"]):
            tk.Label(giris, text=ad).grid(row=0, column=sutun, padx=5)
            kutu = tk.Entry(giris, width=8)
            kutu.grid(row=1, column=sutun, padx=5, pady=5)
            self.kutular[ad] = kutu
        tk.Button(giris, text="Ekle", command=self.islem_ekle).grid(row=1, column=4, padx=5)
        tk.Button(giris, text="Dosyadan yükle", command=self.dosyadan_yukle).grid(row=1, column=5, padx=5)
        tk.Button(giris, text="Temizle", command=self.temizle).grid(row=1, column=6, padx=5)

        # --- İşlem listesi ---
        self.liste = tk.Listbox(pencere, height=5)
        self.liste.pack(fill="x", padx=10)

        # --- Algoritma seçimi ---
        secim = tk.Frame(pencere)
        secim.pack(fill="x", padx=10, pady=5)
        tk.Label(secim, text="Algoritma:").pack(side="left")
        self.algoritma = ttk.Combobox(secim, state="readonly", width=20,
                                      values=["FCFS", "SJF", "Round Robin", "Multilevel Queue", "Hepsini karşılaştır"])
        self.algoritma.current(0)
        self.algoritma.pack(side="left", padx=5)
        tk.Label(secim, text="Süre dilimi:").pack(side="left")
        self.dilim = tk.Entry(secim, width=5)
        self.dilim.insert(0, "2")
        self.dilim.pack(side="left", padx=5)
        tk.Button(secim, text="Çalıştır", command=self.calistir).pack(side="left", padx=10)

        # --- Sonuç yazısı ---
        self.sonuc_yazi = tk.Text(pencere, height=6)
        self.sonuc_yazi.pack(fill="x", padx=10)

        # --- Gantt çizim alanı ---
        self.sekil = Figure(figsize=(8, 3))
        self.cizim = FigureCanvasTkAgg(self.sekil, master=pencere)
        self.cizim.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=5)

        self.islemler = []

    # --- İşlem listesi işlemleri ---
    def liste_yenile(self):
        self.liste.delete(0, tk.END)
        for i in self.islemler:
            self.liste.insert(tk.END, "%s  varış=%d  süre=%d  öncelik=%d" % (i.ad, i.varis, i.sure, i.oncelik))

    def islem_ekle(self):
        try:
            ad = self.kutular["Ad"].get().strip()
            varis = int(self.kutular["Varış"].get())
            sure = int(self.kutular["Süre"].get())
            oncelik = int(self.kutular["Öncelik"].get() or 0)
        except ValueError:
            messagebox.showerror("Hata", "Varış, süre ve öncelik tam sayı olmalı.")
            return
        if ad == "" or sure <= 0 or varis < 0:
            messagebox.showerror("Hata", "Ad boş olamaz, süre 0'dan büyük olmalı.")
            return
        if ad in [i.ad for i in self.islemler]:
            messagebox.showerror("Hata", "Bu ad zaten var, işlem adları benzersiz olmalı.")
            return
        self.islemler.append(Islem(ad, varis, sure, oncelik))
        self.liste_yenile()
        for kutu in self.kutular.values():
            kutu.delete(0, tk.END)

    def dosyadan_yukle(self):
        try:
            self.islemler = dosyadan_oku("islemler.txt")
        except Exception as hata:
            messagebox.showerror("Hata", "islemler.txt okunamadı: %s" % hata)
            return
        self.liste_yenile()

    def temizle(self):
        self.islemler = []
        self.liste_yenile()

    # --- Çalıştırma ---
    def sonuclari_hesapla(self, secilen, dilim):
        if secilen == "FCFS":
            return {"FCFS": fcfs(self.islemler)}
        if secilen == "SJF":
            return {"SJF": sjf(self.islemler)}
        if secilen == "Round Robin":
            return {"Round Robin": round_robin(self.islemler, dilim)}
        if secilen == "Multilevel Queue":
            return {"Multilevel Queue": multilevel_queue(self.islemler)}
        return {
            "FCFS": fcfs(self.islemler),
            "SJF": sjf(self.islemler),
            "Round Robin": round_robin(self.islemler, dilim),
            "Multilevel Queue": multilevel_queue(self.islemler),
        }

    def calistir(self):
        if len(self.islemler) == 0:
            messagebox.showerror("Hata", "Önce işlem ekleyin ya da dosyadan yükleyin.")
            return
        try:
            dilim = int(self.dilim.get())
            if dilim <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Hata", "Süre dilimi 0'dan büyük bir tam sayı olmalı.")
            return

        sonuclar = self.sonuclari_hesapla(self.algoritma.get(), dilim)

        # Yazı tablosu
        self.sonuc_yazi.delete("1.0", tk.END)
        self.sonuc_yazi.insert(tk.END, "%-18s %9s %9s %9s %9s\n" % ("Algoritma", "Bekleme", "Dönüş", "Cevap", "CPU %"))
        for ad, sonuc in sonuclar.items():
            p = performans_hesapla(sonuc, self.islemler)
            self.sonuc_yazi.insert(tk.END, "%-18s %9.2f %9.2f %9.2f %9.1f\n" % (ad, p["bekleme"], p["donus"], p["cevap"], p["cpu"]))

        # Gantt çizimi
        self.sekil.clear()
        eksenler = self.sekil.subplots(len(sonuclar), 1, squeeze=False)
        for satir, (ad, sonuc) in enumerate(sonuclar.items()):
            _ciz(eksenler[satir][0], sonuc, ad)
        self.sekil.subplots_adjust(left=0.12, right=0.97, top=0.93, bottom=0.12, hspace=1.1)
        self.cizim.draw()

def pencere_ac():
    pencere = tk.Tk()
    Uygulama(pencere)
    pencere.mainloop()

if __name__ == "__main__":
    pencere_ac()
