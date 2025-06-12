# Piko si Koding Kancil dan Kantong Ajaib Serbaguna (List)

Petualangan Piko si Koding Kancil berlanjut! Setelah bermain dengan Gulungan Pesan Ajaib (String), Piko menemukan sebuah Kantong Ajaib. Kantong ini istimewa karena bisa menyimpan banyak barang berbeda secara berurutan, dan isinya bisa diubah-ubah! Di dunia koding, kantong ini disebut "List".

## Cerita 1: Piko Mengisi Kantong Ajaibnya

Piko ingin membawa bekal untuk petualangannya. Dia memasukkan beberapa buah ke dalam Kantong Ajaibnya:
1.  Apel
2.  Pisang
3.  Jeruk

Kantong Ajaib Piko sekarang berisi: `["apel", "pisang", "jeruk"]`

Piko juga ingin membawa mainannya:
1.  Bola
2.  Yoyo

Dia membuat kantong baru untuk mainan: `["bola", "yoyo"]`

Piko bahkan bisa membuat kantong yang isinya campuran, misalnya nama teman dan umurnya: `["Bobi si Beruang", 5, "Lala si Kelinci", 4]`

**Kode Python-nya:**

```python
# main.py
# Kantong buah Piko
bekal_buah_piko = ["apel", "pisang", "jeruk"]
# print(f"Isi kantong buah Piko: {bekal_buah_piko}")

# Kantong mainan Piko
mainan_piko = ["bola", "yoyo"]
# print(f"Isi kantong mainan Piko: {mainan_piko}")

# Kantong campuran
kantong_campuran = ["Bobi si Beruang", 5, "Lala si Kelinci", 4]
# print(f"Isi kantong campuran Piko: {kantong_campuran}")

# Kantong kosong juga bisa!
kantong_kosong = []
# print(f"Piko punya kantong kosong: {kantong_kosong}")
```

## Cerita 2: Piko Melihat Isi Kantong (Mengakses Elemen)

Piko ingin mengambil buah pertama dari kantong bekalnya.
Kantong Ajaib memberitahu, "Barang pertama (nomor 0) adalah `apel`."

Lalu Piko ingin tahu buah terakhir.
Kantong Ajaib berkata, "Barang terakhir (nomor 2 atau -1 dari belakang) adalah `jeruk`."

Sama seperti string, setiap barang di dalam list punya nomor urut (indeks) yang dimulai dari 0.

**Kode Python-nya:**

```python
# main.py
# bekal_buah_piko = ["apel", "pisang", "jeruk"]

buah_pertama = bekal_buah_piko[0]
# print(f"Buah pertama yang Piko ambil: {buah_pertama}")

buah_terakhir = bekal_buah_piko[2]
# print(f"Buah terakhir di kantong Piko: {buah_terakhir}")

# Mengambil dari belakang juga bisa!
buah_terakhir_cara_lain = bekal_buah_piko[-1]
# print(f"Buah terakhir (diambil dari belakang): {buah_terakhir_cara_lain}")
```

## Cerita 3: Piko Menambah Barang ke Kantong (Menambah Elemen)

Piko menemukan buah mangga dan ingin menambahkannya ke kantong bekal buahnya.
"Kantong Ajaib, tambahkan `mangga` di paling belakang!" (`append()`)
Isi kantong Piko sekarang: `["apel", "pisang", "jeruk", "mangga"]`

Lalu Piko ingin menyisipkan buah `anggur` setelah `apel` (di posisi nomor 1).
"Kantong Ajaib, sisipkan `anggur` di urutan kedua!" (`insert()`)
Isi kantong Piko sekarang: `["apel", "anggur", "pisang", "jeruk", "mangga"]`

**Kode Python-nya:**

```python
# main.py
# bekal_buah_piko = ["apel", "pisang", "jeruk"]
# print(f"Kantong Piko awalnya: {bekal_buah_piko}")

# Menambah mangga di akhir
bekal_buah_piko.append("mangga")
# print(f"Setelah ditambah mangga: {bekal_buah_piko}")

# Menyisipkan anggur di posisi indeks 1
bekal_buah_piko.insert(1, "anggur")
# print(f"Setelah disisipi anggur: {bekal_buah_piko}")
```

## Cerita 4: Piko Mengeluarkan Barang dari Kantong (Menghapus Elemen)

Piko sudah memakan buah `pisang`. Dia ingin mengeluarkannya dari kantong.
"Kantong Ajaib, keluarkan `pisang`!" (`remove()`)
Isi kantong Piko: `["apel", "anggur", "jeruk", "mangga"]` (Pisang pertama yang ditemukan akan dihapus)

Kemudian, Piko ingin mengeluarkan buah terakhir yang dia masukkan, yaitu `mangga`.
"Kantong Ajaib, keluarkan barang terakhir!" (`pop()`)
Kantong Ajaib mengeluarkan `mangga` dan memberikannya pada Piko.
Isi kantong Piko: `["apel", "anggur", "jeruk"]`

Piko juga bisa mengeluarkan barang dari posisi tertentu, misalnya barang pertama (indeks 0).
"Kantong Ajaib, keluarkan barang di urutan pertama!" (`pop(0)`)
Kantong Ajaib mengeluarkan `apel`.
Isi kantong Piko: `["anggur", "jeruk"]`

**Kode Python-nya:**

```python
# main.py
# bekal_buah_piko = ["apel", "anggur", "pisang", "jeruk", "mangga"]
# print(f"Kantong Piko sebelum ada yang dimakan: {bekal_buah_piko}")

# Piko makan pisang
bekal_buah_piko.remove("pisang")
# print(f"Setelah pisang dimakan: {bekal_buah_piko}")

# Piko mengeluarkan mangga (terakhir)
buah_yang_dikeluarkan_akhir = bekal_buah_piko.pop()
# print(f"Piko mengeluarkan buah terakhir: {buah_yang_dikeluarkan_akhir}")
# print(f"Kantong Piko sekarang: {bekal_buah_piko}")

# Piko mengeluarkan apel (pertama)
buah_yang_dikeluarkan_pertama = bekal_buah_piko.pop(0)
# print(f"Piko mengeluarkan buah pertama: {buah_yang_dikeluarkan_pertama}")
# print(f"Kantong Piko akhirnya: {bekal_buah_piko}")
```

## Cerita 5: Piko Memeriksa Semua Isi Kantong Satu per Satu (Iterasi)

Piko ingin melihat semua mainan yang ada di kantong mainannya.
"Kantong Ajaib, tunjukkan semua mainanku satu per satu!"

Kantong Ajaib menampilkan:
- `bola`
- `yoyo`

Ini seperti menggunakan `for` loop untuk list!

**Kode Python-nya:**

```python
# main.py
# mainan_piko = ["bola", "yoyo", "gasing", "robot"]
# print("\nPiko memeriksa kantong mainannya:")
# for mainan in mainan_piko:
#     print(f"- Piko punya {mainan}")
```

## Cerita 6: Mantra Kantong Ajaib Lainnya

Kantong Ajaib punya banyak mantra lain!

1.  **Mantra Hitung Jumlah (`len()`):**
    Piko bertanya, "Ada berapa banyak buah di kantongku?"
    Kantong: `["anggur", "jeruk"]`. Mantra `len()`: "Ada 2 buah!"
2.  **Mantra Cari Barang (`index()`):**
    Piko mencari `jeruk`. "Kantong Ajaib, di mana `jeruk`?"
    Mantra `index()`: "`jeruk` ada di nomor urut 1."
3.  **Mantra Hitung Barang Tertentu (`count()`):**
    Piko punya kantong `["apel", "pisang", "apel"]`. "Ada berapa `apel`?"
    Mantra `count()`: "Ada 2 `apel`."
4.  **Mantra Urutkan Barang (`sort()` dan `sorted()`):**
    Piko punya kantong buah `["jeruk", "apel", "pisang"]`.
    Mantra `sort()`: Mengurutkan isi kantongnya langsung menjadi `["apel", "jeruk", "pisang"]`.
    Mantra `sorted()`: Memberi Piko daftar urut yang baru `["apel", "jeruk", "pisang"]` tapi kantong aslinya tetap.
5.  **Mantra Balik Urutan (`reverse()`):**
    Piko punya `["apel", "jeruk", "pisang"]`. Mantra `reverse()` mengubahnya jadi `["pisang", "jeruk", "apel"]`.

**Kode Python-nya:**

```python
# main.py
# kantong_buah_akhir = ["anggur", "jeruk"]
# print(f"\nKantong buah Piko saat ini: {kantong_buah_akhir}")
# print(f"Jumlah buah di kantong Piko: {len(kantong_buah_akhir)}")

# posisi_jeruk = kantong_buah_akhir.index("jeruk")
# print(f"Jeruk ada di posisi: {posisi_jeruk}")

# kantong_apel_banyak = ["apel", "pisang", "apel", "mangga", "apel"]
# jumlah_apel = kantong_apel_banyak.count("apel")
# print(f"Di kantong {kantong_apel_banyak}, ada {jumlah_apel} apel.")

# buah_acak = ["kiwi", "stroberi", "anggur", "pisang"]
# print(f"Buah sebelum diurutkan: {buah_acak}")
# buah_terurut_baru = sorted(buah_acak) # Membuat list baru yang terurut
# print(f"Buah setelah diurutkan (sorted(), list baru): {buah_terurut_baru}")
# print(f"Buah acak asli masih sama: {buah_acak}")
# buah_acak.sort() # Mengurutkan list aslinya
# print(f"Buah setelah diurutkan (sort(), list asli berubah): {buah_acak}")

# buah_acak.reverse() # Membalik urutan list asli
# print(f"Buah setelah dibalik urutannya: {buah_acak}")
```

## Uh-Oh! Momen Kesalahan dengan Kantong Ajaib

1.  **Salah Ambil Barang (IndexError):**
    Sama seperti string, jika Piko punya 2 buah di kantong (indeks 0 dan 1) dan mencoba mengambil buah di nomor urut 2 (`kantong[2]`), Kantong Ajaib akan bingung!
    *   **Pesan Error di Python:** `IndexError: list index out of range`
    *   **Piko berkata:** "Waduh! Aku salah hitung nomor barangnya!"

2.  **Mencoba Mengeluarkan Barang yang Tidak Ada (ValueError):**
    Jika Piko mencoba mengeluarkan buah `semangka` dari kantongnya (`kantong.remove("semangka")`), padahal tidak ada semangka di sana.
    *   **Pesan Error di Python:** `ValueError: list.remove(x): x not in list`
    *   **Piko berkata:** "Lho, kok tidak ada semangka? Aku pasti salah ingat!"

Piko sangat senang dengan Kantong Ajaib Serbaguna miliknya. Dia bisa menyimpan apa saja, mengaturnya, menambah, dan mengurangi isinya dengan mudah! Petualangan Piko jadi lebih terorganisir. Sampai jumpa di petualangan berikutnya!
