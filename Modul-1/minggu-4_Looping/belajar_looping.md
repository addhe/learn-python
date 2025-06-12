# Petualangan di Kerajaan Kode: Mesin Pengulang Ajaib (Looping)!

Hai Jagoan Cilik! Piko si Koding Kancil sudah tidak sabar untuk petualangan kita hari ini! Setelah kita belajar tentang Gerbang Ajaib Penentu Jalan (Kondisional), sekarang kita akan berkenalan dengan **Looping**, si Mesin Pengulang Ajaib di Kerajaan Kode Python! Dengan mesin ini, kita bisa melakukan banyak hal berulang kali dengan mudah!

## Apa itu Mesin Pengulang Ajaib (Looping)?

Bayangkan Piko punya setumpuk surat undangan pesta yang harus Piko tulis satu per satu untuk semua teman Piko. Ada 10 teman! Wah, kalau Piko tulis manual satu-satu, bisa pegal tangannya.

Nah, di Kerajaan Kode Python, **looping** (atau perulangan) itu seperti mesin ajaib yang bisa membantu Piko melakukan pekerjaan yang sama berulang-ulang secara otomatis. Piko tinggal bilang ke mesinnya, "Tolong tulis undangan ini untuk setiap teman di daftarku!" dan mesin itu akan melakukannya sampai selesai!

Ada dua jenis mesin pengulang utama yang sering Piko gunakan:
1.  **Mesin Pengulang Terhitung (`for` loop):** Untuk mengulang sesuatu sebanyak jumlah yang sudah kita tahu pasti, misalnya untuk setiap teman di daftar Piko, atau menghitung dari 1 sampai 10.
2.  **Mesin Pengulang Bersyarat (`while` loop):** Untuk mengulang sesuatu *selama* sebuah kondisi masih benar. Misalnya, Piko akan terus makan kue *selama* masih ada kue di piring. (Mesin `while` ini akan kita pelajari lebih dalam di minggu depan ya!)

Hari ini, kita fokus dulu ke **Mesin Pengulang Terhitung (`for` loop)**!

## Mesin Pengulang Terhitung (`for` loop)

Mesin `for` ini sangat pintar! Dia bisa mengambil satu per satu item dari sebuah daftar (atau urutan) dan melakukan sesuatu dengan item tersebut.

Cara menggunakannya:
`for item_saat_ini in daftar_item:`
    `# Lakukan sesuatu dengan item_saat_ini`

*   `for`: Kata sihir untuk memulai mesin pengulang terhitung.
*   `item_saat_ini`: Ini adalah Kotak Ajaib (variabel) sementara yang akan menyimpan item yang sedang dipegang oleh mesin dari `daftar_item`.
*   `in`: Kata sihir yang berarti "di dalam".
*   `daftar_item`: Ini bisa berupa daftar nama teman, daftar angka, atau bahkan huruf-huruf dalam sebuah kata!
*   Jangan lupa tanda titik dua `:` di akhir dan beri indentasi (menjorok ke dalam) untuk perintah-perintah yang mau diulang.

**Contoh 1: Piko Menyapa Teman-Temannya**

```python
daftar_teman_piko = ["Kura-kura Cepat", "Kelinci Bijak", "Monyet Ceria"]

print("Piko akan menyapa teman-temannya satu per satu:")
for teman in daftar_teman_piko:
    print(f"Halo, {teman}! Selamat datang di pestaku!")

print("Semua teman sudah Piko sapa!")
```
Mesin `for` akan mengambil nama "Kura-kura Cepat", menyapanya. Lalu mengambil "Kelinci Bijak", menyapanya. Terakhir "Monyet Ceria", dan menyapanya.

**Contoh 2: Piko Menghitung Harta Karun dengan `range()`**

Kadang kita mau mengulang sesuatu beberapa kali tanpa punya daftar khusus. Kita bisa pakai mantra `range()`!
*   `range(5)` akan memberi kita urutan angka dari 0 sampai 4 (total 5 angka: 0, 1, 2, 3, 4).
*   `range(1, 6)` akan memberi kita urutan angka dari 1 sampai 5 (total 5 angka: 1, 2, 3, 4, 5).

```python
print("\nPiko menghitung sampai 5:")
for angka in range(5):
    print(f"Hitungan ke-{angka}")

print("\nPiko menghitung dari 1 sampai 3 untuk roketnya:")
for hitungan_mundur in range(1, 4):
    print(f"{hitungan_mundur}...")
print("MELUNCUR!")
```

## "Uh-Oh!" dari Piko Saat Menggunakan Mesin Pengulang

Mesin Pengulang ini hebat, tapi kadang kita bisa salah menggunakannya dan bertemu "Uh-Oh!" (error).

1.  **Lupa Titik Dua (`SyntaxError`)**:
    Seperti biasa, setelah baris `for nama_item in daftar_item:`, jangan lupa tanda titik dua `:`!
    ```python
    # for teman in daftar_teman_piko # Uh-Oh! Lupa titik dua!
    #     print(teman)
    ```
    Piko bilang: "Aduh, mantra `for` nya kurang lengkap! Butuh `:` di akhir barisnya!"

2.  **Salah Menjorok (`IndentationError`)**:
    Perintah yang mau diulang di dalam `for` harus ditulis sedikit menjorok ke dalam.
    ```python
    # for angka in range(3):
    # print(angka) # Uh-Oh! Harus menjorok!
    ```
    Piko bilang: "Perintah untuk mesin pengulangnya harus masuk sedikit ke kanan ya, biar Python tahu itu bagian dari pengulangan!"

3.  **Loop Tak Terhingga (Lebih sering di `while` loop, tapi hati-hati!)**:
    Kalau kita membuat mesin yang syarat berhentinya tidak pernah tercapai, dia akan terus berjalan selamanya! Ini seperti Piko lari di treadmill yang tidak bisa berhenti. (Ini akan lebih kita bahas di `while` loop).

4.  **Menggunakan Variabel yang Salah di Dalam Loop (`NameError` atau Logika Salah)**:
    Pastikan kamu menggunakan nama variabel yang benar di dalam loop, yaitu variabel yang kamu definisikan di baris `for` (seperti `teman` atau `angka` di contoh Piko).
    ```python
    # buah_buahan = ["apel", "pisang", "mangga"]
    # for buah_enak in buah_buahan:
    #     print(buah) # Uh-Oh! Seharusnya `print(buah_enak)`
    ```
    Piko bilang: "Variabel `buah` tidak Piko kenali di sini. Mungkin maksudmu `buah_enak`?"

**Singkatnya dari Piko:**

*   **Looping (`for` loop)** adalah Mesin Pengulang Ajaib untuk melakukan tugas yang sama berkali-kali secara otomatis.
*   Gunakan `for item in daftar:` untuk mengulang untuk setiap item dalam sebuah daftar.
*   Gunakan `range(jumlah)` untuk mengulang beberapa kali.
*   Selalu ingat `:` di akhir baris `for` dan indentasi yang benar untuk perintah di dalamnya.
*   Hati-hati dengan nama variabel yang kamu gunakan di dalam loop!

Kamu makin pintar saja, Jagoan Cilik! Dengan Mesin Pengulang Ajaib ini, kamu bisa membuat program yang jauh lebih kuat dan efisien. Sampai jumpa di petualangan mantra `while` loop minggu depan!
