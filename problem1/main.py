# tulis solusi code disini

class persegi():
    def __init__(self, sisi):
        self.sisi = sisi

    def menghitung_luas(self):
        return self.sisi * self.sisi
    
class segitiga():
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def menghitung_luas(self):
        return self.alas * self.tinggi / 2
    
class persegi_panjang():
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def menghitung_luas(self):
        return self.panjang * self.lebar
    
persegi = persegi(4)
persegi.menghitung_luas()

segitiga = segitiga(3, 4)
segitiga.menghitung_luas()

persegi_panjang = persegi_panjang(7, 8)
persegi_panjang.menghitung_luas()

print("Luas")
print(f"persegi : {persegi.menghitung_luas()}")
print(f"segitiga : {segitiga.menghitung_luas()}")
print(f"persegi_panjang : {persegi_panjang.menghitung_luas()}")

print('\n')


class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def menghitung_keliling(self):
        return 4 * self.sisi
    
class Segitiga:
    def __init__(self, sisiA, sisiB):
        self.sisiA = sisiA
        self.sisiB = sisiB

    def menghitung_keliling(self):
        sisiC = (self.sisiA ** 2 + self.sisiB ** 2) ** 0.5
        return self.sisiA + self.sisiB + sisiC
    
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def menghitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

persegi = Persegi(4)
keliling_persegi = persegi.menghitung_keliling()

segitiga = Segitiga(3, 4)
keliling_segitiga = segitiga.menghitung_keliling()

persegi_panjang = PersegiPanjang(7, 8)
keliling_persegi_panjang = persegi_panjang.menghitung_keliling()

print("Keliling")
print(f"persegi : {keliling_persegi}")
print(f"segitiga : {keliling_segitiga}")
print(f"persegi_panjang : {keliling_persegi_panjang}")

