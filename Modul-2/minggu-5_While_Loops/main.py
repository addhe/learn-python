# main.py untuk Modul-2/minggu-5_While_Loops/
# Petualangan di Kerajaan Kode: `while` Loop, si Mesin Pengulang Tak Kenal Lelah!

# --- Piko si Koding Kancil dan Mesin `while` Loop ---
print("--- Piko dan Mesin `while` Loop ---")

# 1. Piko Menghitung Mundur Roket
# ===============================
print("\n--- 1. Piko Menghitung Mundur Roket ---")
hitungan_mundur = 5
print(f"Piko punya {hitungan_mundur} detik sebelum roket meluncur.")
print("Bersiap untuk peluncuran roket Piko!")

while hitungan_mundur > 0:  # Selama hitungan_mundur masih lebih besar dari 0
    print(f"{hitungan_mundur}...")
    hitungan_mundur = hitungan_mundur - 1  # Ini penting! Mengurangi hitungan agar loop berhenti.
    # Cara lain: hitungan_mundur -= 1

print("MELUNCUR! Roket Piko terbang tinggi!\n")

# 2. Piko Menebak Angka Rahasia (Membutuhkan input pengguna)
# ========================================================
# Piko: "Bagian ini seru kalau dijalankan langsung, Jagoan!"
# Kamu bisa menghilangkan tanda komentar di bawah ini untuk mencobanya.

# import random # Kita butuh ini untuk angka acak
# angka_rahasia_piko = random.randint(1, 10)
# tebakan_kamu = 0 # Mulai dengan tebakan yang pasti salah
# jumlah_tebakan = 0
# print("\n--- 2. Piko Menebak Angka Rahasia ---")
# print("Piko punya angka rahasia antara 1 dan 10. Coba tebak!")

# while tebakan_kamu != angka_rahasia_piko:
#     jumlah_tebakan += 1
#     while True: # Loop kecil untuk memastikan input adalah angka
#         tebakan_str = input(f"Tebakan ke-{jumlah_tebakan} (angka 1-10): ")
#         if tebakan_str.isdigit():
#             tebakan_kamu = int(tebakan_str)
#             break # Keluar dari loop input jika sudah angka
#         else:
#             print("Oops, itu bukan angka, Jagoan! Coba lagi.")

#     if tebakan_kamu < angka_rahasia_piko:
#         print("Terlalu kecil! Coba lagi yang lebih besar.")
#     elif tebakan_kamu > angka_rahasia_piko:
#         print("Terlalu besar! Coba lagi yang lebih kecil.")

# print(f"Hore! Kamu benar setelah {jumlah_tebakan} tebakan! Angka rahasia Piko adalah {angka_rahasia_piko}. Kamu hebat!\n")


# 3. Mantra Tambahan: `break` (Mantra Berhenti Paksa)
# ==================================================
print("--- 3. Mantra `break` (Berhenti Paksa) ---")
angka_hitung = 0
print("Piko menghitung, tapi akan berhenti jika angka mencapai 3:")
while angka_hitung < 10: # Seharusnya bisa sampai 9
    print(f"Piko menghitung: {angka_hitung}")
    if angka_hitung == 3:
        print("Piko bilang: Cukup sampai di sini! (Mantra `break` diucapkan!)")
        break  # Langsung keluar dari loop `while` ini
    angka_hitung += 1
print(f"Piko berhenti menghitung pada angka: {angka_hitung}\n")

# 4. Mantra Tambahan: `continue` (Mantra Lewati Putaran Ini)
# ========================================================
print("--- 4. Mantra `continue` (Lewati Putaran Ini) ---")
angka_ajaib = 0
print("Piko akan mencetak angka ganjil di bawah 10:")
while angka_ajaib < 10:
    angka_ajaib += 1
    if angka_ajaib % 2 == 0: # Jika angka_ajaib adalah genap
        # print(f"(Angka {angka_ajaib} adalah genap, Piko lewati dengan `continue`)")
        continue # Lewati sisa kode di putaran ini, langsung ke cek kondisi `while` lagi
    print(f"Piko menemukan angka ganjil: {angka_ajaib}")
print("Pencarian angka ganjil selesai!\n")

# 5. "Uh-Oh!" dari Piko: Bahaya Loop Tak Terhingga!
# =================================================
print("--- 5. 'Uh-Oh!' dari Piko: Bahaya Loop Tak Terhingga! ---")
# Piko: "Hati-hati, Jagoan! Jika kondisi `while` tidak pernah jadi False, Piko bisa terjebak!"

# Contoh Loop Tak Terhingga (JANGAN DIJALANKAN kecuali kamu tahu cara menghentikannya: Ctrl+C)
# angka_bahaya = 0
# print("Ini contoh loop yang (sengaja) salah dan bisa tak terhingga:")
# while angka_bahaya < 5:
#     print(f"Piko terjebak di angka {angka_bahaya}! Tolong! Tekan Ctrl+C untuk menyelamatkan Piko!")
#     # LUPA: angka_bahaya += 1  <-- Baris ini hilang, jadi angka_bahaya selalu 0, dan 0 < 5 selalu True!

print("Piko selalu memastikan ada jalan keluar dari `while` loop!\n")

# Mengintegrasikan contoh yang mungkin sudah ada sebelumnya
# Jika file main.py sebelumnya memiliki contoh spesifik, kita bisa letakkan di sini
# atau memastikan contoh baru kita sudah mencakupnya.
# Untuk kasus ini, contoh Piko lebih komprehensif.

# Contoh dasar yang mungkin ada sebelumnya (seperti di prompt awal):
print("--- Contoh Dasar (jika ada sebelumnya) ---")
counter_dasar = 0
limit_dasar = 3 # Dibuat lebih pendek agar tidak terlalu banyak output
print(f"Contoh dasar: Menghitung dari {counter_dasar} sampai kurang dari {limit_dasar}")
while counter_dasar < limit_dasar:
    print("Current counter value (contoh dasar):", counter_dasar)
    counter_dasar += 1
print("While loop (contoh dasar) has completed.\n")

print("Petualangan hari ini tentang `while` Loop si Mesin Pengulang Tak Kenal Lelah selesai!")
print("Kamu semakin tangguh di Kerajaan Kode, Jagoan Cilik!")