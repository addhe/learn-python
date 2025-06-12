# Piko si Koding Kancil dan Kamus Ajaib Piko (Dictionary)

Petualangan Piko si Koding Kancil semakin seru! Kali ini, Piko menemukan sebuah buku catatan kuno yang sangat istimewa. Buku ini bukan buku biasa, melainkan "Kamus Ajaib Piko"! Di kamus ini, Piko bisa menyimpan informasi dengan cara yang unik: setiap informasi punya "kata kunci" khusus untuk menemukannya. Di dunia koding, ini disebut "Dictionary" atau kamus.

Berbeda dengan Kantong Ajaib (List) yang menyimpan barang berurutan pakai nomor, Kamus Ajaib ini menyimpan barang pakai "kata kunci" (key) dan "keterangannya" (value).

## Cerita 1: Piko Membuat Kamus Pertamanya

Piko ingin mencatat makanan kesukaan teman-temannya.

-   Bobi si Beruang, kata kuncinya `"Bobi"`, keterangannya `"Madu"`.
-   Lala si Kelinci, kata kuncinya `"Lala"`, keterangannya `"Wortel"`.
-   Kura si Kura-kura, kata kuncinya `"Kura"`, keterangannya `"Daun Selada"`.

Kamus Ajaib Piko sekarang berisi:
`{"Bobi": "Madu", "Lala": "Wortel", "Kura": "Daun Selada"}`

Piko juga bisa membuat kamus kosong dulu, lalu mengisinya nanti.
`kamus_kosong_piko = {}`

**Kode Python-nya:**

```python
# main.py
# Kamus makanan kesukaan teman Piko
makanan_kesukaan = {
    "Bobi": "Madu",
    "Lala": "Wortel",
    "Kura": "Daun Selada"
}
# print(f"Kamus makanan kesukaan teman Piko: {makanan_kesukaan}")

# Kamus kosong
kamus_baru_piko = {}
# print(f"Piko membuat kamus baru yang masih kosong: {kamus_baru_piko}")
```

## Cerita 2: Piko Mencari Keterangan di Kamusnya (Mengakses Nilai)

Piko ingin tahu apa makanan kesukaan Lala.
"Kamus Ajaib, apa makanan kesukaan `Lala`?" tanya Piko.
Kamus Ajaib langsung membuka halaman dengan kata kunci `"Lala"` dan menjawab: `"Wortel"`.

Bagaimana jika Piko mencari teman yang tidak ada di kamus, misalnya `"Monyet"`?
Jika Piko langsung mencari `makanan_kesukaan["Monyet"]`, Kamus Ajaib akan bingung karena tidak ada kata kunci itu (ini bisa menyebabkan error!).

Cara yang lebih aman adalah menggunakan mantra `get()`.
"Kamus Ajaib, apa makanan kesukaan `Monyet`? Kalau tidak ada, bilang saja `'Tidak tahu'`." (`get("Monyet", "Tidak tahu")`)
Kamus Ajaib akan menjawab: `"Tidak tahu"`.

**Kode Python-nya:**

```python
# main.py
# makanan_kesukaan = {"Bobi": "Madu", "Lala": "Wortel", "Kura": "Daun Selada"}

makanan_lala = makanan_kesukaan["Lala"]
# print(f"Makanan kesukaan Lala adalah: {makanan_lala}")

# Menggunakan get() untuk keamanan
makanan_bobi = makanan_kesukaan.get("Bobi")
# print(f"Makanan kesukaan Bobi (pakai get): {makanan_bobi}")

makanan_monyet = makanan_kesukaan.get("Monyet") # Tidak ada di kamus
# print(f"Makanan kesukaan Monyet: {makanan_monyet}") # Hasilnya None (kosong)

makanan_monyet_dengan_pesan = makanan_kesukaan.get("Monyet", "Piko belum tahu")
# print(f"Makanan kesukaan Monyet (dengan pesan jika tidak ada): {makanan_monyet_dengan_pesan}")
```

## Cerita 3: Piko Menambah atau Mengubah Catatan di Kamus

Piko bertemu teman baru, Sisi si Tupai, yang suka `"Kacang"`.
Piko menambahkan catatan baru ke kamusnya:
Kata kuncinya `"Sisi"`, keterangannya `"Kacang"`.
Kamus Piko sekarang: `{"Bobi": "Madu", "Lala": "Wortel", "Kura": "Daun Selada", "Sisi": "Kacang"}`

Ternyata, Lala sekarang juga suka `"Apel"` selain wortel. Piko ingin mengubah catatan Lala.
"Kamus Ajaib, ubah makanan kesukaan `Lala` menjadi `"Apel"`."
Kamus Piko sekarang: `{"Bobi": "Madu", "Lala": "Apel", "Kura": "Daun Selada", "Sisi": "Kacang"}`

**Kode Python-nya:**

```python
# main.py
# makanan_kesukaan = {"Bobi": "Madu", "Lala": "Wortel", "Kura": "Daun Selada"}
# print(f"Kamus Piko awalnya: {makanan_kesukaan}")

# Menambah teman baru
makanan_kesukaan["Sisi"] = "Kacang"
# print(f"Setelah Sisi ditambahkan: {makanan_kesukaan}")

# Mengubah makanan kesukaan Lala
makanan_kesukaan["Lala"] = "Apel"
# print(f"Setelah makanan Lala diubah: {makanan_kesukaan}")
```

## Cerita 4: Piko Menghapus Catatan dari Kamus

Kura pindah ke hutan lain. Piko ingin menghapus catatan tentang Kura.
"Kamus Ajaib, hapus catatan untuk `Kura`." (`pop()`)
Kamus Ajaib akan menghapus catatan Kura dan memberitahu Piko apa makanan kesukaan Kura yang dihapus (`"Daun Selada"`).
Isi kamus Piko: `{"Bobi": "Madu", "Lala": "Apel", "Sisi": "Kacang"}`

Piko juga bisa menghapus pakai mantra `del`.
"Kamus Ajaib, hapus saja catatan untuk `Bobi`." (`del makanan_kesukaan["Bobi"]`)
Isi kamus Piko: `{"Lala": "Apel", "Sisi": "Kacang"}`

**Kode Python-nya:**

```python
# main.py
# makanan_kesukaan = {"Bobi": "Madu", "Lala": "Apel", "Kura": "Daun Selada", "Sisi": "Kacang"}
# print(f"Kamus Piko sebelum ada yang dihapus: {makanan_kesukaan}")

# Menghapus Kura dengan pop()
makanan_kura_dihapus = makanan_kesukaan.pop("Kura")
# print(f"Piko menghapus Kura yang suka: {makanan_kura_dihapus}")
# print(f"Kamus setelah Kura dihapus: {makanan_kesukaan}")

# Menghapus Bobi dengan del
# if "Bobi" in makanan_kesukaan: # Sebaiknya cek dulu sebelum del
#     del makanan_kesukaan["Bobi"]
#     print(f"Kamus setelah Bobi dihapus dengan del: {makanan_kesukaan}")
# else:
#     print("Bobi tidak ada di kamus untuk dihapus dengan del.")
```

## Cerita 5: Piko Memeriksa Semua Isi Kamusnya

Piko ingin tahu siapa saja teman yang sudah dicatat di kamusnya.
"Kamus Ajaib, siapa saja yang ada di kamus?" (menggunakan `.keys()`)
Kamus: `["Lala", "Sisi"]` (urutan bisa berbeda-beda!)

Piko ingin tahu apa saja makanan kesukaan yang tercatat.
"Kamus Ajaib, makanan apa saja yang tercatat?" (menggunakan `.values()`)
Kamus: `["Apel", "Kacang"]`

Piko ingin melihat semua pasangan kata kunci dan keterangannya.
"Kamus Ajaib, tunjukkan semua catatanmu!" (menggunakan `.items()`)
Kamus:
-   `Lala` -> `Apel`
-   `Sisi` -> `Kacang`

Ini seperti menggunakan `for` loop untuk dictionary!

**Kode Python-nya:**

```python
# main.py
# makanan_kesukaan_akhir = {"Lala": "Apel", "Sisi": "Kacang"}
# print(f"\nKamus Piko saat ini: {makanan_kesukaan_akhir}")

# Melihat semua kata kunci (nama teman)
# print("\nTeman-teman Piko yang tercatat (kata kunci):")
# for teman in makanan_kesukaan_akhir.keys():
#     print(f"- {teman}")

# Melihat semua keterangan (makanan kesukaan)
# print("\nMakanan kesukaan yang tercatat (keterangan):")
# for makanan in makanan_kesukaan_akhir.values():
#     print(f"- {makanan}")

# Melihat semua pasangan catatan
# print("\nSemua catatan di Kamus Piko (pasangan kunci-nilai):")
# for teman, makanan in makanan_kesukaan_akhir.items():
#     print(f"- {teman} suka {makanan}")
```

## Cerita 6: Mantra Kamus Ajaib Lainnya

1.  **Mantra Cek Kata Kunci (`in`):**
    Piko bertanya, "Apakah `Lala` ada di kamusku?"
    Kamus: "Ya, `Lala` ada!" (`"Lala" in makanan_kesukaan`)
2.  **Mantra Hitung Jumlah Catatan (`len()`):**
    Piko: "Ada berapa catatan di kamusku?"
    Kamus: `{"Lala": "Apel", "Sisi": "Kacang"}`. Mantra `len()`: "Ada 2 catatan!"

**Kode Python-nya:**

```python
# main.py
# makanan_kesukaan_akhir = {"Lala": "Apel", "Sisi": "Kacang"}

# Cek apakah Lala ada
# if "Lala" in makanan_kesukaan_akhir:
#     print(f"\nYa, catatan untuk Lala ada di kamus.")
# else:
#     print(f"\nCatatan untuk Lala tidak ada.")

# Cek apakah Bobi ada (setelah dihapus)
# if "Bobi" in makanan_kesukaan_akhir:
#     print(f"Catatan untuk Bobi masih ada.")
# else:
#     print(f"Catatan untuk Bobi sudah tidak ada.")

# Jumlah catatan
# jumlah_catatan = len(makanan_kesukaan_akhir)
# print(f"Jumlah catatan di Kamus Piko: {jumlah_catatan}")
```

## Uh-Oh! Momen Kesalahan dengan Kamus Ajaib

1.  **Mencari dengan Kata Kunci yang Salah (KeyError):**
    Jika Piko mencoba mencari makanan kesukaan `"Kucing"` langsung dengan `makanan_kesukaan["Kucing"]` padahal Kucing tidak ada di kamusnya, Kamus Ajaib akan berteriak! "Kata kunci `Kucing` tidak ditemukan!"
    *   **Pesan Error di Python:** `KeyError: 'Kucing'`
    *   **Piko berkata:** "Oh tidak! Aku salah tulis kata kuncinya atau memang belum ada! Sebaiknya aku pakai mantra `get()` atau cek dengan `in` dulu."

2.  **Kata Kunci Harus Unik:**
    Piko tidak bisa punya dua catatan dengan kata kunci yang sama persis. Jika Piko mencoba menambahkan `"Lala": "Stroberi"` padahal sudah ada `"Lala": "Apel"`, catatan lama untuk Lala akan tergantikan dengan yang baru.
    *   **Piko mengerti:** "Setiap kata kunci itu seperti nama unik untuk satu keterangan. Kalau aku pakai nama yang sama lagi, keterangan lamanya akan hilang diganti yang baru."

Piko kini sangat pandai menggunakan Kamus Ajaibnya. Dia bisa menyimpan dan mencari informasi dengan cepat menggunakan kata kunci. Petualangan Piko jadi lebih teratur dan penuh pengetahuan! Sampai jumpa di petualangan berikutnya!
