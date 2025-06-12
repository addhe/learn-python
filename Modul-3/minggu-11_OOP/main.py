# Modul 3 Minggu 11: Object-Oriented Programming (OOP)
# Piko si Koding Kancil dan Cetakan Ajaib (OOP)

print("===== Piko si Koding Kancil dan Cetakan Ajaib (OOP) =====")

# Cerita: Piko menemukan Cetakan Ajaib untuk membuat mainan hewan.
# Cetakan ini adalah 'class' di Python. Class adalah blueprint atau cetakan untuk membuat objek.

print("\n----- Cerita 1: Piko Membuat Cetakan Ajaib Pertamanya -----")
class CetakanAjaibHewan:
    # Ini adalah 'constructor', seperti resep awal saat membuat mainan dari cetakan.
    # Ia dijalankan setiap kali kita membuat mainan baru (objek baru).
    def __init__(self, nama_mainan, jenis_hewan, suara_hewan):
        print(f"Cetakan Ajaib: Membuat mainan {jenis_hewan} baru bernama {nama_mainan}...")
        # 'self' merujuk ke mainan spesifik yang sedang dibuat.
        # Ini adalah 'attributes' atau ciri-ciri dari setiap mainan yang dibuat.
        self.nama = nama_mainan
        self.jenis = jenis_hewan
        self.suara = suara_hewan
        self.energi = 10 # Semua hewan mainan Piko punya energi awal

    # Ini adalah 'method', yaitu kemampuan atau aksi yang bisa dilakukan mainan.
    def bersuara(self):
        if self.energi > 0:
            print(f"{self.nama} ({self.jenis}): '{self.suara}! {self.suara}!'")
            self.energi -= 1 # Bersuara butuh energi
        else:
            print(f"{self.nama} ({self.jenis}): 'Zzz... (kehabisan energi)'")

    def perkenalanDiri(self):
        print(f"Halo! Aku {self.nama}, seekor {self.jenis}. Aku suka bilang '{self.suara}!'")

    def makan(self, makanan):
        print(f"{self.nama} sedang makan {makanan}...")
        self.energi += 2 # Makan menambah energi
        print(f"Energi {self.nama} sekarang: {self.energi}")

# Piko sekarang punya cetakan! Tapi belum ada mainan yang dibuat.

print("\n----- Cerita 2: Piko Membuat Mainan dari Cetakan Ajaib -----")
# Sekarang Piko menggunakan CetakanAjaibHewan untuk membuat mainan (objek).
# Ini disebut 'instantiation' (membuat instance atau contoh dari class).

# Mainan pertama: Kancil Piko
kancil_piko = CetakanAjaibHewan("Piko Kancil", "Kancil Cerdik", "Cil! Cil!")
# Mainan kedua: Kelinci Lala
kelinci_lala = CetakanAjaibHewan("Lala Kelinci", "Kelinci Lincah", "Ncit! Ncit!")

# Sekarang Piko punya dua mainan. Setiap mainan punya nama, jenis, dan suara sendiri.
print(f"Mainan Piko pertama adalah {kancil_piko.nama} jenis {kancil_piko.jenis}.")
print(f"Mainan Lala pertama adalah {kelinci_lala.nama} jenis {kelinci_lala.jenis}.")

print("\n----- Cerita 3: Mainan Piko Beraksi! (Menggunakan Method) -----")
kancil_piko.perkenalanDiri()
kelinci_lala.perkenalanDiri()

print("\nMinta mainan bersuara:")
kancil_piko.bersuara()  # Piko Kancil: Cil! Cil!
kelinci_lala.bersuara() # Lala Kelinci: Ncit! Ncit!
kancil_piko.bersuara()
print(f"Energi Kancil Piko setelah bersuara dua kali: {kancil_piko.energi}")

print("\nMinta mainan makan:")
kelinci_lala.makan("wortel")
kancil_piko.makan("rumput")

print("\n----- Uh-Oh! Momen Kesalahan dengan Cetakan Ajaib -----")
# 1. Lupa memberikan argumen saat membuat objek (mainan)
# print("Mencoba membuat mainan tanpa informasi lengkap:")
# try:
#     mainan_error = CetakanAjaibHewan("Polos") # Akan error karena kurang argumen jenis_hewan dan suara_hewan
# except TypeError as e:
#     print(f"Piko berkata: Uh-oh! Cetakannya butuh info lengkap! Errornya: {e}")

# 2. Mencoba mengakses ciri-ciri (attribute) yang tidak ada
# print("\nMencoba tanya warna Kancil Piko (padahal belum dicatat di cetakan):")
# try:
#     print(kancil_piko.warna) # Akan error karena 'warna' tidak ada di CetakanAjaibHewan
# except AttributeError as e:
#     print(f"Piko berkata: Oops! Aku lupa catat warna di cetakan! Errornya: {e}")

# 3. Lupa 'self' saat mendefinisikan method di dalam class
# Jika di method bersuara() kita tulis 'def bersuara():' (tanpa self)
# dan di dalamnya kita coba akses 'nama' atau 'suara', akan error.
# Python akan bingung, 'nama' atau 'suara' milik siapa?
# 'self' itu seperti bilang "milik mainan ini".
# (Ini tidak bisa didemokan langsung di sini tanpa mengubah class, tapi ini poin penting)
print("Piko mengerti: 'self' itu penting agar setiap mainan tahu ciri-cirinya sendiri!")


print("\n----- Mengintegrasikan Contoh OOP yang Sudah Ada (Animal, Dog, Cat) -----")
# Ini adalah contoh class Animal yang sudah ada sebelumnya.
# Kita bisa anggap ini sebagai 'Cetakan Dasar Hewan'.
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
        self.energy = 5 # Energi default untuk Animal

    def make_sound(self):
        if self.energy > 0:
            print(f"{self.name} the {self.species} says {self.sound}")
            self.energy -=1
        else:
            print(f"{self.name} is too tired to make a sound.")
    
    def feed(self):
        print(f"{self.name} is being fed.")
        self.energy += 2
        print(f"Energy of {self.name} is now {self.energy}")

# 'Dog' dan 'Cat' adalah 'Cetakan Khusus' yang mewarisi sifat dari 'Cetakan Dasar Hewan'.
# Ini disebut 'Inheritance' atau pewarisan.
class Dog(Animal): # Dog adalah 'anak' dari Animal
    def __init__(self, name, breed, sound="Woof"): # Default sound untuk Dog
        # 'super()' memanggil constructor dari 'parent class' (Animal)
        super().__init__(name, "Dog", sound) # Spesiesnya pasti "Dog"
        self.breed = breed # Dog punya ciri khusus: breed

    # Dog bisa punya method khusus yang tidak dimiliki Animal lain
    def fetch(self, item):
        if self.energy > 1:
            print(f"{self.name} the {self.breed} fetches the {item}.")
            self.energy -=2 # Fetch butuh lebih banyak energi
        else:
            print(f"{self.name} is too tired to fetch.")

    # Dog juga bisa 'override' (mengganti) method dari parent class
    def make_sound(self):
        if self.energy > 0:
            # Anjing mungkin punya cara bersuara yang lebih spesifik
            print(f"{self.name} the {self.breed} barks loudly: {self.sound.upper()}! {self.sound.upper()}!")
            self.energy -=1
        else:
            print(f"{self.name} is too tired to bark.")


class Cat(Animal): # Cat juga 'anak' dari Animal
    def __init__(self, name, color, sound="Meow"):
        super().__init__(name, "Cat", sound) # Spesiesnya pasti "Cat"
        self.color = color # Cat punya ciri khusus: color

    def purr(self):
        if self.energy > 0:
            print(f"{self.name} the {self.color} cat is purring...")
            self.energy -=1
        else:
            print(f"{self.name} is too tired to purr.")
    
    # Cat juga bisa override make_sound
    def make_sound(self):
        if self.energy > 0:
            print(f"{self.name} the {self.color} cat meows softly: {self.sound}...")
            self.energy -=1
        else:
            print(f"{self.name} is too tired to meow.")

print("\nMembuat objek dari class Animal, Dog, dan Cat:")
# Membuat objek Animal biasa
generic_animal = Animal("Generic Animal", "Unknown Species", "Generic Sound")
generic_animal.make_sound()
generic_animal.feed()

# Membuat objek Dog
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.make_sound() # Akan menggunakan method make_sound() yang di-override di Dog
my_dog.fetch("ball")
my_dog.feed()

# Membuat objek Cat
my_cat = Cat("Whiskers", "Gray", "Meeoooww")
my_cat.make_sound() # Akan menggunakan method make_sound() yang di-override di Cat
my_cat.purr()
my_cat.feed()

print("\nCek energi setelah beraktivitas:")
print(f"Energi {my_dog.name}: {my_dog.energy}")
print(f"Energi {my_cat.name}: {my_cat.energy}")

print("\n----- Piko Belajar Lebih Lanjut: Inheritance (Pewarisan) -----")
# Piko melihat bahwa Dog dan Cat adalah jenis khusus dari Animal.
# Mereka punya semua sifat Animal (nama, spesies, suara, bisa bersuara, bisa makan)
# TAPI mereka juga punya sifat atau kemampuan tambahan (breed untuk Dog, color untuk Cat, fetch untuk Dog, purr untuk Cat).
# Ini seperti Piko membuat 'Cetakan Super Ajaib' (Dog/Cat) dari 'Cetakan Dasar' (Animal).

print("Piko sekarang mengerti tentang class, object, attribute, method, dan inheritance!")
print("Petualangan OOP Piko sangat menyenangkan!")

# Uh-Oh! Momen dengan Inheritance:
# 1. Memanggil method khusus dari parent class:
#    Objek 'generic_animal' (dari class Animal) tidak bisa melakukan 'fetch' atau 'purr'.
# try:
#     print("Mencoba generic_animal melakukan fetch:")
#     generic_animal.fetch("stick") # Akan error
# except AttributeError as e:
#     print(f"Piko berkata: Oh iya! Hanya anjing yang punya cetakan untuk fetch! Error: {e}")

# 2. Lupa memanggil super().__init__() di child class:
#    Jika di class Dog, Piko lupa menulis 'super().__init__(name, "Dog", sound)',
#    maka 'Dog' tidak akan punya 'name', 'species', atau 'sound' dari 'Animal'.
#    Mainan anjingnya jadi tidak lengkap!
# print("Piko mencatat: Jangan lupa panggil 'super()' agar warisan sifatnya lengkap!")

# Contoh lain dari penggunaan class yang sudah ada
# ... (kode Animal, Dog, Cat yang sudah ada sebelumnya bisa tetap di sini atau diintegrasikan seperti di atas)
# class Animal:
# ... (existing Animal class code) ...

# class Dog(Animal):
# ... (existing Dog class code) ...

# class Cat(Animal):
# ... (existing Cat class code) ...

# dog1 = Dog("Buddy", "Golden Retriever")
# cat1 = Cat("Whiskers", "Siamese")
# animal1 = Animal("Generic", "Creature", "Some sound")

# print(f"{dog1.name} is a {dog1.species} of breed {dog1.breed} and says {dog1.sound}")
# dog1.make_sound()
# dog1.fetch("ball")

# print(f"{cat1.name} is a {cat1.species} of color {cat1.color} and says {cat1.sound}")
# cat1.make_sound()
# cat1.purr()

# print(f"{animal1.name} is a {animal1.species} and says {animal1.sound}")
# animal1.make_sound()
# animal1.feed()
# dog1.feed()