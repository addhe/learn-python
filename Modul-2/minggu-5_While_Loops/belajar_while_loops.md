# Petualangan di Kerajaan Kode: `while` Loop, si Mesin Pengulang Tak Kenal Lelah!

Hai Jagoan Cilik! Piko si Koding Kancil kembali dengan semangat baru! Minggu lalu kita sudah bermain dengan Mesin Pengulang Terhitung (`for` loop). Hari ini, kita akan belajar tentang saudaranya yang tak kalah hebat: **`while` loop**, si Mesin Pengulang Tak Kenal Lelah di Kerajaan Kode Python!

## Apa itu `while` Loop, si Mesin Pengulang Tak Kenal Lelah?

Bayangkan Piko sedang sangat lapar dan di depannya ada setumpuk kue ajaib yang bisa muncul lagi. Piko akan terus makan kue *selama* Piko masih lapar. Begitu Piko kenyang, Piko akan berhenti makan.

Nah, **`while` loop** (dibaca: "wail lup") bekerja persis seperti itu! Dia akan terus melakukan serangkaian perintah *selama* (atau *while*) sebuah kondisi tertentu masih **Benar** (`True`). Begitu kondisi itu menjadi **Salah** (`False`), mesinnya akan berhenti.

Berbeda dengan `for` loop yang biasanya kita tahu berapa kali dia akan mengulang (misalnya, sebanyak item di daftar), `while` loop bisa mengulang berapa kali pun, bahkan bisa tidak mengulang sama sekali jika kondisinya dari awal sudah `False`, atau bisa juga mengulang selamanya jika kondisinya tidak pernah menjadi `False` (ini bahaya, nanti Piko ceritakan!).

Cara menggunakannya:
`while kondisi_yang_diperiksa:`
    `# Lakukan perintah-perintah ini berulang kali`
    `# Penting! Harus ada sesuatu di sini yang bisa membuat kondisi_yang_diperiksa menjadi False suatu saat nanti!`

*   `while`: Kata sihir untuk memulai mesin pengulang tak kenal lelah.
*   `kondisi_yang_diperiksa`: Ini adalah sebuah pertanyaan (seperti di `if`) yang hasilnya `True` atau `False`. Mesin akan terus berjalan selama hasilnya `True`.
*   Jangan lupa tanda titik dua `:` di akhir dan beri indentasi (menjorok ke dalam) untuk perintah-perintah yang mau diulang.

## Contoh 1: Piko Menghitung Mundur Roket

Piko mau meluncurkan roket mainannya. Piko mau hitung mundur dari 5 sampai 1.

```python
hitungan_mundur = 5
print("Bersiap untuk peluncuran roket Piko!")

while hitungan_mundur > 0: # Selama hitungan_mundur masih lebih besar dari 0
    print(f"{hitungan_mundur}...")
    hitungan_mundur = hitungan_mundur - 1 # Ini penting! Mengurangi hitungan agar suatu saat jadi 0 atau kurang

print("MELUNCUR! Roket Piko terbang tinggi!")
```
Di sini, `hitungan_mundur = hitungan_mundur - 1` sangat krusial! Tanpa ini, `hitungan_mundur` akan selalu 5, dan loop akan berjalan selamanya mencetak "5..."! Kita harus memastikan kondisi `while` bisa berubah menjadi `False`.

## Contoh 2: Piko Menebak Angka Rahasia

Piko punya angka rahasia antara 1 dan 10. Kamu harus menebaknya!

```python
import random # Kita butuh ini untuk angka acak

angka_rahasia_piko = random.randint(1, 10) # Piko memilih angka acak antara 1 dan 10
tebakan_kamu = 0 # Kita mulai dengan tebakan yang pasti salah

print("\nPiko punya angka rahasia antara 1 dan 10. Coba tebak!")

while tebakan_kamu != angka_rahasia_piko: # Selama tebakanmu belum sama dengan angka rahasia Piko
    tebakan_str = input("Masukkan tebakanmu (angka 1-10): ")
    tebakan_kamu = int(tebakan_str) # Ubah input teks jadi angka

    if tebakan_kamu < angka_rahasia_piko:
        print("Terlalu kecil, Jagoan! Coba lagi yang lebih besar.")
    elif tebakan_kamu > angka_rahasia_piko:
        print("Terlalu besar, Jagoan! Coba lagi yang lebih kecil.")
    # Jika tebakan_kamu == angka_rahasia_piko, kondisi while akan jadi False, dan loop berhenti

print(f"Hore! Kamu benar! Angka rahasia Piko adalah {angka_rahasia_piko}. Kamu hebat!")
```
Di sini, loop akan terus berjalan meminta input sampai tebakanmu benar. Saat tebakan benar, kondisi `tebakan_kamu != angka_rahasia_piko` menjadi `False`.

## Mantra Tambahan: `break` dan `continue`

Di dalam `while` loop (dan juga `for` loop), ada dua mantra tambahan:
*   **`break` (Mantra Berhenti Paksa)**: Jika Piko mengucapkan `break` di dalam loop, mesin pengulang akan langsung berhenti saat itu juga, tidak peduli kondisi `while`-nya masih `True` atau tidak.
*   **`continue` (Mantra Lewati Putaran Ini)**: Jika Piko mengucapkan `continue`, mesin akan langsung melompati sisa perintah di putaran saat ini dan langsung kembali ke atas untuk memeriksa kondisi `while` lagi.

**Contoh dengan `break`:**
```python
angka = 0
print("\nPiko menghitung, tapi akan berhenti jika angka mencapai 3:")
while angka < 10:
    print(angka)
    if angka == 3:
        print("Piko bilang: Cukup sampai di sini! (break)")
        break # Langsung keluar dari loop
    angka += 1
```

## "Uh-Oh!" dari Piko: Bahaya Loop Tak Terhingga!

Ini adalah "Uh-Oh!" paling berbahaya dari `while` loop: **Loop Tak Terhingga (Infinite Loop)**!
Ini terjadi jika kondisi `while` tidak pernah menjadi `False`. Mesin akan terus berjalan, programmu akan macet, dan Piko akan lari di treadmill selamanya!

```python
# BAHAYA! JANGAN JALANKAN INI TANPA HATI-HATI!
# angka_bahaya = 0
# while angka_bahaya < 5:
#     print("Piko terjebak! Tolong!")
#     # Lupa mengubah angka_bahaya, jadi angka_bahaya < 5 akan selalu True!
#     # Untuk menghentikannya jika tidak sengaja dijalankan, biasanya tekan Ctrl+C di terminal.
```
**Selalu pastikan ada sesuatu di dalam `while` loop-mu yang akan mengubah kondisi agar suatu saat bisa menjadi `False`!**

Kesalahan umum lainnya mirip dengan `for` loop:
*   **Lupa Titik Dua (`SyntaxError`)**: Setelah `while kondisi:`, jangan lupa `:`.
*   **Salah Menjorok (`IndentationError`)**: Perintah di dalam `while` harus menjorok.

**Singkatnya dari Piko:**

*   **`while` loop** adalah Mesin Pengulang Tak Kenal Lelah yang akan terus bekerja *selama* kondisinya `True`.
*   **SANGAT PENTING**: Pastikan ada cara agar kondisi `while` bisa menjadi `False` untuk menghindari **loop tak terhingga**!
*   `break` bisa digunakan untuk keluar dari loop secara paksa.
*   `continue` bisa digunakan untuk melompati sisa putaran saat ini dan lanjut ke putaran berikutnya.

Kamu luar biasa, Jagoan Cilik! Dengan `while` loop, kamu bisa membuat program yang lebih dinamis dan interaktif. Ingat pesan Piko tentang loop tak terhingga ya! Sampai jumpa di petualangan berikutnya!
