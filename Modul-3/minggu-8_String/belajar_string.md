# Piko si Koding Kancil dan Gulungan Pesan Ajaib (String)

Selamat datang lagi di petualangan Piko si Koding Kancil! Hari ini, Piko menemukan sebuah gulungan perkamen tua di sebuah gua. Gulungan ini berisi pesan-pesan ajaib yang bisa berubah dan dimainkan! Pesan-pesan ini di dunia koding disebut "String".

String itu seperti untaian huruf, angka, atau simbol yang Piko tulis di atas kertas. Setiap pesan punya cerita sendiri!

## Cerita 1: Piko Menulis Pesan Pertamanya

Piko ingin menulis namanya di gulungan ajaib.
"Gulungan Ajaib, tuliskan namaku!" kata Piko.
Di gulungan itu muncul tulisan: `Piko`

Lalu Piko ingin menulis salam.
"Gulungan Ajaib, tuliskan salam untuk temanku!"
Di gulungan muncul: `Halo Kawan!`

Piko belajar bahwa membuat string itu mudah, tinggal tulis saja pesannya di antara tanda kutip!

**Kode Python-nya:**

```python
# main.py
nama_piko = "Piko"
salam = 'Halo Kawan!' # Boleh pakai kutip satu atau dua

# print(f"Pesan pertama Piko: {nama_piko}")
# print(f"Pesan kedua Piko: {salam}")
```

## Cerita 2: Piko Menggabungkan Pesan

Piko punya dua potongan pesan: `Aku Suka` dan `Apel Merah`. Dia ingin menggabungkannya menjadi satu pesan panjang.
"Gulungan Ajaib, gabungkan pesanku!"
Gulungan itu menyatukan kedua pesan: `Aku SukaApel Merah`

"Hmm, kok tidak ada spasi ya?" Piko berpikir. Dia lalu menambahkan spasi sendiri.
Potongan pertama: `Aku Suka ` (dengan spasi di akhir)
Potongan kedua: `Apel Merah`
Sekarang gulungan menampilkan: `Aku Suka Apel Merah`

Piko senang! Menggabungkan string disebut **konkatenasi**.

**Kode Python-nya:**

```python
# main.py
pesan1 = "Aku Suka "
pesan2 = "Apel Merah"
pesan_lengkap = pesan1 + pesan2 # Ini konkatenasi

# print(f"Pesan gabungan Piko: {pesan_lengkap}")

nama_hewan = "Kancil"
nama_panggilan = "Koding " + nama_hewan
# print(f"Nama panggilan Piko: {nama_panggilan}")
```

## Cerita 3: Piko Menghitung Panjang Pesan

Piko penasaran, "Seberapa panjang ya pesanku yang bertuliskan `Piko`?"
Gulungan Ajaib memberitahu, "Pesanmu punya 4 huruf!" (P-I-K-O)

Lalu untuk pesan `Halo Kawan!`, Gulungan Ajaib berkata, "Pesanmu punya 11 karakter, termasuk spasi dan tanda seru!"

Ini disebut mengetahui **panjang string**.

**Kode Python-nya:**

```python
# main.py
pesan_pendek = "Piko"
panjang_pesan_pendek = len(pesan_pendek)
# print(f"Pesan '{pesan_pendek}' panjangnya: {panjang_pesan_pendek}")

pesan_panjang = "Halo Kawan!"
panjang_pesan_panjang = len(pesan_panjang)
# print(f"Pesan '{pesan_panjang}' panjangnya: {panjang_pesan_panjang}")
```

## Cerita 4: Piko Membaca Huruf Satu per Satu (Indexing)

Piko ingin tahu huruf pertama dari namanya, `Piko`.
Gulungan Ajaib menunjukkan: `P`
"Bagaimana kalau huruf ketiga?" tanya Piko.
Gulungan Ajaib menunjukkan: `k`

Piko belajar bahwa setiap huruf dalam string punya nomor urut (indeks), dimulai dari 0.
Untuk `Piko`:
- `P` ada di nomor 0
- `i` ada di nomor 1
- `k` ada di nomor 2
- `o` ada di nomor 3

**Kode Python-nya:**

```python
# main.py
nama = "Piko"
huruf_pertama = nama[0] # Indeks 0 untuk huruf pertama
huruf_ketiga = nama[2]  # Indeks 2 untuk huruf ketiga

# print(f"Huruf pertama dari '{nama}' adalah: {huruf_pertama}")
# print(f"Huruf ketiga dari '{nama}' adalah: {huruf_ketiga}")
```

## Cerita 5: Piko Mengambil Potongan Pesan (Slicing)

Piko punya pesan `KodingKancil`. Dia ingin mengambil kata `Koding` saja.
Gulungan Ajaib bisa memotongnya! Piko meminta huruf dari nomor 0 sampai sebelum nomor 6.
Hasilnya: `Koding`

Lalu Piko ingin mengambil kata `Kancil`. Dia meminta huruf dari nomor 6 sampai akhir.
Hasilnya: `Kancil`

Ini namanya **slicing**!

**Kode Python-nya:**

```python
# main.py
julukan = "KodingKancil"
kata_pertama = julukan[0:6] # Dari indeks 0 sampai sebelum indeks 6
kata_kedua = julukan[6:]   # Dari indeks 6 sampai akhir

# print(f"Dari '{julukan}', Piko mengambil: '{kata_pertama}'")
# print(f"Dari '{julukan}', Piko juga mengambil: '{kata_kedua}'")
```

## Cerita 6: Piko Bermain dengan Mantra String Ajaib (Metode String)

Gulungan Ajaib punya banyak mantra untuk mengubah tampilan pesan tanpa mengubah pesan aslinya!

1.  **Mantra Huruf Besar (`upper()`):**
    Piko punya pesan `halo`. Dengan mantra ini, pesan menjadi `HALO`.
2.  **Mantra Huruf Kecil (`lower()`):**
    Piko punya pesan `PIKO KEREN`. Dengan mantra ini, pesan menjadi `piko keren`.
3.  **Mantra Rapikan Spasi (`strip()`):**
    Piko punya pesan `   banyak spasi   `. Mantra ini menghilangkan spasi di awal dan akhir, menjadi `banyak spasi`.
4.  **Mantra Cari Kata (`find()`):**
    Piko punya pesan `Piko suka koding`. Dia mencari kata `suka`. Gulungan memberitahu, kata `suka` dimulai dari nomor urut 5. Jika tidak ada, gulungan akan bilang -1.
5.  **Mantra Ganti Kata (`replace()`):**
    Piko punya pesan `Piko suka apel`. Dia ingin mengganti `apel` dengan `pisang`. Gulungan mengubahnya menjadi `Piko suka pisang`.

**Kode Python-nya:**

```python
# main.py
pesan_awal = "  Piko si Kancil Cerdik!  "
# print(f"Pesan awal: '{pesan_awal}'")

# Mantra Huruf Besar
pesan_besar = pesan_awal.upper()
# print(f"Pesan jadi besar semua: '{pesan_besar}'")

# Mantra Huruf Kecil
pesan_kecil = pesan_awal.lower()
# print(f"Pesan jadi kecil semua: '{pesan_kecil}'")

# Mantra Rapikan Spasi
pesan_rapi = pesan_awal.strip()
# print(f"Pesan dirapikan spasinya: '{pesan_rapi}'")

# Mantra Cari Kata
posisi_kancil = pesan_rapi.find("Kancil")
# print(f"Kata 'Kancil' ditemukan di posisi: {posisi_kancil}")
posisi_buaya = pesan_rapi.find("Buaya") # Buaya tidak ada di pesan
# print(f"Kata 'Buaya' ditemukan di posisi: {posisi_buaya}") # Akan -1

# Mantra Ganti Kata
pesan_diganti = pesan_rapi.replace("Cerdik", "Pintar")
# print(f"Pesan setelah diganti: '{pesan_diganti}'")
```

## Uh-Oh! Momen Kesalahan dengan Gulungan Pesan

1.  **Salah Ambil Huruf (IndexError):**
    Piko punya nama `Piko` (panjangnya 4, indeks dari 0 sampai 3). Jika dia mencoba mengambil huruf ke-4 (`nama[4]`), Gulungan Ajaib akan bingung! "Tidak ada huruf di nomor itu!"
    *   **Pesan Error di Python:** `IndexError: string index out of range`
    *   **Piko berkata:** "Ups! Aku salah hitung nomor hurufnya!"

2.  **Salah Mantra (TypeError atau AttributeError):**
    Jika Piko mencoba menggunakan mantra angka (misalnya, tambah `+ 5`) pada pesan huruf, atau menggunakan mantra yang tidak ada untuk string.
    *   **Contoh:** `nama_piko + 5` (mencoba menambah string dengan angka)
    *   **Pesan Error di Python:** `TypeError: can only concatenate str (not "int") to str`
    *   **Piko berkata:** "Oh, mantra ini sepertinya bukan untuk pesan huruf!"

Piko sekarang tahu banyak tentang string, si pesan ajaib! Dia bisa menulis, menggabung, menghitung, memotong, dan mengubahnya dengan berbagai mantra. Petualangan Piko dengan koding jadi makin seru! Sampai jumpa di cerita berikutnya!
