# This file contains examples of looping in Python.

# --- Piko si Koding Kancil dan Mesin Pengulang Ajaib ---
print("--- Piko dan Mesin Pengulang Ajaib (`for` loop) ---")

# 1. Piko Menyapa Teman-Temannya (Looping melalui list)
# ====================================================
print("\n--- 1. Piko Menyapa Teman-Temannya ---")
daftar_teman_piko = ["Kura-kura Cepat", "Kelinci Bijak", "Monyet Ceria", "Beruang Baik Hati"]

print("Daftar teman Piko:", daftar_teman_piko)
print("Piko akan menyapa mereka satu per satu:")
for teman_saat_ini in daftar_teman_piko:
    # 'teman_saat_ini' akan berisi satu nama teman dari daftar_teman_piko setiap kali pengulangan
    print(f"Halo, {teman_saat_ini}! Selamat datang di petualangan kode!")

print("Semua teman sudah Piko sapa!\n")

# 2. Piko Menghitung Harta Karun dengan `range()`
# =============================================
print("--- 2. Piko Menghitung Harta Karun dengan `range()` ---")

# Menggunakan range(jumlah) -> menghasilkan angka dari 0 sampai jumlah-1
print("Piko menghitung 5 permata pertamanya (0 sampai 4):")
for nomor_permata in range(5):
    print(f"Permata ke-{nomor_permata}")

# Menggunakan range(mulai, sampai) -> menghasilkan angka dari 'mulai' sampai 'sampai-1'
print("\nPiko menghitung koin emas dari 1 sampai 3:")
for nomor_koin in range(1, 4):
    print(f"Koin emas ke-{nomor_koin}")

# Menggunakan range(mulai, sampai, langkah)
print("\nPiko menghitung lompatan ajaib (angka genap dari 2 sampai 10):")
for lompatan in range(2, 11, 2):
    print(f"Piko melompat ke angka {lompatan}!")

print("Perhitungan harta karun selesai!\n")

# 3. Piko Mengeja Kata Ajaib (Looping melalui string)
# ==================================================
print("--- 3. Piko Mengeja Kata Ajaib ---")
kata_ajaib = "PYTHON"
print(f"Kata ajaib Piko adalah: {kata_ajaib}")
print("Piko akan mengejanya:")
for huruf in kata_ajaib:
    print(f"Huruf: {huruf}")

print("Kata ajaib sudah dieja!\n")

# 4. (Pengantar Singkat) Mesin Pengulang Bersyarat (`while` loop)
# ===========================================================
print("--- 4. Pengantar Singkat Mesin `while` (lebih detail minggu depan!) ---")
# Piko: "Ada juga mesin `while` yang mengulang selama kondisinya benar."
# Contoh sederhana:
jumlah_kue_piko = 3
print(f"Piko punya {jumlah_kue_piko} kue.")
while jumlah_kue_piko > 0:
    print(f"Piko makan 1 kue. Nyam! Sisa kue: {jumlah_kue_piko - 1}")
    jumlah_kue_piko = jumlah_kue_piko - 1 # Penting! Mengubah kondisi agar loop bisa berhenti

print("Kue Piko sudah habis! (Ini contoh `while` loop sederhana)\n")

# 5. "Uh-Oh!" dari Piko (Contoh Error Umum pada `for` Loop)
# ========================================================
print("--- 5. 'Uh-Oh!' dari Piko (Contoh Error Umum pada `for` Loop) ---")
# Piko: "Ingat, 'Uh-Oh!' itu teman belajar kita! Jangan takut untuk mencoba dan salah!"

# a. Lupa titik dua (SyntaxError)
# Piko: "Kalau lupa tanda ':' setelah baris `for`..."
# daftar_angka = [1, 2, 3]
# for angka in daftar_angka # Uh-Oh! SyntaxError: expected ':'
#     print(angka)

# b. Salah menjorok (IndentationError)
# Piko: "Kalau baris di dalam `for` tidak menjorok ke dalam..."
# for angka in range(3):
# print(angka) # Uh-Oh! IndentationError: expected an indented block

# c. Menggunakan variabel yang salah di dalam loop (NameError)
# Piko: "Kalau salah ketik nama variabel di dalam loop..."
# buah_buahan = ["apel", "pisang", "mangga"]
# for buah_enak_pisan in buah_buahan:
#     print(buah_enak) # Uh-Oh! NameError: name 'buah_enak' is not defined. Mungkin maksudnya 'buah_enak_pisan'?

print("\nPetualangan hari ini tentang Mesin Pengulang Ajaib (`for` loop) selesai!")
print("Kamu semakin mahir di Kerajaan Kode, Jagoan Cilik!")