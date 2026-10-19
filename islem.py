class Islem:
    def __init__(self, ad, varis, sure, oncelik=0):
        self.ad = ad            # örn. "P1"
        self.varis = varis      # işlem kaçıncı saniyede geldi
        self.sure = sure        # işlem kaç saniye CPU istiyor
        self.oncelik = oncelik  # öncelik numarası