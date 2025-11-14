# Game tebak angka
import random

def play_game(difficulty):
    """
    Fungsi utama untuk menjalankan game tebak angka.
    """
    if difficulty == "mudah":
        lower_bound = 1
        upper_bound = 50
        max_guesses = 10
    elif difficulty == "sedang":
        lower_bound = 1
        upper_bound = 100
        max_guesses = 7
    else: # sulit
        lower_bound = 1
        upper_bound = 200
        max_guesses = 5

    angka_rahasia = random.randint(lower_bound, upper_bound)
    jumlah_tebakan = 0

    print(f"\nSaya telah memilih sebuah angka antara {lower_bound} dan {upper_bound}.")
    print(f"Kamu memiliki {max_guesses} kali kesempatan untuk menebaknya.")

    while jumlah_tebakan < max_guesses:
        try:
            tebakan = int(input("Masukkan tebakanmu: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue

        jumlah_tebakan += 1

        if tebakan < angka_rahasia:
            print("Tebakanmu terlalu kecil!")
        elif tebakan > angka_rahasia:
            print("Tebakanmu terlalu besar!")
        else:
            print(f"Selamat, kamu berhasil menebak angkanya dalam {jumlah_tebakan} kali tebakan!")
            return

    print(f"Maaf, kamu kehabisan kesempatan. Angka rahasianya adalah {angka_rahasia}.")

def main():
    """
    Fungsi utama untuk menjalankan program.
    """
    print("Selamat datang di game tebak angka!")

    while True:
        print("\nPilih tingkat kesulitan:")
        print("1. Mudah (1-50, 10 tebakan)")
        print("2. Sedang (1-100, 7 tebakan)")
        print("3. Sulit (1-200, 5 tebakan)")

        pilihan = input("Masukkan pilihanmu (1/2/3): ")

        if pilihan == "1":
            difficulty = "mudah"
        elif pilihan == "2":
            difficulty = "sedang"
        elif pilihan == "3":
            difficulty = "sulit"
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        play_game(difficulty)

        play_again = input("\nApakah kamu ingin bermain lagi? (y/n): ")
        if play_again.lower() != "y":
            print("Terima kasih telah bermain!")
            break

if __name__ == "__main__":
    main()
