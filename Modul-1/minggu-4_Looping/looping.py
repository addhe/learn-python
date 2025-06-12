"""
    # Python program looping adalah pernyataan yang digunakan untuk melakukan perulangan
    # pada suatu blok kode
    # Looping di python ada 2 jenis yaitu
    # 1. for loop
    # 2. while loop
    # for loop adalah pernyataan yang digunakan untuk melakukan perulangan
    # pada suatu blok kode dengan jumlah perulangan yang sudah ditentukan
    # while loop adalah pernyataan yang digunakan untuk melakukan perulangan
    # pada suatu blok kode dengan jumlah perulangan yang tidak ditentukan
    # Looping di python juga bisa menggunakan fungsi range() untuk melakukan perulangan
    # pada suatu blok kode dengan jumlah perulangan yang sudah ditentukan
    # Fungsi range() adalah fungsi yang digunakan untuk menghasilkan urutan angka
    # dari 0 sampai n-1
    # Fungsi range() juga bisa digunakan untuk menghasilkan urutan angka
"""

"""
x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

----
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5)

----
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
attempts(5)

----
username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()
#This code will give an error because get_username is not defined

----
while my_variable < 10:
    print("Hello")
    my_variable += 1
#This code will give a NameError
#Variable is not defined 

----
my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1


----
x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1

product = 1
while x < 10:
    product = product * x
    x = x + 1

print(sum, product)
#Ouput 45 1

----

while x % 2 == 0:
    x = x / 2
#No output

----
if x != 0:
    while x % 2 == 0:
        x = x / 2
#No output

----
while x != 0 and x % 2 == 0:
    x = x / 2
#No output

----
while True:
    do_something_cool()
    if user_requested_to_stop():
        break
#This code will give an error because do_something_cool is not defined

----

"""

"""
# Sebuah for loop mengulangi urutan nilai. Contoh yang sangat sederhana dari loop for adalah mengulangi urutan angka seperti ini.
# Perhatikan bagaimana struktur ini mirip dengan struktur yang telah kita lihat. Baris pertama menunjukkan kata kunci yang membedakan.
# Dalam hal ini, itu untuk, dan berakhir dengan usus besar. Tubuh loop diindentasi ke kanan seperti yang kita lihat di loop while.
# Blok if, dan definisi fungsi. Yang berbeda dalam kasus ini adalah bahwa kita memiliki kata kunci di. 
# Juga, antara kata kunci for dan kata kunci dalam, kita memiliki nama variabel.
# Variabel ini akan mengambil setiap nilai dalam urutan yang diulangi loop.
# Dalam contoh ini, itu akan mengulangi melalui urutan angka yang dihasilkan menggunakan fungsi rentang.
# Ada dua hal penting yang ingin saya sampaikan tentang fungsi rentang ini.
# Pertama, dalam Python dan banyak bahasa pemrograman lainnya, rentang angka akan dimulai dengan nilai nol secara default.
# Kedua, daftar angka yang dihasilkan akan menjadi satu kurang dari nilai yang diberikan.
# Dalam contoh sederhana di sini, x akan mengambil nilai 0, 1, 2, 3 dan 4. Mari kita periksa ini.

"""

"""
# Contoh Python Loop
product = 1
for n in range(1,10):
  product = product * n

print(product)

# The loop will terminate when the value of n is 9. At this point, the value of product will be 1 * 2 * 3 * ... * 9 = 362880.
def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))

for n in range(x, y, z):
    print(n)

for n in range(1, 5, 6):  
    print(n)

# This loop iterates on the value of the "n" variable in a range
# of 0 to 10 (the value of the end-of-range index 11 is excluded).
# The incremental value for the loop is 2. The print() function will 
# output the resulting value of "n" as the loop counts from 0 to 10 
# (end-of-range index 11) in incremental steps of 2. This is one 
# method that can be used in Python to print a list of even numbers.


for n in range(0,11,2):
    print(n)

# The loop should print 0, 2, 4, 6, 8, 10

# This loop iterates on the value of the "number" variable in a range
# of 2 to 7+1 (the value of the end-of-range index 7 is excluded, so 
# +1 has been added to the parameter to include the numeric value 7 in 
# the range). The incremental value for the loop is the default of +1.
# The print() function will output the resulting value of "number" 
# multiplied by 3.


for number in range(2,7+1):
    print(number*3)


# The loop should print 6, 9, 12, 15, 18, 21

# This loop iterates on the value of the "x" variable in a range
# of 2 to -1 (the end-of-range index -2 is excluded). The third 
# parameter is also a negative number, making it a decremental value
# of -1. The print() function will output the resulting value of
# "x" as it starts at 2 and counts down to -1 (index -2).


for x in range(2, -2, -1):
    print(x)


# The loop should print 2, 1, 0, -1


Key takeaways

The roles of the range(start, stop, step) function parameters are:
Start - Beginning of range
- value included in range
- default = 0

Stop - End of range
- value excluded from range (to include, use stop+1)
- no default
- must provide the ending index number 

Step - Incremental value 
- default = 1


for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)

for element in long_list:
  do_something(element)

for element1 in long_list:
  for element2 in long_list:
    do_something(element1, element2)



"""
