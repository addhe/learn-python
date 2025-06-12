# Petualangan di Kerajaan Kode: Mantra Pemanggil Ajaib (Fungsi)!

Halo lagi, Jagoan Cilik! Piko si Koding Kancil kembali! Setelah kita bermain dengan Kotak Ajaib (Variabel) dan Tongkat Pengubah (Ekspresi), hari ini kita akan belajar mantra yang super kuat dan berguna di Kerajaan Kode Python: **Fungsi**, si Mantra Pemanggil Ajaib!

## Apa itu Mantra Pemanggil Ajaib (Fungsi)?

Bayangkan kamu punya sebuah buku resep ajaib. Di dalam buku itu, ada banyak resep untuk membuat hal-hal keren. Misalnya, ada "Resep Kue Pelangi Kilat", "Resep Ramuan Lompat Tinggi", atau "Resep Nyanyian Pagi Ceria".

Nah, di Kerajaan Kode Python, **fungsi** itu persis seperti resep ajaib itu!
Kamu menulis resepnya sekali saja (ini namanya **mendefinisikan fungsi**). Di dalam resep itu, kamu tulis langkah-langkah apa saja yang harus dilakukan.

Setelah resepnya jadi, setiap kali kamu butuh Kue Pelangi Kilat, kamu tidak perlu repot-repot menulis ulang semua langkahnya. Kamu tinggal bilang, "Piko, tolong buatkan Kue Pelangi Kilat!" (ini namanya **memanggil fungsi**). Praktis, kan?

Dengan fungsi, pekerjaan yang sama bisa kita lakukan berkali-kali tanpa capek menulis ulang mantranya!

## Menulis Resep Ajaib (Mendefinisikan Fungsi)

Untuk menulis resep ajaib (fungsi) di buku mantra Python kita, ada beberapa aturan:
1.  Kita mulai dengan kata sihir `def` (singkatan dari *define*, artinya menentukan atau membuat).
2.  Setelah `def`, kita tulis nama resep kita. Nama ini harus unik dan mudah diingat, misalnya `buat_kue_pelangi` atau `sapa_teman_ajaib`.
3.  Setelah nama resep, kita tambahkan tanda kurung `()`. Di dalam kurung ini, kadang kita bisa masukkan "bahan-bahan khusus" yang dibutuhkan resep. Bahan-bahan ini disebut **parameter**.
4.  Baris pertama resep diakhiri dengan tanda titik dua `:`.
5.  Langkah-langkah detail resepnya ditulis di baris-baris berikutnya. Penting! Setiap langkah harus ditulis sedikit menjorok ke dalam (ini namanya **indentasi**). Ini memberitahu Python bahwa langkah-langkah tersebut adalah bagian dari resep itu.

Yuk, kita coba buat resep sederhana untuk menyapa teman:

```python
def sapa_teman_ajaib(nama_teman):
    pesan_salam = "Hore, " + nama_teman + "! Selamat berpetualang di Kerajaan Kode hari ini!"
    print(pesan_salam)
```

Lihat? Resep kita bernama `sapa_teman_ajaib`. Dia butuh satu bahan khusus (parameter) yaitu `nama_teman`. Langkah resepnya adalah membuat `pesan_salam` lalu mencetaknya.

## Menggunakan Resep Ajaib (Memanggil Fungsi)

Setelah resep `sapa_teman_ajaib` kita tulis di buku mantra, kita bisa langsung menggunakannya! Caranya gampang:
Cukup tulis nama resepnya, diikuti tanda kurung `()`. Kalau resepnya butuh bahan (seperti `nama_teman` tadi), kita masukkan bahannya di dalam kurung. Bahan yang kita masukkan saat memanggil ini disebut **argumen**.

```python
sapa_teman_ajaib("Jagoan Cilik Pemberani") # Memanggil resep dengan bahan "Jagoan Cilik Pemberani"
sapa_teman_ajaib("Piko si Kancil Cerdik")  # Memanggil resep untuk Piko
```
Setiap kali kita panggil, langkah-langkah di dalam resep `sapa_teman_ajaib` akan dijalankan!

## Resep yang Memberikan Hasil (Fungsi dengan `return`)

Beberapa resep tidak hanya melakukan sesuatu (seperti mencetak salam), tapi juga bisa memberikan kita hasil jadi. Misalnya, resep jus buah akan menghasilkan segelas jus yang bisa kita minum.

Di Python, fungsi bisa "mengembalikan" sebuah hasil menggunakan kata sihir `return`.

Contoh, kita buat resep untuk menggandakan angka:
```python
def gandakan_angka_ajaib(angka):
    hasil_ganda = angka * 2
    return hasil_ganda # Ini dia! Resepnya mengembalikan hasil_ganda
```

Saat kita panggil resep ini, kita bisa simpan hasilnya di Kotak Ajaib (variabel):
```python
angka_rahasia = 7
hasil_resep_ganda = gandakan_angka_ajaib(angka_rahasia) # Hasilnya (14) disimpan di sini
print("Angka rahasiaku adalah", angka_rahasia)
print("Setelah digandakan oleh resep ajaib, jadi:", hasil_resep_ganda)
```
Keren! `hasil_resep_ganda` sekarang berisi angka 14.

## Jangan Takut Sama "Uh-Oh!" Saat Memakai Mantra Pemanggil!

Saat kita asyik membuat dan memanggil mantra (fungsi), kadang ada "Uh-Oh!" (error) yang muncul. Tapi ingat kata Piko, jangan takut! "Uh-Oh!" itu teman yang memberitahu kita kalau ada yang keliru.

*   **Salah Panggil Nama Mantra (`NameError`)**:
    Kalau kita panggil nama resep yang tidak ada di buku mantra.
    ```python
    # sapa_teman_ajaib("Piko") # Ini benar
    # sapa_teman_ajaiib("Piko") # Uh-Oh! NameError: name 'sapa_teman_ajaiib' is not defined
    ```
    Piko bilang: "Ups, sepertinya mantra `sapa_teman_ajaiib` belum pernah kita tulis atau salah ketik namanya!"

*   **Bahan Kurang atau Lebih (`TypeError`)**:
    Kalau resepnya butuh 1 bahan, tapi kita kasih 2, atau tidak kita kasih sama sekali.
    ```python
    def butuh_satu_bahan_saja(bahan):
        print("Bahan yang kuterima:", bahan)

    # butuh_satu_bahan_saja() # Uh-Oh! TypeError: butuh_satu_bahan_saja() missing 1 required positional argument: 'bahan'
    # butuh_satu_bahan_saja("apel", "pisang") # Uh-Oh! TypeError: butuh_satu_bahan_saja() takes 1 positional argument but 2 were given
    ```
    Piko bilang: "Resep ini butuh tepat satu bahan, tidak kurang, tidak lebih!"

*   **Lupa Tanda Kurung `()` Saat Memanggil**:
    Kalau kita panggil nama resep tanpa `()`.
    ```python
    # print(sapa_teman_ajaib)
    ```
    Piko bilang: "Hei, ini tidak menjalankan resepnya, tapi malah memberitahu kita tentang resep itu sendiri (seperti melihat sampul bukunya saja). Untuk menjalankan isi resep, jangan lupa tambahkan `()` di akhir nama resepnya ya, misalnya `sapa_teman_ajaib('teman')`!"

*   **Salah Menulis Resep (`IndentationError`)**:
    Saat menulis resep (mendefinisikan fungsi), langkah-langkahnya harus menjorok ke dalam dengan benar.
    ```python
    # def resep_salah_tulis(nama):
    # print("Halo", nama) # Uh-Oh! IndentationError: expected an indented block after function definition
    ```
    Piko bilang: "Aduh! Langkah-langkah resepnya harus ditulis sedikit ke kanan (menjorok) setelah baris `def` ya, biar Python tahu itu bagian dari resep!"

**Singkatnya dari Piko:**

*   **Fungsi** (Mantra Pemanggil Ajaib) itu seperti resep di buku mantra: tulis sekali, gunakan berkali-kali!
*   Kita **definisikan** fungsi (tulis resep) dengan `def nama_fungsi(parameter):`. Ingat indentasi untuk langkah-langkahnya!
*   Kita **panggil** fungsi (gunakan resep) dengan `nama_fungsi(argumen)`.
*   Fungsi bisa `return` (memberikan) hasil yang bisa kita simpan.
*   "Uh-Oh!" (Error) saat pakai fungsi itu biasa, dia teman yang membantu kita belajar!

Kamu makin hebat, Jagoan Cilik! Dengan Mantra Pemanggil Ajaib ini, petualanganmu di Kerajaan Kode Python akan semakin seru dan efisien! Sampai jumpa di pelajaran mantra berikutnya!
