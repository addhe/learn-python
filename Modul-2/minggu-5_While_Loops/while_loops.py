"""
while loops adalah salah satu cara untuk mengulang sesuatu dalam bahasa pemrograman Python.

While loops digunakan untuk mengulang suatu blok kode selama kondisi tertentu terpenuhi.
Kondisi tersebut biasanya berupa ekspresi boolean yang menghasilkan nilai True atau False.

number = 0
while number <= 5:
    print(number)
    number = number + 1

def factorial(n):
    result = n
    start = n
    n = n - 1
    while n > 0:
        result = result * n
        n = n - 1
    return result

# contoh penggunaan while dengan fungsi
print(factorial(5)) # 120

# contoh penggunaan while dengan list
numbers = [1, 2, 3, 4, 5]
while numbers:
    number = numbers.pop()
    print(number)

    
angka = 10
while angka > 0:
    print(angka)
    angka -= 1

baris = 1
while baris <= tinggi:
    print("* " * baris)
    baris += 1

# contoh while dengan string
string = "Hello, World!"
while string:
    print(string)
    string = string[1:]
    
# buatkan program untuk pengecekan password 3x jika salah program akan berhenti dengan while loops
password = "pythonia"
percobaan = 0
while percobaan < 3:
    input_password = input("Masukkan password: ")
    if input_password == password:
        print("Password benar!")
        break
    else:
        print("Password salah!")
        percobaan += 1
else:
    print("Anda telah mencoba 3 kali. Program berhenti.")

# buatkan program python triangle dengan while loops as bentuk segitiga terbalik
tinggi = 5
for i in range(tinggi, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
# contoh output

 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      * 

"""