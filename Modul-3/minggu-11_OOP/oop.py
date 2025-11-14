# Contoh kelas
class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("Meow!")

# Membuat objek dari kelas
kucing1 = Kucing("Tom", 3)
print(kucing1.nama)
print(kucing1.umur)
kucing1.bersuara()
