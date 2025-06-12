# main.py untuk Modul-1/minggu-3_Conditionals/
# Petualangan di Kerajaan Kode: Gerbang Ajaib Penentu Jalan (Kondisional)!

# --- Piko si Koding Kancil dan Gerbang Ajaib ---
print("--- Piko dan Gerbang Ajaib Penentu Jalan ---")

# 1. Gerbang Emas dengan Kunci (if)
# =================================
print("\n--- 1. Gerbang Emas dengan Kunci (if) ---")
kunci_emas_dimiliki = True # Coba ganti jadi False!
print(f"Piko punya Kunci Emas? {kunci_emas_dimiliki}")

if kunci_emas_dimiliki: # Kondisi: apakah kunci_emas_dimiliki itu Benar (True)?
    print("Gerbang Emas terbuka! Hore, Piko boleh masuk ke Taman Permata!")
    print("Di dalam taman, Piko menemukan banyak permata berkilauan!")

print("Petualangan di Gerbang Emas selesai (atau tidak jika tidak punya kunci).")

# 2. Gerbang Emas atau Gerbang Kayu (if-else)
# ==========================================
print("\n--- 2. Gerbang Emas atau Gerbang Kayu (if-else) ---")
kunci_perak_dimiliki = False # Coba ganti jadi True!
print(f"Piko punya Kunci Perak? {kunci_perak_dimiliki}")

if kunci_perak_dimiliki:
    print("Gerbang Perak terbuka! Piko masuk ke Air Terjun Pelangi!")
else:
    print("Gerbang Perak terkunci! Oh tidak!")
    print("Tapi jangan sedih, Piko bisa lewat Gerbang Kayu menuju Hutan Bisikan.")

print("Petualangan di Gerbang Perak atau Kayu selesai.")

# 3. Banyak Pilihan Gerbang (if-elif-else)
# ========================================
print("\n--- 3. Banyak Pilihan Gerbang (if-elif-else) ---")
jenis_kunci_piko = "perunggu" # Coba ganti jadi "emas", "perak", atau "besi"

print(f"Piko membawa kunci jenis: {jenis_kunci_piko}")

if jenis_kunci_piko == "emas":
    print("Dengan Kunci Emas, Piko membuka Gerbang Istana Awan!")
elif jenis_kunci_piko == "perak":
    print("Dengan Kunci Perak, Piko membuka Gerbang Sungai Kristal!")
elif jenis_kunci_piko == "perunggu":
    print("Dengan Kunci Perunggu, Piko membuka Gerbang Gua Rahasia!")
else:
    print(f"Hmm, Kunci {jenis_kunci_piko} sepertinya tidak cocok untuk gerbang mana pun di sini. Piko coba cari jalan lain.")

print("Petualangan memilih gerbang selesai.")

# 4. Kunci Ajaib (Kondisi dan Perbandingan)
# ========================================
print("\n--- 4. Kunci Ajaib (Kondisi dan Perbandingan) ---")
jumlah_apel_piko = 7
jumlah_apel_teman = 10

print(f"Piko punya {jumlah_apel_piko} apel, teman Piko punya {jumlah_apel_teman} apel.")

if jumlah_apel_piko > 5:
    print("Piko punya lebih dari 5 apel! Cukup untuk bekal petualangan!")

if jumlah_apel_piko == jumlah_apel_teman:
    print("Jumlah apel Piko sama banyak dengan teman Piko.")
else:
    print("Jumlah apel Piko tidak sama dengan teman Piko.")

if jumlah_apel_piko < jumlah_apel_teman:
    print("Piko punya apel lebih sedikit dari temannya.")

# 5. "Uh-Oh!" dari Piko (Contoh Error Umum)
# ========================================
print("\n--- 5. 'Uh-Oh!' dari Piko (Contoh Error Umum) ---")
# Piko: "Ingat, 'Uh-Oh!' itu teman belajar kita!"

# a. Lupa titik dua (SyntaxError)
# Piko: "Kalau lupa tanda ':' setelah if, elif, atau else..."
# if jumlah_apel_piko > 3 # Uh-Oh! SyntaxError: expected ':'
#     print("Ini tidak akan jalan")

# b. Salah menjorok (IndentationError)
# Piko: "Kalau baris di dalam if tidak menjorok ke dalam..."
# if jumlah_apel_piko > 3:
# print("Ini juga tidak akan jalan") # Uh-Oh! IndentationError: expected an indented block

# c. Salah pakai '=' untuk membandingkan (Logika Salah atau SyntaxError)
# Piko: "Ingat, untuk membandingkan kita pakai '==', bukan '=' sendirian di kondisi if!"
# nilai_ujian = 80
# if nilai_ujian = 80: # Uh-Oh! Ini mencoba memberi nilai, bukan membandingkan. Seharusnya nilai_ujian == 80
#     print("Nilai bagus!")
# Di Python 3.8+, ini akan jadi SyntaxError: invalid syntax (assignment expression).
# Di versi lama, mungkin tidak error tapi logikanya salah.

print("\n--- Menggunakan Fungsi dengan Kondisional (Contoh dari file awal) ---")
# Ini adalah fungsi yang sudah ada di file main.py sebelumnya
def check_number(num):
    """Fungsi ini memeriksa apakah sebuah angka positif, negatif, atau nol."""
    if num > 0:
        return "Positif"
    elif num < 0:
        return "Negatif"
    else:
        return "Nol"

# Contoh penggunaan fungsi check_number
if __name__ == "__main__": # Memastikan kode ini hanya berjalan jika file ini dijalankan langsung
    test_numbers = [10, -5, 0, 100, -23]
    print("Piko akan memeriksa beberapa angka menggunakan resep 'check_number':")
    for number in test_numbers:
        result = check_number(number)
        print(f"Angka {number} itu {result}, kata resep Piko!")

print("\nPetualangan hari ini tentang Gerbang Ajaib Penentu Jalan (Kondisional) selesai!")
print("Kamu semakin jago di Kerajaan Kode, Jagoan Cilik!")