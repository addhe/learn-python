def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

print("Selamat datang di Petualangan Piko dengan Cermin Ajaib (Rekursi)!")

# Cerita 1: Mantra Pengganda Piko untuk Menghitung Apel
print("\n--- Cerita 1: Mantra Pengganda Piko untuk Menghitung Apel ---")
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

print("Piko ingin menghitung 3 apel:")
hitung_mundur_apel(3)

# Uh-Oh! Momen Kesalahan (Rekursi Tanpa Base Case atau Salah Arah)
# print("\n--- Uh-Oh! Contoh Rekursi Bermasalah (Jangan dijalankan!) ---")
# def rekursi_bermasalah_tanpa_henti(n):
#     print(f"Bayangan ke-{n} muncul!")
#     rekursi_bermasalah_tanpa_henti(n + 1) # Tidak menuju base case, akan error
# # rekursi_bermasalah_tanpa_henti(1) # Ini akan menyebabkan RecursionError

# def rekursi_lupa_base_case(n):
#     # Tidak ada kondisi if n <= 0: return
#     print(f"Menghitung {n}")
#     rekursi_lupa_base_case(n - 1)
# # rekursi_lupa_base_case(3) # Ini juga akan menyebabkan RecursionError

print("\nPiko belajar pentingnya mantra berhenti (base case) dan mantra yang benar arahnya!")

# Cerita 2: Mantra Faktorial untuk Mengatur Mainan
print("\n--- Cerita 2: Mantra Faktorial untuk Mengatur Mainan ---")
def faktorial_piko(n):
    # Kasus Dasar
    if n < 0: # Menangani angka negatif
        return "Tidak bisa menghitung faktorial dari angka negatif"
    if n == 0 or n == 1:
        return 1
    # Langkah Rekursif
    else:
        return n * faktorial_piko(n - 1)

print("Piko ingin tahu berapa cara menyusun 3 balok:")
jumlah_cara = faktorial_piko(3)
print(f"Piko bisa menyusun 3 balok dengan {jumlah_cara} cara berbeda!")

print("Piko mencoba dengan 5 balok:")
print(f"Faktorial dari 5 adalah: {faktorial_piko(5)}")

print("Piko mencoba dengan 0 balok:")
print(f"Faktorial dari 0 adalah: {faktorial_piko(0)}")

print("Piko mencoba dengan angka negatif (-2):")
print(f"Faktorial dari -2 adalah: {faktorial_piko(-2)}")


# Contoh fungsi rekursif yang sudah ada sebelumnya (Fibonacci)
# Kita bisa jelaskan ini sebagai Piko menemukan gulungan mantra kuno lain
print("\n--- Piko Menemukan Gulungan Mantra Fibonacci Kuno ---")
def fibonacci(n):
    if n <= 0:
        # print("Masukkan angka positif untuk Fibonacci")
        return [] # Mengembalikan list kosong jika input tidak valid
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        # Langkah rekursif: dapatkan deret sebelumnya
        fib_sequence = fibonacci(n - 1)
        # Tambahkan elemen baru
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

print("Piko mencoba mantra Fibonacci untuk 7 angka pertama:")
print(f"Deret Fibonacci untuk 7 angka: {fibonacci(7)}")

print("Piko mencoba mantra Fibonacci untuk 1 angka:")
print(f"Deret Fibonacci untuk 1 angka: {fibonacci(1)}")

print("Piko mencoba mantra Fibonacci untuk 0 angka:")
print(f"Deret Fibonacci untuk 0 angka: {fibonacci(0)}")


if __name__ == "__main__":
    print("\n--- Ringkasan dari __main__ ---")
    print("Piko menjalankan beberapa mantra utama:")
    print(f"Mantra Hitung Mundur Apel untuk 3 apel:")
    hitung_mundur_apel(3)
    print(f"\nMantra Faktorial untuk 5 balok: {faktorial_piko(5)}")
    print(f"Mantra Fibonacci untuk 10 angka: {fibonacci(10)}")

print("\nPetualangan Piko dengan Rekursi selesai! Ia makin pintar menggunakan Cermin Ajaib!")