print("Selamat datang di Petualangan Piko dengan Kantong Ajaib Serbaguna (List)!")

# Cerita 1: Piko Mengisi Kantong Ajaibnya
print("\n--- Cerita 1: Piko Mengisi Kantong Ajaibnya ---")
bekal_buah_piko = ["apel", "pisang", "jeruk"]
print(f"Isi kantong buah Piko: {bekal_buah_piko}")

mainan_piko = ["bola", "yoyo"]
print(f"Isi kantong mainan Piko: {mainan_piko}")

kantong_campuran = ["Bobi si Beruang", 5, "Lala si Kelinci", 4]
print(f"Isi kantong campuran Piko: {kantong_campuran}")

kantong_kosong = []
print(f"Piko punya kantong kosong: {kantong_kosong}")

# Mengintegrasikan contoh dari file sebelumnya (my_list)
my_list_from_file = [1, 2, 3, 4, 5]
print(f"Contoh list dari file (Original List): {my_list_from_file}")

# Cerita 2: Piko Melihat Isi Kantong (Mengakses Elemen)
print("\n--- Cerita 2: Piko Melihat Isi Kantong ---")
buah_pertama = bekal_buah_piko[0]
print(f"Buah pertama yang Piko ambil: {buah_pertama}")

buah_terakhir = bekal_buah_piko[2]
print(f"Buah terakhir di kantong Piko: {buah_terakhir}")

buah_terakhir_cara_lain = bekal_buah_piko[-1]
print(f"Buah terakhir (diambil dari belakang): {buah_terakhir_cara_lain}")

# Mengintegrasikan contoh dari file sebelumnya (accessing elements)
print(f"Contoh dari file (First element of my_list_from_file): {my_list_from_file[0]}")
print(f"Contoh dari file (Last element of my_list_from_file): {my_list_from_file[-1]}")

# Cerita 3: Piko Menambah Barang ke Kantong (Menambah Elemen)
print("\n--- Cerita 3: Piko Menambah Barang ke Kantong ---")
print(f"Kantong Piko awalnya: {bekal_buah_piko}")
bekal_buah_piko.append("mangga")
print(f"Setelah ditambah mangga (append): {bekal_buah_piko}")

bekal_buah_piko.insert(1, "anggur")
print(f"Setelah disisipi anggur (insert di indeks 1): {bekal_buah_piko}")

# Mengintegrasikan contoh dari file sebelumnya (adding an element)
my_list_from_file.append(6)
print(f"Contoh dari file (my_list_from_file after appending 6): {my_list_from_file}")

# Piko juga bisa menggabungkan dua kantong (extend)
kantong_tambahan = ["buku cerita", "krayon"]
bekal_buah_piko.extend(kantong_tambahan)
print(f"Setelah ditambah isi kantong tambahan (extend): {bekal_buah_piko}")

# Cerita 4: Piko Mengeluarkan Barang dari Kantong (Menghapus Elemen)
print("\n--- Cerita 4: Piko Mengeluarkan Barang dari Kantong ---")
# Kita gunakan list yang sudah di-extend untuk contoh ini
print(f"Kantong Piko sebelum ada yang dikeluarkan/dimakan: {bekal_buah_piko}")

if "pisang" in bekal_buah_piko:
    bekal_buah_piko.remove("pisang")
    print(f"Setelah pisang dimakan (remove 'pisang'): {bekal_buah_piko}")
else:
    print("Pisang tidak ada di kantong Piko untuk dikeluarkan.")

buah_yang_dikeluarkan_akhir = bekal_buah_piko.pop()
print(f"Piko mengeluarkan barang terakhir (pop): {buah_yang_dikeluarkan_akhir}")
print(f"Kantong Piko sekarang: {bekal_buah_piko}")

if len(bekal_buah_piko) > 0:
    buah_yang_dikeluarkan_pertama = bekal_buah_piko.pop(0)
    print(f"Piko mengeluarkan barang pertama (pop(0)): {buah_yang_dikeluarkan_pertama}")
    print(f"Kantong Piko akhirnya: {bekal_buah_piko}")
else:
    print("Kantong Piko sudah kosong, tidak ada yang bisa dikeluarkan dari depan.")

# Mengintegrasikan contoh dari file sebelumnya (removing an element)
if 3 in my_list_from_file:
    my_list_from_file.remove(3)
    print(f"Contoh dari file (my_list_from_file after removing 3): {my_list_from_file}")
else:
    print("Angka 3 tidak ada di my_list_from_file untuk dihapus.")

# Menghapus dengan del berdasarkan indeks
kantong_del_test = ['a', 'b', 'c', 'd', 'e']
print(f"Kantong untuk tes 'del': {kantong_del_test}")
if len(kantong_del_test) > 2:
    del kantong_del_test[2] # Hapus elemen di indeks 2 ('c')
    print(f"Setelah 'del kantong_del_test[2]': {kantong_del_test}")

# Cerita 5: Piko Memeriksa Semua Isi Kantong Satu per Satu (Iterasi)
print("\n--- Cerita 5: Piko Memeriksa Semua Isi Kantong ---")
print(f"Piko memeriksa kantong mainannya ({mainan_piko}):")
for mainan in mainan_piko:
    print(f"- Piko punya {mainan}")

# Mengintegrasikan contoh dari file sebelumnya (iterating through the list)
print(f"Contoh dari file (Iterating through my_list_from_file: {my_list_from_file}):")
for item in my_list_from_file:
    print(item)

# Cerita 6: Mantra Kantong Ajaib Lainnya
print("\n--- Cerita 6: Mantra Kantong Ajaib Lainnya ---")
kantong_buah_akhir = ["anggur", "jeruk", "apel"] # Reset untuk contoh ini
print(f"Kantong buah Piko untuk mantra lain: {kantong_buah_akhir}")
print(f"Jumlah buah di kantong Piko (len): {len(kantong_buah_akhir)}")

if "jeruk" in kantong_buah_akhir:
    posisi_jeruk = kantong_buah_akhir.index("jeruk")
    print(f"Jeruk ada di posisi (index): {posisi_jeruk}")
else:
    print("Jeruk tidak ditemukan di kantong.")

kantong_apel_banyak = ["apel", "pisang", "apel", "mangga", "apel"]
jumlah_apel = kantong_apel_banyak.count("apel")
print(f"Di kantong {kantong_apel_banyak}, ada {jumlah_apel} apel (count)." )

buah_acak = ["kiwi", "stroberi", "anggur", "pisang"]
print(f"Buah sebelum diurutkan: {buah_acak}")
buah_terurut_baru = sorted(buah_acak) 
print(f"Buah setelah diurutkan (sorted(), list baru): {buah_terurut_baru}")
print(f"Buah acak asli masih sama: {buah_acak}")
buah_acak.sort() 
print(f"Buah setelah diurutkan (sort(), list asli berubah): {buah_acak}")

buah_acak.reverse() 
print(f"Buah setelah dibalik urutannya (reverse): {buah_acak}")

# Membersihkan kantong (clear)
print(f"Kantong buah acak sebelum di-clear: {buah_acak}")
buah_acak.clear()
print(f"Kantong buah acak setelah di-clear: {buah_acak}")

# Menyalin kantong (copy)
kantong_asli = [10, 20, 30]
kantong_salinan = kantong_asli.copy()
print(f"Kantong asli: {kantong_asli}")
print(f"Kantong salinan: {kantong_salinan}")
kantong_salinan.append(40)
print(f"Kantong salinan setelah ditambah 40: {kantong_salinan}")
print(f"Kantong asli tetap tidak berubah: {kantong_asli}")

# Uh-Oh! Momen Kesalahan
print("\n--- Uh-Oh! Momen Kesalahan dengan Kantong Ajaib ---")
# IndexError
# print("Mencoba mengambil barang di luar jangkauan:")
# kantong_error = [1, 2]
# print(kantong_error[2]) # Akan menyebabkan IndexError

# ValueError
# print("\nMencoba mengeluarkan barang yang tidak ada:")
# kantong_error_value = ["apel", "pisang"]
# kantong_error_value.remove("semangka") # Akan menyebabkan ValueError

print("\nPetualangan Piko dengan Kantong Ajaib selesai! Ia jadi mahir mengatur barang-barangnya!")

# Fungsi main() dari file asli, sekarang sudah terintegrasi
# def main():
#     # ... (kode asli dari file)
#     pass

# if __name__ == "__main__":
#     # main() # Tidak perlu dipanggil lagi
#     print("Semua contoh list telah dijalankan melalui cerita Piko.")