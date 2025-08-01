# 🌟 Piko si Koding Kancil dan Gulungan Pesan Ajaib: Kisah tentang String Python

Suatu hari, di kedalaman gua yang sunyi, Piko si Kancil Penjelajah Kode menemukan sebuah gulungan perkamen (lembaran tipis yang terbuat dari kulit hewan, biasanya domba, kambing, atau anak sapi, yang telah diproses dan disiapkan untuk dijadikan media tulis) yang bersinar lembut. "Apa ini?" gumamnya. Ternyata gulungan itu memiliki sihir khusus—mampu mengubah kata-kata menjadi mantra kode!

Di dunia pemrograman, sihir semacam ini dikenal sebagai **string**—untaian huruf, angka, dan simbol yang membentuk pesan.

## 📝 Cerita 1: Pesan Awal dari Gulungan Ajaib

"Gulungan Ajaib, tuliskan namaku!" seru Piko.  
✨ Dan muncullah tulisan: `Piko`

Lalu ia berkata, "Beri salam untuk teman-temanku!"  
✨ Gulungan menjawab: `Halo Kawan!`

Piko pun belajar: cukup menulis pesan di antara tanda kutip untuk membuat string!

```python
nama_piko = "Piko"
salam = 'Halo Kawan!'
```

## 🔗 Cerita 2: Merangkai Mantra

Piko mencoba menggabungkan dua potong kalimat: `Aku Suka` dan `Apel Merah`.

Namun gulungan menampilkan: `Aku SukaApel Merah`  
"Hmm, kok dempet gitu ya?" pikir Piko.

Akhirnya ia menambahkan spasi di akhir kalimat pertama, dan gulungan pun menampilkan: `Aku Suka Apel Merah`

```python
pesan1 = "Aku Suka "
pesan2 = "Apel Merah"
pesan_lengkap = pesan1 + pesan2
```

## 📏 Cerita 3: Mengukur Panjang Pesan

Piko bertanya, "Berapa panjang pesan 'Piko'?"  
Gulungan menjawab: `4 huruf`

Untuk pesan `Halo Kawan!`, panjangnya adalah `11 karakter`, termasuk spasi dan tanda seru.

```python
len("Piko")          # Hasil: 4
len("Halo Kawan!")   # Hasil: 11
```

## 🔍 Cerita 4: Membaca Karakter Satu per Satu

Piko penasaran akan huruf-huruf dalam namanya.

```python
nama = "Piko"
print(nama[0])  # Output: 'P'
print(nama[2])  # Output: 'k'
```

Setiap karakter punya nomor urut:  
`P` di indeks 0, `i` di 1, `k` di 2, `o` di 3.

## ✂️ Cerita 5: Memotong Pesan (Slicing)

Pesan `KodingKancil` ingin dipisah:  
- Huruf 0–5: `Koding`  
- Huruf 6 hingga akhir: `Kancil`

```python
julukan = "KodingKancil"
kata_pertama = julukan[:6]    # Koding
kata_kedua = julukan[6:]      # Kancil
```

## 🧙‍♂️ Cerita 6: Mantra-String Ajaib

Piko menemukan mantra yang bisa mengubah tampilan pesan:

- `.upper()` → mengubah ke huruf besar
- `.lower()` → mengubah ke huruf kecil
- `.strip()` → menghilangkan spasi
- `.find()` → mencari posisi kata
- `.replace()` → mengganti kata

```python
pesan = "  Piko si Kancil Cerdik!  "
pesan.upper()       # '  PIKO SI KANCIL CERDIK!  '
pesan.lower()       # '  piko si kancil cerdik!  '
pesan.strip()       # 'Piko si Kancil Cerdik!'
pesan.find("Kancil")# Hasil: posisi index
pesan.replace("Cerdik", "Pintar")  # Ganti kata
```

## ⚠️ Cerita Bonus: Kesalahan Kecil yang Bisa Terjadi

- **IndexError:** Piko memanggil huruf ke-4 dari `Piko` padahal indeksnya hanya sampai 3.
- **TypeError:** Piko mencoba menambahkan angka ke string (contoh: `"Piko" + 5`)

Gulungan pun berkata, "Ups, mantra yang kau pakai belum tepat!"