import tkinter as tk

def pencere_ac():
    # 1. Ana pencereyi oluşturuyoruz
    pencere = tk.Tk()
    pencere.title("CPU Zamanlama Simülatörü")
    pencere.geometry("400x300")

    # 2. Pencere içine bir karşılama yazısı ekliyoruz
    etiket = tk.Label(pencere, text="CPU Zamanlama Simülatörüne Hoş Geldiniz!")
    etiket.pack(pady=20)

    # 3. Pencerenin ekranda açık kalmasını sağlıyoruz
    pencere.mainloop()

# TEST BÖLÜMÜ: Dosyayı doğrudan çalıştırırsak pencereyi açar
if __name__ == "__main__":
    pencere_ac()
