print("Selamat datang di Petualangan Piko dengan Kamus Ajaib (Dictionary)!")

# Cerita 1: Piko Membuat Kamus Pertamanya
print("\n--- Cerita 1: Piko Membuat Kamus Pertamanya ---")
makanan_kesukaan = {
    "Bobi": "Madu",
    "Lala": "Wortel",
    "Kura": "Daun Selada"
}
print(f"Kamus makanan kesukaan teman Piko: {makanan_kesukaan}")

kamus_baru_piko = {}
print(f"Piko membuat kamus baru yang masih kosong: {kamus_baru_piko}")

# Mengintegrasikan contoh dari file sebelumnya (create_dictionary)
# Fungsi create_dictionary() dari file asli:
def create_dictionary_from_file():
    sample_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    return sample_dict

kamus_dari_file = create_dictionary_from_file()
print(f"Contoh kamus dari file (kamus_dari_file): {kamus_dari_file}")

# Cerita 2: Piko Mencari Keterangan di Kamusnya (Mengakses Nilai)
print("\n--- Cerita 2: Piko Mencari Keterangan di Kamusnya ---")
makanan_lala = makanan_kesukaan["Lala"]
print(f"Makanan kesukaan Lala adalah: {makanan_lala}")

makanan_bobi = makanan_kesukaan.get("Bobi")
print(f"Makanan kesukaan Bobi (pakai get): {makanan_bobi}")

makanan_monyet = makanan_kesukaan.get("Monyet")
print(f"Makanan kesukaan Monyet (get, tidak ada): {makanan_monyet}")

makanan_monyet_dengan_pesan = makanan_kesukaan.get("Monyet", "Piko belum tahu")
print(f"Makanan kesukaan Monyet (get, dengan pesan default): {makanan_monyet_dengan_pesan}")

# Cerita 3: Piko Menambah atau Mengubah Catatan di Kamus
print("\n--- Cerita 3: Piko Menambah atau Mengubah Catatan ---")
print(f"Kamus Piko awalnya: {makanan_kesukaan}")

makanan_kesukaan["Sisi"] = "Kacang"  # Menambah Sisi
print(f"Setelah Sisi ditambahkan: {makanan_kesukaan}")

makanan_kesukaan["Lala"] = "Apel"  # Mengubah makanan Lala
print(f"Setelah makanan Lala diubah: {makanan_kesukaan}")

# Menggunakan update() untuk menambah/mengubah beberapa sekaligus
kantor_piko = {"lokasi": "Hutan Ceria", "jam_buka": "Pagi Hari"}
piko_info = {"nama": "Piko", "jenis": "Kancil Koding"}
piko_info.update(kantor_piko) # Menambahkan semua dari kantor_piko ke piko_info
piko_info.update({"umur_tahun_ini": 1, "status": "Belajar Koding"})
print(f"Info lengkap Piko setelah di-update: {piko_info}")

# Cerita 4: Piko Menghapus Catatan dari Kamus
print("\n--- Cerita 4: Piko Menghapus Catatan ---")
print(f"Kamus makanan sebelum ada yang dihapus: {makanan_kesukaan}")

if "Kura" in makanan_kesukaan:
    makanan_kura_dihapus = makanan_kesukaan.pop("Kura")
    print(f"Piko menghapus Kura (yang suka {makanan_kura_dihapus}) dengan pop().")
    print(f"Kamus setelah Kura dihapus: {makanan_kesukaan}")
else:
    print("Kura tidak ada di kamus untuk dihapus dengan pop().")

if "Bobi" in makanan_kesukaan:
    del makanan_kesukaan["Bobi"]
    print(f"Piko menghapus Bobi dengan 'del'.")
    print(f"Kamus setelah Bobi dihapus: {makanan_kesukaan}")
else:
    print("Bobi tidak ada di kamus untuk dihapus dengan 'del'.")

# Menghapus item terakhir (Python 3.7+)
# if piko_info: # Cek apakah dictionary tidak kosong
#     item_terakhir_dihapus = piko_info.popitem()
#     print(f"Item terakhir yang dihapus dari piko_info (popitem): {item_terakhir_dihapus}")
#     print(f"piko_info setelah popitem: {piko_info}")

# Cerita 5: Piko Memeriksa Semua Isi Kamusnya
print("\n--- Cerita 5: Piko Memeriksa Semua Isi Kamusnya ---")
makanan_kesukaan_akhir = {"Lala": "Apel", "Sisi": "Kacang", "Tupi": "Biji Pinus"} # Reset untuk contoh
print(f"Kamus Piko untuk diperiksa: {makanan_kesukaan_akhir}")

print("\nTeman-teman Piko (kata kunci dari .keys()):")
for teman in makanan_kesukaan_akhir.keys():
    print(f"- {teman}")

print("\nMakanan kesukaan (keterangan dari .values()):")
for makanan in makanan_kesukaan_akhir.values():
    print(f"- {makanan}")

print("\nSemua catatan di Kamus Piko (pasangan dari .items()):")
for teman, makanan in makanan_kesukaan_akhir.items():
    print(f"- {teman} suka {makanan}")

# Mengintegrasikan contoh dari file sebelumnya (print_dictionary_info)
# Fungsi print_dictionary_info dari file asli:
def print_dictionary_info_from_file(dictionary):
    print("\nInfo dari print_dictionary_info_from_file:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

print_dictionary_info_from_file(kamus_dari_file)

# Cerita 6: Mantra Kamus Ajaib Lainnya
print("\n--- Cerita 6: Mantra Kamus Ajaib Lainnya ---")
print(f"Apakah 'Lala' ada di kamus makanan_kesukaan_akhir? {"Lala" in makanan_kesukaan_akhir}")
print(f"Apakah 'Bobi' ada di kamus makanan_kesukaan_akhir? {"Bobi" in makanan_kesukaan_akhir}")

jumlah_catatan = len(makanan_kesukaan_akhir)
print(f"Jumlah catatan di kamus makanan_kesukaan_akhir (len): {jumlah_catatan}")

# Menyalin kamus (copy)
kamus_asli_copy = {"a": 1, "b": 2}
kamus_salinan_copy = kamus_asli_copy.copy()
print(f"Kamus asli untuk copy: {kamus_asli_copy}")
print(f"Kamus salinan: {kamus_salinan_copy}")
kamus_salinan_copy["c"] = 3
print(f"Salinan setelah ditambah 'c': {kamus_salinan_copy}")
print(f"Asli tetap tidak berubah: {kamus_asli_copy}")

# Membuat kamus dari list of keys (dict.fromkeys)
kunci_hewan = ["gajah", "harimau", "jerapah"]
nilai_default_habitat = "Hutan Tropis"
kamus_habitat_hewan = dict.fromkeys(kunci_hewan, nilai_default_habitat)
print(f"Kamus habitat hewan (fromkeys): {kamus_habitat_hewan}")

# Uh-Oh! Momen Kesalahan
print("\n--- Uh-Oh! Momen Kesalahan dengan Kamus Ajaib ---")
# KeyError
# print("Mencoba mengakses kunci yang tidak ada secara langsung:")
# kamus_error = {"nama": "Piko"}
# print(kamus_error["umur"]) # Akan menyebabkan KeyError

print("Piko belajar: Selalu cek dengan 'in' atau gunakan .get() untuk menghindari KeyError!")

print("\nPetualangan Piko dengan Kamus Ajaib selesai! Ia jadi ahli menyimpan dan mencari informasi!")

# if __name__ == "__main__":
#     # Kode dari __main__ di file asli sudah terintegrasi ke dalam cerita Piko.
#     # my_dict_original = create_dictionary_from_file()
#     # print_dictionary_info_from_file(my_dict_original)
#     print("Semua contoh dictionary telah dijalankan melalui cerita Piko.")