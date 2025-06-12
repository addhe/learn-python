# Petualangan di Kerajaan Kode: `for` Loop, si Penjelajah Koleksi Ajaib! (Lanjutan)

Hai Jagoan Cilik! Piko si Koding Kancil kembali lagi! Ingatkah kamu dengan **`for` loop**, si Mesin Pengulang Terhitung yang kita temui di Modul 1? Dia adalah penjelajah ulung yang bisa mengunjungi setiap item dalam sebuah daftar. Hari ini, kita akan melihat petualangan `for` loop yang lebih seru lagi, menjelajahi berbagai jenis koleksi harta karun dan menggunakan peta ajaib!

## Mengingat Kembali `for` Loop si Penjelajah

Sebelumnya, kita tahu `for` loop bisa seperti ini:

```python
daftar_buah = ["apel", "pisang", "mangga"]
for buah in daftar_buah:
    print(f"Piko menemukan buah: {buah}")
```
Dan juga dengan `range()` untuk menghitung:
```python
for angka in range(1, 4):
    print(f"Hitungan ke-{angka}")
```
Sekarang, ayo kita lihat kemampuan lainnya!

## 1. Menjelajahi Berbagai Jenis Harta Karun (Iterables)

`for` loop tidak hanya bisa menjelajahi daftar (`list`), tapi juga banyak jenis koleksi lainnya!

**a. Menjelajahi Kata Ajaib (String)**
Setiap huruf dalam sebuah kata bisa dijelajahi!

```python
kata_rahasia = "PYTHON"
print(f"\nPiko mengeja kata rahasia: {kata_rahasia}")
for huruf in kata_rahasia:
    print(f"Huruf yang ditemukan: {huruf}")
```

**b. Menjelajahi Koleksi Abadi (Tuple)**
Tuple itu seperti daftar, tapi isinya tidak bisa diubah setelah dibuat. `for` loop tetap bisa menjelajahinya!

```python
koordinat_harta = (10, 25, "Gua Kristal") # Ini tuple
print(f"\nPiko memeriksa koordinat harta: {koordinat_harta}")
for info in koordinat_harta:
    print(f"Info koordinat: {info}")
```

**c. Menjelajahi Peti Harta Karun Bernama (Dictionary)**
Dictionary menyimpan pasangan kunci dan nilai, seperti nama barang dan jumlahnya di peti harta karun. `for` loop punya beberapa cara untuk menjelajahinya:

*   **Mengambil Kunci-Kuncinya Saja:**
    ```python
    isi_peti_piko = {"koin emas": 50, "permata biru": 5, "peta kuno": 1}
    print("\nIsi peti Piko (kunci saja):")
    for kunci_barang in isi_peti_piko:
        print(f"Ada kunci: {kunci_barang}")
    ```

*   **Mengambil Nilai-Nilainya Saja (dengan `.values()`):**
    ```python
    print("\nIsi peti Piko (nilai saja):")
    for jumlah_barang in isi_peti_piko.values():
        print(f"Ada sejumlah: {jumlah_barang}")
    ```

*   **Mengambil Kunci dan Nilai Bersamaan (dengan `.items()`):** Ini cara paling seru!
    ```python
    print("\nIsi peti Piko (kunci dan nilai):")
    for barang, jumlah in isi_peti_piko.items():
        print(f"Piko punya {jumlah} buah/keping {barang}")
    ```

## 2. Peta Penjelajahan dengan Nomor Urut (`enumerate`)

Kadang saat menjelajah daftar, Piko ingin tahu ini item keberapa. Mantra `enumerate` membantu kita mendapatkan nomor urut (indeks) sekaligus itemnya!

```python
teman_baik_piko = ["Kura Cepat", "Kelinci Bijak", "Monyet Ceria"]
print("\nDaftar teman baik Piko dengan nomor urut:")
for nomor, nama_teman in enumerate(teman_baik_piko):
    print(f"Teman ke-{nomor + 1} (indeks {nomor}): {nama_teman}")
# Kita tambahkan nomor + 1 agar hitungannya mulai dari 1 untuk manusia, tapi indeks aslinya mulai dari 0
```

## 3. Petualangan di Dalam Petualangan (Nested `for` Loops)

Wow! `for` loop bisa ada di dalam `for` loop lain! Ini namanya **nested loop** atau loop bersarang. Bayangkan Piko menjelajahi beberapa gua, dan di setiap gua ada beberapa peti harta karun.

```python
gua_gua_ajaib = [
    ["peti emas", "peti perak"],      # Isi gua pertama
    ["peti perunggu"],               # Isi gua kedua
    ["peti kayu", "peti besi", "peti kristal"] # Isi gua ketiga
]

print("\nPiko menjelajahi gua-gua ajaib:")
for nomor_gua, isi_gua in enumerate(gua_gua_ajaib):
    print(f"  Masuk ke Gua ke-{nomor_gua + 1}...")
    for nomor_peti, jenis_peti in enumerate(isi_gua):
        print(f"    Piko menemukan {jenis_peti} (peti ke-{nomor_peti+1} di gua ini)")
```
Dengan nested loop, kita bisa membuat pola atau memproses data yang lebih rumit!

## 4. Mantra `break` dan `continue` Tetap Berguna!

Jangan lupa, mantra `break` (untuk berhenti paksa) dan `continue` (untuk melewati putaran ini) yang kita pelajari di `while` loop juga bisa digunakan di dalam `for` loop!

```python
print("\nPiko mencari 'apel' di keranjang, berhenti jika sudah ketemu:")
keranjang_buah = ["jeruk", "pisang", "apel", "mangga", "rambutan"]
for buah_dicari in keranjang_buah:
    print(f"Mencari... sekarang di {buah_dicari}")
    if buah_dicari == "apel":
        print("Ketemu Apel! Piko berhenti mencari.")
        break

print("\nPiko mau mengambil semua buah kecuali 'pisang':")
for buah_diambil in keranjang_buah:
    if buah_diambil == "pisang":
        print("(Oh, ini pisang, Piko lewati dulu dengan continue...)")
        continue
    print(f"Piko mengambil {buah_diambil}")
```

## "Uh-Oh!" dari Piko Saat Penjelajahan Lanjutan

Selain "Uh-Oh!" yang sudah kita kenal (lupa `:`, salah indentasi, salah nama variabel), saat menggunakan fitur lanjutan ini, perhatikan:
*   **Salah Metode Dictionary**: Saat menjelajahi dictionary, pastikan menggunakan `.values()` atau `.items()` jika memang itu yang kamu mau. Jika hanya `for k in my_dict:`, kamu hanya dapat kuncinya.
*   **Kebingungan Indeks `enumerate`**: Ingat `enumerate` memulai indeks dari 0. Jika ingin menampilkannya mulai dari 1, tambahkan 1 saat mencetak.
*   **Kompleksitas Nested Loop**: Nested loop sangat kuat, tapi jika terlalu banyak tingkatannya (loop di dalam loop di dalam loop...), kode bisa jadi sulit dibaca dan lambat. Gunakan dengan bijak ya!

**Singkatnya dari Piko:**

*   `for` loop bisa menjelajahi berbagai tipe data: **string**, **tuple**, **dictionary** (dengan `.keys()`, `.values()`, `.items()`).
*   Gunakan `enumerate(daftar)` untuk mendapatkan **indeks dan item** saat menjelajah.
*   **Nested `for` loops** (loop di dalam loop) berguna untuk data yang lebih kompleks atau membuat pola.
*   Mantra `break` dan `continue` juga ampuh di dalam `for` loop.

Kamu semakin hebat dalam menjelajahi Kerajaan Kode, Jagoan Cilik! Dengan `for` loop yang makin canggih ini, programmu bisa melakukan hal-hal yang lebih menakjubkan lagi! Sampai jumpa di petualangan berikutnya!
