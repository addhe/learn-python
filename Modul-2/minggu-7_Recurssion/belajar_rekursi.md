# Piko si Koding Kancil dan Cermin Ajaib Pengganda Diri (Rekursi)

Selamat datang kembali di petualangan Piko si Koding Kancil! Kali ini, Piko menemukan sebuah cermin ajaib di tengah hutan. Cermin ini bukan cermin biasa, lho! Setiap kali Piko melihat ke cermin itu sambil mengucapkan mantra khusus, cermin itu akan membuat "bayangan Piko" yang bisa melakukan tugas untuknya!

## Cerita 1: Mantra Pengganda Piko untuk Menghitung Apel

Piko menemukan setumpuk apel di bawah pohon. "Wah, banyak sekali apelnya! Bagaimana cara menghitungnya dengan cepat ya?" pikir Piko. Tiba-tiba, ia teringat Cermin Ajaib Pengganda Diri!

Piko berdiri di depan cermin dan mengucapkan mantra: "**Cermin Ajaib, hitung apel ini untukku, mulai dari apel ke-(jumlah)!**"

Begini cara kerja mantra Piko (ini seperti fungsi rekursif):

1.  **Kasus Dasar (Base Case):** Jika hanya ada 1 apel tersisa untuk dihitung oleh "bayangan Piko", bayangan itu akan berkata, "Ini apel terakhir, apel ke-1!" dan berhenti menggandakan diri.
2.  **Langkah Rekursif (Recursive Step):** Jika ada lebih dari 1 apel, "bayangan Piko" akan:
    *   Mengambil satu apel dan berkata, "Aku hitung apel ke-(jumlah saat ini)."
    *   Kemudian, ia akan melihat ke cermin dan menyuruh "bayangan Piko yang baru" untuk menghitung sisa apelnya, "Cermin Ajaib, hitung apel ini untukku, mulai dari apel ke-(jumlah saat ini - 1)!"

Piko yang asli menyuruh bayangan pertamanya menghitung, misalnya, 3 apel.
*   Bayangan Piko pertama (untuk 3 apel): "Aku hitung apel ke-3." Lalu menyuruh bayangan kedua menghitung 2 apel.
*   Bayangan Piko kedua (untuk 2 apel): "Aku hitung apel ke-2." Lalu menyuruh bayangan ketiga menghitung 1 apel.
*   Bayangan Piko ketiga (untuk 1 apel): "Ini apel terakhir, apel ke-1!" Selesai!

Akhirnya, semua apel terhitung mundur dari 3, 2, lalu 1. Piko senang karena semua apel terhitung dengan bantuan bayangan-bayangannya!

**Kode Python-nya:**

```python
# main.py
def hitung_mundur_apel(jumlah_apel):
    # Kasus Dasar: Jika tidak ada apel lagi (atau sudah 0)
    if jumlah_apel <= 0:
        print("Tidak ada apel lagi untuk dihitung!")
        return
    # Kasus Dasar Lain: Jika tinggal satu apel
    if jumlah_apel == 1:
        print(f"Ini apel terakhir, apel ke-1!")
        return
    
    # Langkah Rekursif
    print(f"Bayangan Piko menghitung apel ke-{jumlah_apel}.")
    hitung_mundur_apel(jumlah_apel - 1) # Memanggil dirinya sendiri dengan jumlah lebih kecil

# Piko ingin menghitung 3 apel
# hitung_mundur_apel(3) 
```

## Cerita 2: Mantra Faktorial untuk Mengatur Mainan

Piko punya banyak mainan balok dan ingin menyusunnya dalam berbagai urutan. "Hmm, ada berapa banyak ya cara menyusun 3 balok ini?" Piko bertanya-tanya. Ia ingat Cermin Ajaib bisa membantunya lagi dengan mantra faktorial!

Mantra Faktorial: "**Cermin Ajaib, beri tahu aku berapa banyak cara menyusun (N) balok!**"

*   **Kasus Dasar:** Jika hanya ada 1 balok (atau 0 balok), hanya ada 1 cara menyusunnya. Bayangan Piko akan berkata, "Hanya ada 1 cara."
*   **Langkah Rekursif:** Jika ada N balok, bayangan Piko akan mengambil 1 balok, lalu berkata, "Untuk N balok, ada N dikali (jumlah cara menyusun N-1 balok)." Kemudian ia menyuruh bayangan baru mencari tahu cara menyusun N-1 balok.

Misalnya, untuk 3 balok:
1.  Bayangan Piko (3 balok): "Ada 3 dikali (cara menyusun 2 balok)." Menyuruh bayangan baru.
2.  Bayangan Piko (2 balok): "Ada 2 dikali (cara menyusun 1 balok)." Menyuruh bayangan baru.
3.  Bayangan Piko (1 balok): "Hanya ada 1 cara."

Jadi, hasilnya adalah 3 * 2 * 1 = 6 cara!

**Kode Python-nya:**

```python
# main.py
def faktorial_piko(n):
    # Kasus Dasar
    if n == 0 or n == 1:
        return 1
    # Langkah Rekursif
    else:
        return n * faktorial_piko(n - 1)

# Piko ingin tahu berapa cara menyusun 3 balok
# jumlah_cara = faktorial_piko(3)
# print(f"Piko bisa menyusun 3 balok dengan {jumlah_cara} cara berbeda!")
```

## Uh-Oh! Momen Kesalahan dengan Cermin Ajaib

Piko harus hati-hati dengan Cermin Ajaib. Jika mantranya salah, bisa-bisa cerminnya terus membuat bayangan tanpa henti!

1.  **Tidak Ada Mantra Berhenti (Missing Base Case):**
    Bayangkan Piko menyuruh cermin menghitung apel, tapi lupa memberitahu kapan harus berhenti (lupa kasus dasar saat apel tinggal 1 atau habis). Cermin akan terus membuat bayangan Piko baru, yang menyuruh bayangan Piko baru lagi, dan seterusnya, sampai ruangannya penuh dengan bayangan Piko dan komputernya kelelahan!
    *   **Pesan Error di Python:** `RecursionError: maximum recursion depth exceeded`
    *   **Piko berkata:** "Waduh! Kebanyakan bayangan! Aku lupa bilang kapan harus berhenti menggandakan diri!"

2.  **Mantra yang Salah Arah (Not Progressing Towards Base Case):**
    Jika Piko salah mengucapkan mantra, misalnya menyuruh bayangan menghitung apel dengan jumlah yang *bertambah* bukan berkurang (`hitung_mundur_apel(jumlah_apel + 1)`). Bayangan Piko tidak akan pernah mencapai kondisi "apel habis" dan akan terus menggandakan diri.
    *   **Pesan Error di Python:** `RecursionError: maximum recursion depth exceeded`
    *   **Piko berkata:** "Astaga! Aku menyuruh bayanganku menghitung ke arah yang salah! Harusnya makin sedikit, bukan makin banyak!"

Piko belajar bahwa setiap menggunakan Cermin Ajaib (rekursi), ia harus memastikan ada:
1.  **Mantra Berhenti yang Jelas (Base Case):** Kapan bayangan Piko harus berhenti menggandakan diri.
2.  **Mantra yang Menuju Pemberhentian (Recursive Step Towards Base Case):** Setiap bayangan baru harus mengerjakan tugas yang lebih kecil atau lebih dekat ke kondisi berhenti.

Dengan begitu, Cermin Ajaib Pengganda Diri akan menjadi alat yang sangat berguna untuk Piko si Koding Kancil! Sampai jumpa di petualangan Piko selanjutnya!
