# main.py untuk Modul-1/minggu-2_Function/
# Petualangan di Kerajaan Kode: Mantra Pemanggil Ajaib (Fungsi)!

# --- Piko si Koding Kancil Memperkenalkan Fungsi ---

# 1. Menulis Resep Ajaib (Mendefinisikan Fungsi)
# =============================================
print("--- Bagian 1: Menulis Resep Ajaib (Mendefinisikan Fungsi) ---")

# Resep sederhana untuk menyapa teman
def sapa_teman_ajaib(nama_teman):
    """
    Ini adalah resep ajaib (fungsi) untuk menyapa teman.
    Dia butuh satu bahan (parameter) yaitu 'nama_teman'.
    """
    pesan_salam = "Hore, " + nama_teman + "! Selamat berpetualang di Kerajaan Kode hari ini!"
    print(pesan_salam)

print("Resep 'sapa_teman_ajaib' sudah Piko tulis di buku mantra!\n")

# Resep yang memberikan hasil (fungsi dengan 'return')
def gandakan_angka_ajaib(angka):
    """
    Resep ini menerima satu angka ajaib,
    lalu mengembalikan angka tersebut setelah digandakan.
    """
    hasil_ganda = angka * 2
    return hasil_ganda # Kata sihir 'return' untuk memberikan hasil

print("Resep 'gandakan_angka_ajaib' juga sudah siap!\n")

# Resep yang butuh lebih dari satu bahan
def buat_minuman_campur(buah1, buah2):
    """Resep untuk membuat minuman dari campuran dua buah."""
    print(f"Piko sedang membuatkanmu minuman dari {buah1} dan {buah2}...")
    minuman_jadi = "Jus Spesial " + buah1 + " dan " + buah2
    return minuman_jadi

print("Resep 'buat_minuman_campur' telah ditambahkan!\n")


# 2. Menggunakan Resep Ajaib (Memanggil Fungsi)
# ==========================================
print("--- Bagian 2: Menggunakan Resep Ajaib (Memanggil Fungsi) ---")

print("Saatnya mencoba resep 'sapa_teman_ajaib':")
sapa_teman_ajaib("Jagoan Cilik Pemberani") # Memanggil resep dengan bahan "Jagoan Cilik Pemberani"
sapa_teman_ajaib("Piko si Kancil Cerdik")  # Memanggil resep untuk Piko
print("-" * 20)

print("\nSaatnya mencoba resep 'gandakan_angka_ajaib':")
angka_rahasia = 7
hasil_resep_ganda = gandakan_angka_ajaib(angka_rahasia)
print(f"Angka rahasiaku adalah {angka_rahasia}")
print(f"Setelah digandakan oleh resep ajaib, jadi: {hasil_resep_ganda}")

angka_lain = 25
print(f"Angka {angka_lain} digandakan menjadi: {gandakan_angka_ajaib(angka_lain)}")
print("-" * 20)

print("\nMencoba resep 'buat_minuman_campur':")
minuman_pesananku = buat_minuman_campur("Mangga Harum", "Jeruk Segar")
print(f"Minumanmu sudah jadi: {minuman_pesananku}")
minuman_piko = buat_minuman_campur("Stroberi Merah", "Apel Hijau")
print(f"Piko juga buat untuk Piko sendiri: {minuman_piko}")
print("-" * 20)


# 3. "Uh-Oh!" si Pesan Kesalahan Saat Memakai Mantra Pemanggil
# ========================================================
# Piko: "Ingat, Jagoan Cilik, jangan takut kalau bertemu 'Uh-Oh!' ya! Itu teman belajar kita!"
print("\n--- Bagian 3: Contoh 'Uh-Oh!' (Error) dari Piko ---")

# a. Salah Panggil Nama Mantra (NameError)
# Piko: "Kalau kita panggil nama resep yang tidak ada atau salah ketik..."
# print("\nMencoba memanggil mantra yang salah tulis 'sapa_teman_ajaiib':")
# sapa_teman_ajaiib("Teman Misterius")
# Pesan Uh-Oh yang akan muncul: NameError: name 'sapa_teman_ajaiib' is not defined

# b. Bahan Kurang atau Lebih (TypeError)
# Piko: "Kalau resepnya butuh bahan tertentu, tapi kita kasihnya kurang atau lebih..."
def butuh_satu_bahan_saja(bahan):
    print("Bahan yang Piko terima:", bahan)

# print("\nMencoba 'butuh_satu_bahan_saja' tanpa bahan:")
# butuh_satu_bahan_saja()
# Pesan Uh-Oh: TypeError: butuh_satu_bahan_saja() missing 1 required positional argument: 'bahan'

# print("\nMencoba 'butuh_satu_bahan_saja' dengan dua bahan:")
# butuh_satu_bahan_saja("apel", "pisang")
# Pesan Uh-Oh: TypeError: butuh_satu_bahan_saja() takes 1 positional argument but 2 were given

# c. Lupa Tanda Kurung () Saat Memanggil
# Piko: "Kalau kita panggil nama resep tanpa tanda kurung ajaib `()`..."
# print("\nLupa tanda kurung saat memanggil 'sapa_teman_ajaib':")
# print(sapa_teman_ajaib)
# Piko: "Ini tidak menjalankan resepnya, tapi cuma menunjukkan resep itu sendiri. Untuk menjalankannya, tambahkan () ya! -> sapa_teman_ajaib('Nama')"

# d. Salah Menulis Resep (IndentationError)
# Piko: "Saat menulis resep (mendefinisikan fungsi), langkah-langkahnya harus menjorok ke dalam dengan benar!"
# Contoh IndentationError (ini akan error jika tidak dikomentari saat Python membaca filenya):
# def resep_salah_tulis(nama):
# print("Halo", nama) # Uh-Oh! IndentationError: expected an indented block after function definition on line X
# Piko: "Langkah-langkah resepnya harus ditulis sedikit ke kanan (menjorok) setelah baris 'def' ya!"

print("\nPetualangan hari ini tentang Fungsi si Mantra Pemanggil Ajaib selesai!")
print("Kamu makin hebat, Jagoan Cilik!")

# Contoh fungsi dari file awal (jika ada dan ingin dipertahankan)
# def greet(name):
#     return f"Hello, {name}!"

# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# if __name__ == "__main__":
#     print("\n--- Contoh Fungsi Tambahan (dari file awal) ---")
#     print(greet("Dunia Lain"))
#     print("Penjumlahan 5 dan 3 (fungsi add):", add(5, 3))
#     print("Perkalian 4 dan 2 (fungsi multiply):", multiply(4, 2))