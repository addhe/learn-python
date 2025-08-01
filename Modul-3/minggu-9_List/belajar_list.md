# 🧺 Piko si Koding Kancil dan Kantong Ajaib Serbaguna (List di Python)

Setelah menaklukkan Gulungan Pesan Ajaib (String), Piko si Kancil Cerdik melanjutkan penjelajahannya. Di tengah hutan koding, dia menemukan benda unik berbentuk kantong yang memancarkan cahaya biru lembut. “Wah, apa ini?” gumamnya. Gulungan Ajaib menjawab, “Itulah Kantong Serbaguna! Kamu bisa menyimpan banyak benda, bahkan yang berbeda jenis!”

Di dunia Python, kantong ini disebut **List**—penyimpanan berurutan yang bisa diisi, dibuka, ditambah, diubah, bahkan dikocok!

## 🍎 Cerita 1: Isi Kantong Si Kancil

Piko mulai bereksperimen. Ia memasukkan buah-buahan favoritnya:

```python
bekal_buah_piko = ["apel", "pisang", "jeruk"]
```

Lalu ia membuat kantong mainan:

```python
mainan_piko = ["bola", "yoyo"]
```

Dan kantong campuran penuh kejutan:

```python
kantong_campuran = ["Bobi si Beruang", 5, "Lala si Kelinci", 4]
```

Kantong bisa berisi apa saja! Bahkan kosong pun boleh:

```python
kantong_kosong = []
```

## 🔍 Cerita 2: Menyentuh Isi Kantong (Indexing)

Piko penasaran dengan buah pertama di kantongnya...

```python
buah_pertama = bekal_buah_piko[0]    # "apel"
buah_terakhir = bekal_buah_piko[-1]  # "jeruk"
```

Dan ia belajar: setiap barang di list punya indeks, dimulai dari 0, dan bisa diakses dari belakang juga!

## ➕ Cerita 3: Menambah Barang ke Kantong

Piko menemukan buah baru dan ingin menambahkannya:

```python
bekal_buah_piko.append("mangga")
bekal_buah_piko.insert(1, "anggur")
```

Kantongnya kini berbunyi: `["apel", "anggur", "pisang", "jeruk", "mangga"]`

## ➖ Cerita 4: Mengeluarkan Barang dari Kantong

Saat Piko makan pisang, ia ingin menghapusnya:

```python
bekal_buah_piko.remove("pisang")
```

Lalu ia mengeluarkan buah terakhir:

```python
bekal_buah_piko.pop()  # "mangga"
```

Dan bahkan bisa mengambil buah pertama:

```python
bekal_buah_piko.pop(0)  # "apel"
```

## 🔁 Cerita 5: Menyapa Isi Kantong Satu per Satu

Piko menyapa mainan-mainan yang ia bawa:

```python
for mainan in mainan_piko:
    print(f"- Piko bermain dengan {mainan}")
```

Loop sihir pun menampilkan semuanya satu per satu!

## 🪄 Cerita 6: Mantra Ajaib dari Kantong

Piko belajar mantra baru:

| Mantra        | Fungsi                            | Contoh Kode                                |
|---------------|-----------------------------------|---------------------------------------------|
| `len()`       | Hitung jumlah isi kantong         | `len(bekal_buah_piko)`                      |
| `index(x)`    | Cari posisi suatu barang          | `bekal_buah_piko.index("jeruk")`           |
| `count(x)`    | Hitung jumlah barang tertentu     | `kantong_apel.count("apel")`               |
| `sort()`      | Urutkan isi kantong               | `buah_acak.sort()`                          |
| `sorted(x)`   | Buat versi terurut (asli tetap)   | `sorted(buah_acak)`                         |
| `reverse()`   | Balik urutan kantong              | `buah_acak.reverse()`                       |

Semua bisa digunakan dengan mudah—asal tahu mantra dan jangan salah sebut!

## ⚠️ Uh-Oh! Kesalahan yang Bisa Terjadi

💥 Piko mencoba mengambil barang yang tidak ada:

```python
bekal_buah_piko[10]
# IndexError: list index out of range
```

💥 Piko mencoba menghapus buah yang tak ada:

```python
bekal_buah_piko.remove("semangka")
# ValueError: list.remove(x): x not in list
```

Gulungan pun berbisik, “Kancil cerdik, lihat dulu isi kantong sebelum mengambil atau membuang!”

Piko semakin kagum dengan dunia koding. List membuat petualangan lebih terorganisir, seperti kantong Doraemon penuh alat ajaib!