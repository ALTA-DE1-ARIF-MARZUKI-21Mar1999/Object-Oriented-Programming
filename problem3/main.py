# tulis solusi code disini

class penjumlahan():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def menghitung_penjumlahan(self):
        return self.a +self.b
    
class pengurangan():
    def __init__(self, c, d):
        self.c = c
        self.d = d

    def menghitung_pengurangan(self):
        return self.c - self.d
    
class perkalian():
    def __init__(self, e, f):
        self.e = e
        self.f = f

    def menghitung_perkalian(self):
        return self.e * self.f
    
class pembagian():
    def __init__(self, g, h):
        self.g = g
        self.h = h

    def menghitung_pembagian(self):
        return self.g / self.h
    

penjumlahan = penjumlahan(3, 4)
penjumlahan_ = penjumlahan.menghitung_penjumlahan()

pengurangan = pengurangan(15, 4)
pengurangan_ = pengurangan.menghitung_pengurangan()

perkalian = perkalian(10, 10)
perkalian_ = perkalian.menghitung_perkalian()

pembagian = pembagian(12, 3)
pembagian_ = pembagian.menghitung_pembagian()

print("Kalkulator")
print(f"penjumlahan : {penjumlahan_}")
print(f"pengurangan : {pengurangan_}")
print(f"perkalian : {perkalian_}")
print(f"pembagian : {pembagian_}")
    
