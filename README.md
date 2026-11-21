# CPU Zamanlama Algoritmaları Simülatörü

BİM 361 İşletim Sistemleri dersi dönem projesi (2026-2027 Güz).

## Ne yapar?

Verilen işlem listesini dört CPU zamanlama algoritmasıyla zamanlar, sonucu Gantt şemasıyla gösterir ve algoritmaları dört ölçüte göre karşılaştırır:

- **Algoritmalar:** FCFS, SJF, Round Robin, Multilevel Queue
- **Ölçütler:** ortalama bekleme süresi, ortalama dönüş süresi, ortalama cevap süresi, CPU kullanım oranı

## Gereksinimler

- Python 3
- Matplotlib: `pip install matplotlib`
- Tkinter (arayüz için): Python ile birlikte gelir, ayrıca kurulum gerekmez

## Nasıl çalıştırılır?

1. Repoyu indirin (Code → Download ZIP) ve klasöre çıkarın. Dosyaların hepsi **aynı klasörde** olmalıdır.
2. Klasörde bir terminal açın.
3. Matplotlib'i bir kere kurun:

```
pip install matplotlib
```

**Komut satırı sürümü** (tablo + Gantt şeması):

```
python main.py
```

Terminalde her algoritmanın sonucu ve karşılaştırma tablosu yazılır, ardından ayrı bir pencerede dört Gantt şeması açılır.

**Arayüzlü sürüm** (Tkinter):

```
python arayuz.py
```

Pencerede işlem ekleyebilir ya da "Dosyadan yükle" ile `islemler.txt` dosyasını okuyabilir, algoritmayı seçip "Çalıştır"a basabilirsiniz. "Hepsini karşılaştır" seçeneği dört algoritmayı birlikte çalıştırır.

## Girdi formatı (islemler.txt)

Her satır bir işlemdir: `ad,varış zamanı,çalışma süresi,öncelik`

```
P1,0,8,1
P2,1,4,2
P3,2,2,1
```

Kurallar:

- Başlık satırı yazılmaz.
- Varış, süre ve öncelik **tam sayı** olmalıdır; süre 0'dan büyük olmalıdır.
- İşlem adları benzersiz olmalıdır.
- Her satırda dört değer bulunmalıdır. Boş satırlar atlanır.
- Multilevel Queue için öncelik 1 acil kuyruğa, 2 ve üzeri normal kuyruğa girer.

## Örnek çıktı

Yukarıdaki üç işlem ve Round Robin süre dilimi 2 için:

```
Algoritma                  Bekleme     Dönüş     Cevap     CPU %
FCFS                          5.67     10.33      5.67     100.0
SJF                           5.00      9.67      5.00     100.0
Round Robin (dilim=2)         4.33      9.00      1.00     100.0
Multilevel Queue              5.00      9.67      5.00     100.0
```

## Dosyalar

| Dosya | Görevi |
|---|---|
| `islem.py` | İşlem sınıfı (ad, varış, süre, öncelik) |
| `islemler.txt` | Örnek girdi dosyası |
| `girdi.py` | Girdi dosyasını okuyup işlem nesnelerine çevirir |
| `fcfs.py` | FCFS algoritması |
| `sjf.py` | SJF algoritması |
| `round_robin.py` | Round Robin algoritması |
| `multilevel_queue.py` | Multilevel Queue algoritması |
| `performans.py` | Bekleme, dönüş, cevap süresi ve CPU kullanımı hesabı |
| `gantt.py` | Matplotlib ile Gantt şeması çizimi |
| `arayuz.py` | Tkinter arayüzü |
| `main.py` | Tüm algoritmaları çalıştırır, tabloyu ve Gantt şemalarını gösterir |

## Ortak sözleşme

Her algoritma işlem listesini alır ve sonucu şu biçimde döndürür:

```python
[("P1", 0, 8), ("P2", 8, 12), ("P3", 12, 14)]
```

Her eleman `(işlem adı, başlama zamanı, bitiş zamanı)` demektir. Round Robin'de aynı işlem birden fazla satırda görünebilir. Performans hesapları ve Gantt çizimi yalnızca bu listeyi kullanır.

## Algoritmalar

- **FCFS:** İşlemler geliş sırasına göre çalışır, başlayan işlem bitene kadar kesilmez.
- **SJF:** İşlemci boşaldığında, o ana kadar gelmiş işlemler arasından süresi en kısa olan seçilir (kesmesiz). Süreler eşitse önce gelen seçilir.
- **Round Robin:** Her işlem en fazla bir süre dilimi (varsayılan 2) çalışır, bitmediyse kuyruğun sonuna geçer.
- **Multilevel Queue:** İki kuyruk vardır (acil: öncelik 1, normal: diğerleri). İşlemci boşaldığında önce acil kuyruğa bakılır. Her kuyruk kendi içinde FCFS çalışır ve çalışan işlem bölünmez.

## Performans ölçütleri

- Dönüş süresi = bitiş zamanı − varış zamanı
- Bekleme süresi = dönüş süresi − çalışma süresi
- Cevap süresi = ilk çalıştığı an − varış zamanı
- CPU kullanımı = çalışılan süre ÷ (son bitiş − ilk varış) × 100

## Bilinen sınırlamalar

- Çalışan işlem yarıda kesilmez (Multilevel Queue'da acil iş gelince bile).
- Girdi dosyasında ayrıntılı hata kontrolü yoktur; bozuk satırda program hata verip durur.
- Arayüzde tek işlemi silme yoktur, yalnızca listeyi temizleme vardır.

## Grup

- Dilan Demirel: depo, ortak yapı, FCFS, SJF, performans ölçütleri, birleştirme
- Berkay Onur Yılmaz: Round Robin
- Kağan: Multilevel Queue
- Elif Vuruşkan: Gantt şeması ve arayüz
