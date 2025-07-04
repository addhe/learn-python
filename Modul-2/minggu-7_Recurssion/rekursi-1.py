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

hitung_mundur_apel(15)