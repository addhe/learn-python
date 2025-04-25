"""
    `Variable` adalah sebuah lokasi penyimpanan dalam memori komputer yang digunakan untuk
    menyimpan data atau nilai tertentu. Nilai di dalam variabel ini dapat 
    berubah-ubah selama program berjalan. Variabel biasanya memiliki nama unik
    yang digunakan untuk mengakses dan memanipulasi nilai tersebut.
"""

"""
    `Keywords` dalam pemrograman (juga sering disebut `reserved words`)
    adalah kata-kata khusus (special words) yang telah ditentukan oleh bahasa
    pemrograman itu sendiri dan memiliki arti atau fungsi tertentu.
    Kata-kata ini tidak diperbolehkan dipakai engineers/developers/programmer
    sebagai nama variabel, fungsi, atau elemen lain yang didefinisikan oleh
    pengguna, karena sudah digunakan untuk tujuan khusus tertentu dalam bahasa tersebut.
"""

# Variables in Python
a = 10
b = 20
c = a + b
print("Nilai a:", a)
print("Nilai b:", b)
print("Nilai c:", c)

# Variables naming rules
# 1. Nama variabel harus dimulai dengan huruf (a-z, A-Z) atau garis bawah (_).
# 2. Nama variabel dapat diikuti oleh huruf, angka (0-9), atau garis bawah (_).
# 3. Nama variabel bersifat case-sensitive (misalnya, "myVar" dan "myvar" adalah dua variabel yang berbeda).
# 4. Nama variabel tidak boleh menggunakan kata kunci (keywords) yang sudah ada dalam bahasa pemrograman Python.
# 5. Nama variabel tidak boleh mengandung spasi atau karakter khusus lainnya (kecuali garis bawah).
# 6. Nama variabel sebaiknya deskriptif dan mencerminkan isi atau tujuan dari variabel tersebut.

# Contoh penamaan variable yang benar di python
my_variable = 10
myVariable = 20
myVariable1 = 30
my_variable_2 = 40
myVariable_3 = 50
my_variable_4 = 60
myVariable_5 = 70

# Contoh penamaan variable yang salah di python
# 1. 1st_variable = 10 # tidak boleh diawali dengan angka
# 2. my-variable = 20 # tidak boleh menggunakan tanda minus (-)
# 3. my variable = 30 # tidak boleh ada spasi
# 4. my@variable = 40 # tidak boleh menggunakan karakter khusus (@)
# 5. my-variable-1 = 50 # tidak boleh menggunakan tanda minus (-)
# 6. my variable 1 = 60 # tidak boleh ada spasi

"""
    Operators in Python adalah simbol-simbol yang digunakan untuk melakukan operasi
    matematika, logika, atau manipulasi data pada variabel atau nilai tertentu.
"""

# Arithmetic Operators
a = 10
b = 5
print("Penjumlahan:", a + b)  # Penjumlahan
print("Pengurangan:", a - b)  # Pengurangan
print("Perkalian:", a * b)  # Perkalian
print("Pembagian:", a / b)  # Pembagian
print("Pangkat:", a ** b)  # Pangkat
print("Modulus:", a % b)  # Modulus
print("Pembagian Bulat:", a // b)  # Pembagian bulat

# Comparison Operators
a = 10
b = 5
print("Sama dengan:", a == b)  # Sama dengan
print("Tidak sama dengan:", a != b)  # Tidak sama dengan
print("Lebih besar:", a > b)  # Lebih besar
print("Lebih kecil:", a < b)  # Lebih kecil
print("Lebih besar atau sama dengan:", a >= b)  # Lebih besar atau sama dengan
print("Lebih kecil atau sama dengan:", a <= b)  # Lebih kecil atau sama dengan

# Logical Operators
a = True
b = False
print("AND:", a and b)  # AND
print("OR:", a or b)  # OR
print("NOT:", not a)  # NOT

# Bitwise Operators
a = 10  # 1010
b = 4   # 0100
print("AND:", a & b)  # AND
print("OR:", a | b)  # OR
print("XOR:", a ^ b)  # XOR
print("NOT:", ~a)  # NOT
print("Left Shift:", a << 1)  # Left Shift
print("Right Shift:", a >> 1)  # Right Shift

# Assignment Operators
a = 10
b = 5
a += b  # a = a + b
a -= b  # a = a - b
a *= b  # a = a * b
a /= b  # a = a / b
a **= b  # a = a ** b
a %= b  # a = a % b
a //= b  # a = a // b

# Identity Operators
a = [1, 2, 3]
b = a
c = a.copy()
print("a is b:", a is b)  # True
print("a is not b:", a is not b)  # False
print("a is c:", a is c)  # False
print("a is not c:", a is not c)  # True
print("a == c:", a == c)  # True
print("a is c:", a is c)  # False
print("a is not c:", a is not c)  # True
print("a == b:", a == b)  # True
print("a is b:", a is b)  # True

# Membership Operators
a = [1, 2, 3]
b = 2
print("2 in a:", b in a)  # True
print("4 in a:", 4 in a)  # False
print("2 not in a:", b not in a)  # False
print("4 not in a:", 4 not in a)  # True
print("2 in a:", b in a)  # True
print("4 in a:", 4 in a)  # False

# Ternary Operator
a = 10
b = 20
max_value = a if a > b else b
print("Nilai maksimum:", max_value)  # Nilai maksimum: 20

# References Docs:
# https://docs.python.org/3/tutorial/index.html
# https://www.python.org/shell/

