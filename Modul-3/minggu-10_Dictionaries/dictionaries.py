# Contoh dictionary
data_diri = {
    "nama": "John Doe",
    "umur": 30,
    "pekerjaan": "Software Engineer"
}
print(data_diri)

# Mengakses elemen dictionary
print(data_diri["nama"])
print(data_diri.get("umur"))

# Menambahkan elemen ke dictionary
data_diri["alamat"] = "Jakarta"
print(data_diri)

# Menghapus elemen dari dictionary
data_diri.pop("pekerjaan")
print(data_diri)

# Mengubah elemen dictionary
data_diri["umur"] = 31
print(data_diri)
