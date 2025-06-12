# This file contains exercises and examples related to strings in Python.

print("Selamat datang di Petualangan Piko dengan Gulungan Pesan Ajaib (String)!")

# Cerita 1: Piko Menulis Pesan Pertamanya
print("\n--- Cerita 1: Piko Menulis Pesan Pertamanya ---")
nama_piko = "Piko"
salam = 'Halo Kawan!' # Boleh pakai kutip satu atau dua
print(f"Pesan pertama Piko: {nama_piko}")
print(f"Pesan kedua Piko: {salam}")

# Cerita 2: Piko Menggabungkan Pesan
print("\n--- Cerita 2: Piko Menggabungkan Pesan ---")
pesan1 = "Aku Suka "
pesan2 = "Apel Merah"
pesan_lengkap = pesan1 + pesan2 # Ini konkatenasi
print(f"Pesan gabungan Piko: {pesan_lengkap}")

nama_hewan = "Kancil"
# Menggunakan f-string untuk gabungan yang lebih rapi
nama_panggilan_fstring = f"Koding {nama_hewan}"
print(f"Nama panggilan Piko (dengan f-string): {nama_panggilan_fstring}")

# Contoh dari file sebelumnya (string concatenation)
greeting_from_file = "Hello, World!"
name_from_file = "Alice"
welcome_message_from_file = greeting_from_file + " My name is " + name_from_file + "."
print(f"Contoh gabungan dari file: {welcome_message_from_file}")

# Cerita 3: Piko Menghitung Panjang Pesan
print("\n--- Cerita 3: Piko Menghitung Panjang Pesan ---")
pesan_pendek = "Piko"
panjang_pesan_pendek = len(pesan_pendek)
print(f"Pesan '{pesan_pendek}' panjangnya: {panjang_pesan_pendek}")

pesan_panjang = "Halo Kawan!"
panjang_pesan_panjang = len(pesan_panjang)
print(f"Pesan '{pesan_panjang}' panjangnya: {panjang_pesan_panjang}")

# Cerita 4: Piko Membaca Huruf Satu per Satu (Indexing)
print("\n--- Cerita 4: Piko Membaca Huruf Satu per Satu (Indexing) ---")
nama = "Piko"
huruf_pertama = nama[0] # Indeks 0 untuk huruf pertama
huruf_ketiga = nama[2]  # Indeks 2 untuk huruf ketiga
print(f"Huruf pertama dari '{nama}' adalah: {huruf_pertama}")
print(f"Huruf ketiga dari '{nama}' adalah: {huruf_ketiga}")

# Uh-Oh! Momen Kesalahan (IndexError)
# print("\n--- Uh-Oh! Mencoba mengambil huruf di luar jangkauan ---")
# nama_tes = "ABC"
# print(nama_tes[3]) # Ini akan menyebabkan IndexError

# Cerita 5: Piko Mengambil Potongan Pesan (Slicing)
print("\n--- Cerita 5: Piko Mengambil Potongan Pesan (Slicing) ---")
julukan = "KodingKancil"
kata_pertama = julukan[0:6] # Dari indeks 0 sampai sebelum indeks 6
kata_kedua = julukan[6:]   # Dari indeks 6 sampai akhir
print(f"Dari '{julukan}', Piko mengambil: '{kata_pertama}'")
print(f"Dari '{julukan}', Piko juga mengambil: '{kata_kedua}'")

pesan_slice = "Belajar Python itu Seru"
print(f"Pesan asli untuk slice: '{pesan_slice}'")
print(f"Slice [8:14]: '{pesan_slice[8:14]}'") # Mengambil 'Python'
print(f"Slice [:7]: '{pesan_slice[:7]}'")     # Mengambil 'Belajar'
print(f"Slice [19:]: '{pesan_slice[19:]}'")   # Mengambil 'Seru'
print(f"Slice [::2]: '{pesan_slice[::2]}'")   # Mengambil setiap huruf kedua

# Cerita 6: Piko Bermain dengan Mantra String Ajaib (Metode String)
print("\n--- Cerita 6: Piko Bermain dengan Mantra String Ajaib (Metode String) ---")
pesan_awal_metode = "  Piko si Kancil Cerdik!  "
print(f"Pesan awal untuk metode: '{pesan_awal_metode}'")

# Mantra Huruf Besar
pesan_besar = pesan_awal_metode.upper()
print(f"Pesan jadi besar semua: '{pesan_besar}'")

# Mantra Huruf Kecil
pesan_kecil = pesan_awal_metode.lower()
print(f"Pesan jadi kecil semua: '{pesan_kecil}'")

# Mantra Rapikan Spasi (strip, lstrip, rstrip)
pesan_rapi_strip = pesan_awal_metode.strip()
print(f"Pesan dirapikan spasinya (strip): '{pesan_rapi_strip}'")
pesan_rapi_lstrip = pesan_awal_metode.lstrip()
print(f"Pesan dirapikan spasi kiri (lstrip): '{pesan_rapi_lstrip}'")
pesan_rapi_rstrip = pesan_awal_metode.rstrip()
print(f"Pesan dirapikan spasi kanan (rstrip): '{pesan_rapi_rstrip}'")

# Mantra Judul (title)
pesan_judul = pesan_rapi_strip.title()
print(f"Pesan jadi judul (title): '{pesan_judul}'")

# Mantra Kapitalisasi (capitalize)
pesan_kapital = pesan_rapi_strip.capitalize()
print(f"Pesan dikapitalisasi (capitalize): '{pesan_kapital}'")

# Mantra Cari Kata (find, index)
# find() mengembalikan -1 jika tidak ditemukan
# index() mengembalikan ValueError jika tidak ditemukan
posisi_kancil_find = pesan_rapi_strip.find("Kancil")
print(f"Kata 'Kancil' ditemukan (find) di posisi: {posisi_kancil_find}")
posisi_buaya_find = pesan_rapi_strip.find("Buaya")
print(f"Kata 'Buaya' ditemukan (find) di posisi: {posisi_buaya_find}")

# Mantra Ganti Kata (replace)
pesan_diganti = pesan_rapi_strip.replace("Cerdik", "Pintar")
print(f"Pesan setelah diganti ('Cerdik' jadi 'Pintar'): '{pesan_diganti}'")
pesan_diganti_semua_i = pesan_rapi_strip.replace("i", "o")
print(f"Pesan setelah semua 'i' diganti 'o': '{pesan_diganti_semua_i}'")

# Mantra Cek Awalan dan Akhiran (startswith, endswith)
print(f"Apakah pesan '{pesan_rapi_strip}' dimulai dengan 'Piko'? {pesan_rapi_strip.startswith('Piko')}")
print(f"Apakah pesan '{pesan_rapi_strip}' diakhiri dengan 'Cerdik!'? {pesan_rapi_strip.endswith('Cerdik!')}")

# Mantra Pecah String (split)
kalimat = "Piko belajar koding setiap hari"
kata_kata = kalimat.split(" ") # Memecah berdasarkan spasi
print(f"Kalimat '{kalimat}' dipecah menjadi: {kata_kata}")

# Mantra Gabung String dari List (join)
list_kata = ["Belajar", "Python", "itu", "menyenangkan"]
kalimat_dari_list = " ".join(list_kata) # Menggabungkan dengan spasi
print(f"List {list_kata} digabung menjadi: '{kalimat_dari_list}'")

# Mengintegrasikan contoh dari file yang sudah ada (string_examples)
print("\n--- Contoh dari file string_examples() yang sudah ada ---")

# Example of string creation (sudah ada di cerita Piko)
greeting_original = "Hello, World!"
print(f"Original greeting: {greeting_original}")

# Example of string formatting (f-string)
name_original = "Alice"
age_original = 30
formatted_message_original = f"{name_original} is {age_original} years old."
print(f"Original formatted message: {formatted_message_original}")

# Example of string methods (sudah ada di cerita Piko, ditambahkan yang belum)
sample_string_original = "   Python Programming   "
print(f"Original String: '{sample_string_original}'")
print(f"Stripped String: '{sample_string_original.strip()}'")
print(f"Uppercase: '{sample_string_original.upper()}'")
print(f"Lowercase: '{sample_string_original.lower()}'")
print(f"Title Case: '{sample_string_original.title()}'") # Sudah ada di cerita Piko

# Uh-Oh! Momen Kesalahan (TypeError)
# print("\n--- Uh-Oh! Mencoba menggabung string dengan angka ---")
# coba_error = "Piko punya " + 5 + " apel" # Ini akan menyebabkan TypeError
# print(coba_error)
# Solusi: ubah angka jadi string
# solusi_error = "Piko punya " + str(5) + " apel"
# print(solusi_error)

print("\nPetualangan Piko dengan Gulungan Pesan Ajaib selesai! Ia jadi ahli memainkan string!")

# Menjalankan fungsi string_examples jika ada dan belum tercakup semua
# (Dalam kasus ini, semua contoh dari string_examples() sudah diintegrasikan ke cerita Piko)
# def string_examples():
#     # ... (kode asli dari file)
#     pass

# if __name__ == "__main__":
    # string_examples() # Tidak perlu dipanggil lagi jika sudah terintegrasi
    # Cukup print akhir dari cerita Piko
    # print("Semua contoh string telah dijalankan melalui cerita Piko.")