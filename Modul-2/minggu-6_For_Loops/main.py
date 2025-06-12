# For Loops Lanjutan Example

print("Selamat datang di Petualangan Piko si Koding Kancil dengan For Loop Lanjutan!")

# Cerita 1: Piko Menjelajahi Isi Tas Ajaib dengan enumerate
print("\\n--- Cerita 1: Piko Menjelajahi Isi Tas Ajaib dengan enumerate ---")
isi_tas_ajaib = ["buku catatan", "pensil warna", "kompas ajaib", "roti lapis"]
print("Piko membuka tas ajaibnya dan melihat isinya satu per satu:")
for nomor, barang in enumerate(isi_tas_ajaib):
    print(f"Barang ke-{nomor + 1}: {barang}")
print("Piko sekarang tahu urutan semua barang di tasnya!")

# Uh-Oh! Momen Kesalahan (enumerate)
# Jika Piko lupa menggunakan enumerate dan mencoba mengakses nomor urut secara manual
# print("\\n--- Uh-Oh! Momen Kesalahan (enumerate) ---")
# nomor_manual = 1
# for barang in isi_tas_ajaib:
#     # Ini akan menyebabkan kesalahan jika kita ingin nomor urut yang benar tanpa enumerate
#     # print(f"Barang ke-{nomor_manual}: {barang}") # Tidak akan otomatis bertambah dengan benar
#     nomor_manual +=1
# print("Piko menyadari, 'Oh, lebih mudah pakai enumerate agar nomornya otomatis benar!'")


# Cerita 2: Piko dan Kupu-Kupu Berwarna-warni (Looping dengan range dan kondisi)
print("\\n--- Cerita 2: Piko dan Kupu-Kupu Berwarna-warni ---")
print("Piko melihat kupu-kupu terbang!")
jumlah_kupu_kupu = 7
for i in range(1, jumlah_kupu_kupu + 1):
    if i % 2 == 0:
        warna = "biru"
    else:
        warna = "kuning"
    print(f"Kupu-kupu ke-{i} berwarna {warna} hinggap di bunga.")
print("Piko senang melihat begitu banyak kupu-kupu!")

# Uh-Oh! Momen Kesalahan (range)
# Jika Piko salah menentukan batas range
# print("\\n--- Uh-Oh! Momen Kesalahan (range) ---")
# print("Piko ingin menghitung 5 apel, tapi salah menuliskan range:")
# for i in range(4): # Seharusnya range(1, 6) atau range(5) jika mulai dari 0
#     print(f"Apel ke-{i+1}")
# print("Piko menyadari, 'Oops, jumlah apelnya kurang satu! Aku harus perbaiki rangenya.'")


# Cerita 3: Piko Membuat Pola Bintang Ajaib (Nested Loop)
print("\\n--- Cerita 3: Piko Membuat Pola Bintang Ajaib ---")
print("Piko ingin membuat pola bintang ajaib di langit malam.")
baris_bintang = 4
for i in range(1, baris_bintang + 1):
    for j in range(i):
        print("* ", end="") # Mencetak bintang tanpa pindah baris
    print() # Pindah baris setelah satu baris bintang selesai
print("Pola bintang ajaib Piko sudah jadi!")

# Uh-Oh! Momen Kesalahan (Nested Loop)
# Jika Piko lupa print() untuk pindah baris di nested loop
# print("\\n--- Uh-Oh! Momen Kesalahan (Nested Loop) ---")
# print("Piko mencoba membuat pola, tapi semua bintang jadi satu baris!")
# for i in range(3):
#     for j in range(3):
#         print("* ", end="")
#     # Lupa print() di sini!
# print("\\nPiko berpikir, 'Hmm, aku perlu memberitahu komputer kapan harus pindah baris!'")

# Cerita 4: Piko dan Pesan Rahasia (Looping string)
print("\\n--- Cerita 4: Piko dan Pesan Rahasia ---")
pesan_rahasia = "KODINGSERU"
print(f"Piko menemukan pesan rahasia: {pesan_rahasia}")
print("Piko membaca pesan itu huruf per huruf:")
for huruf in pesan_rahasia:
    print(f"Huruf: {huruf}")
print("Piko berhasil membaca seluruh pesan rahasia!")

# Uh-Oh! Momen Kesalahan (Looping String)
# Tidak ada kesalahan umum yang spesifik untuk looping string dasar selain logika program,
# tapi bisa saja Piko mencoba mengubah string di dalam loop (string immutable)
# print("\\n--- Uh-Oh! Momen Kesalahan (Looping String) ---")
# pesan_awal = "ABC"
# print(f"Pesan awal: {pesan_awal}")
# # for huruf_idx in range(len(pesan_awal)):
# #     pesan_awal[huruf_idx] = 'X' # Ini akan menyebabkan TypeError karena string immutable
# print("Piko belajar bahwa string tidak bisa diubah langsung per hurufnya, harus dibuat string baru.")


# Cerita 5: Piko Menggunakan 'break' untuk Mencari Harta Karun
print("\\n--- Cerita 5: Piko Menggunakan 'break' untuk Mencari Harta Karun ---")
langkah_peta = ["maju", "kiri", "maju", "harta karun", "kanan", "mundur"]
print("Piko mengikuti peta:")
for langkah in langkah_peta:
    print(f"Piko melangkah: {langkah}")
    if langkah == "harta karun":
        print("Piko menemukan Harta Karun! Petualangan selesai!")
        break
print("Piko sangat senang!")

# Uh-Oh! Momen Kesalahan (break)
# Jika Piko lupa kondisi 'break' atau salah menempatkannya
# print("\\n--- Uh-Oh! Momen Kesalahan (break) ---")
# angka_dicari = 5
# list_angka = [1, 2, 3, 4, 5, 6, 7]
# ditemukan = False
# for angka in list_angka:
#     print(f"Mengecek angka: {angka}")
#     if angka == angka_dicari:
#         ditemukan = True
#         # Lupa break di sini, jadi loop terus berjalan meski sudah ditemukan
# print(f"Apakah angka {angka_dicari} ditemukan? {ditemukan}")
# print("Piko berpikir, 'Seharusnya aku berhenti mencari setelah ketemu agar lebih cepat!'")


# Cerita 6: Piko Menggunakan 'continue' untuk Melewati Genangan Air
print("\\n--- Cerita 6: Piko Menggunakan 'continue' untuk Melewati Genangan Air ---")
jalur_hutan = ["jalan setapak", "genangan air", "bunga indah", "genangan air", "pohon besar"]
print("Piko berjalan di hutan:")
for spot in jalur_hutan:
    if spot == "genangan air":
        print("Piko melihat genangan air, dia melompatinya!")
        continue
    print(f"Piko berada di: {spot}")
print("Piko berhasil melewati semua rintangan!")

# Uh-Oh! Momen Kesalahan (continue)
# Jika Piko salah logika dan 'continue' malah melewati hal penting
# print("\\n--- Uh-Oh! Momen Kesalahan (continue) ---")
# makanan_piko = ["apel", "pisang", "batu", "jeruk"]
# print("Piko mau makan buah:")
# for item in makanan_piko:
#     if item == "batu":
#         print("Ini batu, tidak bisa dimakan. Lanjut!")
#         continue
#     # Jika continue diletakkan sebelum print makan, maka tidak akan ada buah yang 'dimakan'
#     print(f"Piko makan {item}.")
# print("Piko berpikir, 'Pastikan aku tidak melewati buah yang enak karena salah 'continue'!'")

print("\\nPetualangan Piko dengan For Loop Lanjutan selesai! Sampai jumpa di petualangan berikutnya!")