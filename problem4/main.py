# tulis solusi code disini

class transaksi():
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def penghitungan_volume(self):
        return self.panjang * self.lebar * self.tinggi
    
    def hitung_harga(self):
        penghitungan_volume = self.penghitungan_volume()

        if penghitungan_volume < 50:
            penghitungan_volume = 50

        berat_barang = (self.berat + 999) // 1000

        harga = berat_barang * 5000

        return harga
    
panjang = 5
lebar = 2
tinggi = 4
berat = 1000

barang = transaksi(panjang, lebar, tinggi, berat)
harga = barang.hitung_harga()

print(f"Harga Pengiriman: Rp {harga}")