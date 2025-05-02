"""
    Function di python adalah sekumpulan pernyataan yang melakukan tugas tertentu.
    Fungsi dapat menerima input (parameter) dan mengembalikan output (nilai).
    Fungsi digunakan untuk mengorganisir kode, menghindari pengulangan, dan meningkatkan
    keterbacaan kode.
    Fungsi dapat didefinisikan dengan menggunakan kata kunci 'def' diikuti dengan nama fungsi,
    tanda kurung, dan tanda titik dua. Di dalam tanda kurung, kita dapat menentukan parameter
    yang akan diterima oleh fungsi. Setelah itu, kita dapat menuliskan kode yang akan dieksekusi
    ketika fungsi dipanggil. Fungsi dapat mengembalikan nilai dengan menggunakan kata kunci 'return'.
    Fungsi juga dapat memiliki parameter default, yang akan digunakan jika tidak ada argumen
    yang diberikan saat memanggil fungsi. Fungsi juga dapat memiliki parameter variabel, yang
    memungkinkan kita untuk mengirimkan sejumlah argumen yang tidak terbatas ke dalam fungsi.
    Fungsi juga dapat memiliki parameter dengan nama yang berbeda, yang memungkinkan kita untuk
    memberikan nilai pada parameter tertentu tanpa harus mengikuti urutan parameter.
"""

"""
    Function best practices:
    1. Gunakan nama fungsi yang deskriptif dan jelas.
    2. Gunakan parameter yang jelas dan deskriptif.
    3. Gunakan docstring untuk menjelaskan fungsi dan parameter.
    4. Gunakan return untuk mengembalikan nilai dari fungsi.
    5. Gunakan exception handling untuk menangani kesalahan.
    6. Gunakan default parameter untuk memberikan nilai default pada parameter.
    7. Gunakan variabel lokal di dalam fungsi untuk menghindari konflik dengan variabel global.
    8. Gunakan fungsi untuk mengorganisir kode dan menghindari pengulangan.
    9. Gunakan fungsi untuk meningkatkan keterbacaan kode.
    10. Gunakan fungsi untuk memecah kode menjadi bagian-bagian yang lebih kecil dan lebih mudah dikelola.
    11. Gunakan fungsi untuk meningkatkan modularitas kode.
    12. Gunakan fungsi untuk meningkatkan pemeliharaan kode.
    13. Gunakan fungsi untuk meningkatkan efisiensi (untuk waktu eksekusi) kode.
    14. Gunakan fungsi untuk meningkatkan keamanan kode.
    15. Gunakan fungsi untuk meningkatkan portabilitas (untuk penggunaan di berbagai platform) kode.
    16. Gunakan fungsi untuk meningkatkan fleksibilitas (untuk perubahan) kode.
    17. Gunakan fungsi untuk meningkatkan keamanan kode.
"""

# Example 1: Function without parameter
def greet():
    """
    Fungsi ini akan mencetak pesan sapaan.
    """
    print("Hello, World!")

# Example 2: Function with parameter
def add_numbers(a, b):
    """
    Fungsi ini akan menjumlahkan dua angka.
    """
    return a + b

# Example 3: Function with default parameter
def greet_user(name="User"):
    """
    Fungsi ini akan mencetak pesan sapaan dengan nama pengguna.
    """
    print(f"Hello, {name}!")

# Example 4: Function with variable-length arguments
def sum_numbers(*args):
    """
    Fungsi ini akan menjumlahkan sejumlah angka.
    """
    return sum(args)

# Example 5: Function with keyword arguments
def print_info(name, age, **kwargs):
    """
    Fungsi ini akan mencetak informasi pengguna.
    """
    print(f"Name: {name}")
    print(f"Age: {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example 6: Function with return value
def multiply_numbers(a, b):
    """
    Fungsi ini akan mengalikan dua angka dan mengembalikan hasilnya.
    """
    return a * b

# Example 7: Function with exception handling
def divide_numbers(a, b):
    """
    Fungsi ini akan membagi dua angka dan mengembalikan hasilnya.
    Jika pembagi adalah nol, fungsi akan mengembalikan pesan kesalahan.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Example 8: Function with docstring
def square_number(n):
    """
    Fungsi ini akan mengembalikan kuadrat dari angka yang diberikan.
    :param n: Angka yang akan dikuadratkan.
    :return: Kuadrat dari angka yang diberikan.
    """
    return n ** 2

# Example 9: Function with lambda expression
def square_lambda(n):
    """
    Fungsi ini akan mengembalikan kuadrat dari angka yang diberikan menggunakan lambda expression.
    :param n: Angka yang akan dikuadratkan.
    :return: Kuadrat dari angka yang diberikan.
    """
    return (lambda x: x ** 2)(n)

# Example 10: Function with list comprehension
def even_numbers(n):
    """
    Fungsi ini akan mengembalikan list angka genap dari 0 hingga n.
    :param n: Batas atas untuk angka genap.
    :return: List angka genap dari 0 hingga n.
    """
    return [x for x in range(n + 1) if x % 2 == 0]

# Example 11: Function with mapping
def square_mapping(numbers):
    """
    Fungsi ini akan mengembalikan list kuadrat dari angka-angka yang diberikan.
    :param numbers: List angka yang akan dikuadratkan.
    :return: List kuadrat dari angka-angka yang diberikan.
    """
    return list(map(lambda x: x ** 2, numbers))

# Example 12: Function with filtering
def filter_even_numbers(numbers):
    """
    Fungsi ini akan mengembalikan list angka genap dari list yang diberikan.
    :param numbers: List angka yang akan difilter.
    :return: List angka genap dari list yang diberikan.
    """
    return list(filter(lambda x: x % 2 == 0, numbers))

# Example 13: Function with recursion
def factorial(n):
    """
    Fungsi ini akan mengembalikan faktorial dari angka yang diberikan.
    :param n: Angka yang akan dihitung faktorialnya.
    :return: Faktorial dari angka yang diberikan.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example 14: Function with closure
def outer_function(x):
    """
    Fungsi ini akan mengembalikan fungsi dalam fungsi (closure).
    :param x: Angka yang akan digunakan dalam fungsi dalam fungsi.
    :return: Fungsi dalam fungsi (closure).
    """
    def inner_function(y):
        return x + y
    return inner_function

# Example 15: Function with decorator
def decorator_function(func):
    """
    Fungsi ini akan mengembalikan fungsi dalam fungsi (decorator).
    :param func: Fungsi yang akan di-dekorasi.
    :return: Fungsi dalam fungsi (decorator).
    """
    def wrapper_function(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper_function

# Example 16: Function with generator
def number_generator(n):
    """
    Fungsi ini akan mengembalikan generator yang menghasilkan angka dari 0 hingga n.
    :param n: Batas atas untuk angka.
    :return: Generator yang menghasilkan angka dari 0 hingga n.
    """
    for i in range(n + 1):
        yield i

# Example 17: Function with lambda expression and filter
def filter_even_numbers_lambda(numbers):
    """
    Fungsi ini akan mengembalikan list angka genap dari list yang diberikan menggunakan lambda expression.
    :param numbers: List angka yang akan difilter.
    :return: List angka genap dari list yang diberikan.
    """
    return list(filter(lambda x: x % 2 == 0, numbers))

def square_numbers_lambda(numbers):
    """
    Fungsi ini akan mengembalikan list kuadrat dari angka-angka yang diberikan menggunakan lambda expression.
    :param numbers: List angka yang akan dikuadratkan.
    :return: List kuadrat dari angka-angka yang diberikan.
    """
    return list(map(lambda x: x ** 2, numbers))

# Example 18: Function with lambda expression and map
def even_numbers_lambda(n):
    """
    Fungsi ini akan mengembalikan list angka genap dari 0 hingga n menggunakan lambda expression.
    :param n: Batas atas untuk angka genap.
    :return: List angka genap dari 0 hingga n.
    """
    return list(map(lambda x: x if x % 2 == 0 else None, range(n + 1)))

# Example 19: Function with lambda expression and filter
def odd_numbers_lambda(n):
    """
    Fungsi ini akan mengembalikan list angka ganjil dari 0 hingga n menggunakan lambda expression.
    :param n: Batas atas untuk angka ganjil.
    :return: List angka ganjil dari 0 hingga n.
    """
    return list(filter(lambda x: x % 2 != 0, range(n + 1)))

# Example 20: Function with lambda expression and reduce
from functools import reduce

def sum_numbers_lambda(numbers):
    """
    Fungsi ini akan mengembalikan jumlah dari list angka menggunakan lambda expression.
    :param numbers: List angka yang akan dijumlahkan.
    :return: Jumlah dari list angka.
    """
    return reduce(lambda x, y: x + y, numbers)

# Example 21: Function with lambda expression and zip
def zip_lists(list1, list2):
    """
    Fungsi ini akan mengembalikan list yang merupakan hasil penggabungan dua list menggunakan lambda expression.
    :param list1: List pertama yang akan digabungkan.
    :param list2: List kedua yang akan digabungkan.
    :return: List yang merupakan hasil penggabungan dua list.
    """
    return list(map(lambda x, y: (x, y), list1, list2))

# Example 22: Function with lambda expression and sorted
def sort_list_lambda(numbers):
    """
    Fungsi ini akan mengembalikan list yang sudah diurutkan menggunakan lambda expression.
    :param numbers: List angka yang akan diurutkan.
    :return: List yang sudah diurutkan.
    """
    return sorted(numbers, key=lambda x: x)

# Example 23: Function with lambda expression and filter
def filter_even_numbers_lambda(numbers):
    """
    Fungsi ini akan mengembalikan list angka genap dari list yang diberikan menggunakan lambda expression.
    :param numbers: List angka yang akan difilter.
    :return: List angka genap dari list yang diberikan.
    """
    return list(filter(lambda x: x % 2 == 0, numbers))

# Example 24: Explain lambda expression
def explain_lambda():
    """
    Lambda expression adalah fungsi anonim yang dapat digunakan untuk membuat fungsi
    sederhana tanpa harus mendefinisikan fungsi secara eksplisit. Lambda expression
    biasanya digunakan untuk fungsi-fungsi kecil yang hanya digunakan sekali.
    """
    pass

# Example 25: Function with lambda expression and map
def square_numbers_lambda(numbers):
    """
    Fungsi ini akan mengembalikan list kuadrat dari angka-angka yang diberikan menggunakan lambda expression.
    :param numbers: List angka yang akan dikuadratkan.
    :return: List kuadrat dari angka-angka yang diberikan.
    """
    return list(map(lambda x: x ** 2, numbers))
