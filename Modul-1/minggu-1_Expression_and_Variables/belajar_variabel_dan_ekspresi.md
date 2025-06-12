# Petualangan di Dunia Python: Kotak Ajaib dan Isinya!

Hai jagoan cilik! Selamat datang di Kerajaan Kode Python! Aku Piko, si Koding Kancil, yang akan jadi pemandumu di petualangan seru ini! Hari ini, kita akan belajar dua mantra sihir pertama: **Variabel** si Kotak Ajaib dan **Ekspresi** si Tongkat Pengubah! Siap?

## Kotak Ajaib (Variabel)

Bayangkan kamu punya tas ajaib yang bisa menyimpan apa saja! Di Kerajaan Kode Python, tas ajaib ini kita sebut **variabel**. Variabel itu seperti kotak mainan super canggih yang bisa kamu beri nama sesukamu dan kamu isi dengan berbagai harta karun!

Misalnya, kamu menemukan buah apel emas yang berkilauan. Kita bisa simpan apel emas itu di kotak bernama `harta_karun_pertama`.

```python
harta_karun_pertama = "apel emas"
```

Sim salabim! Sekarang, setiap kali Piko atau kamu menyebut `harta_karun_pertama`, Kerajaan Kode Python langsung tahu kalau isinya adalah "apel emas". Hebat, kan?

Kamu juga bisa menyimpan angka ajaib. Misalnya, kamu punya 5 bintang keberuntungan. Kita simpan di kotak bernama `jumlah_bintang`.

```python
jumlah_bintang = 5
```

Mudah sekali! Kotak `jumlah_bintang` sekarang menyimpan angka 5. Kamu bisa membuat ribuan kotak dengan nama-nama unik untuk menyimpan semua penemuanmu di Kerajaan Kode!

## Bermain dengan Isi Kotak (Ekspresi) si Tongkat Pengubah!

Nah, ini dia bagian yang paling mendebarkan! Kita akan menggunakan **Ekspresi**, si Tongkat Pengubah, untuk melakukan keajaiban dengan isi kotak-kotak kita!

Misalnya, di kotak `jumlah_bintang` kamu punya 5 bintang. Lalu, Peri Baik Hati memberimu 2 bintang lagi, yang kita simpan di kotak `bintang_tambahan`. Berapa bintangmu sekarang?

Ayo ayunkan Tongkat Pengubah!

```python
jumlah_bintang = 5
bintang_tambahan = 2
total_bintang_sekarang = jumlah_bintang + bintang_tambahan
```

Abrakadabra! `jumlah_bintang + bintang_tambahan` adalah mantra dari Tongkat Pengubah. Kerajaan Kode Python akan menghitung `5 + 2`, dan hasilnya (yaitu 7) akan disimpan di kotak baru bernama `total_bintang_sekarang`. Jadi, sekarang kamu punya 7 bintang keberuntungan! Luar biasa!

Tongkat Pengubah juga bisa menggabungkan kata-kata ajaib. Misalnya, kita mau membuat pesan rahasia: "Piko suka apel emas".
Kita simpan "Piko suka " di kotak `kata_awal` dan "apel emas" (yang sudah ada di `harta_karun_pertama`) di kotak `harta`.

```python
kata_awal = "Piko suka "
harta = "apel emas" # atau bisa juga pakai harta_karun_pertama dari atas
pesan_rahasia = kata_awal + harta
```

Presto! Sekarang, kotak `pesan_rahasia` isinya adalah "Piko suka apel emas". Kamu bisa mengirim pesan ini ke teman-temanmu di Kerajaan Kode!

## Jangan Takut Sama "Uh-Oh!" si Pesan Kesalahan!

Kadang-kadang, saat kita mengucapkan mantra atau menggunakan Tongkat Pengubah, mungkin ada sedikit kesalahan. Di Kerajaan Kode, ini disebut **error** atau "Uh-Oh!". Tapi jangan khawatir, jagoan! "Uh-Oh!" ini bukan monster jahat. Dia sebenarnya teman yang memberitahu kita kalau ada yang perlu diperbaiki.

Misalnya, bagaimana kalau kamu mencoba mengambil isi kotak yang belum ada?

```python
# print(kotak_kosong_melompong) # Uh-Oh! Python akan bilang: NameError: name 'kotak_kosong_melompong' is not defined
```
Pesan `NameError` itu seperti Piko bilang, "Hei, aku tidak menemukan kotak bernama `kotak_kosong_melompong`! Kamu yakin sudah membuatnya?" Itu artinya kita lupa membuat kotaknya atau salah ketik namanya.

Atau, bagaimana kalau kamu salah menulis nama kotak yang sudah ada?

```python
buah_favorit = "mangga"
# print(buah_favort) # Uh-Oh! Mirip seperti tadi, ini juga NameError!
```
Lihat? Salah satu huruf saja bisa membuat Python bingung!

Bagaimana dengan Tongkat Pengubah? Bisakah dia membuat "Uh-Oh!"? Tentu saja!
Misalnya, kamu mencoba menambahkan angka dengan tulisan tanpa mengubahnya dulu:

```python
angka_ajaib = 7
kata_ajaib = "kucing"
# hasil_aneh = angka_ajaib + kata_ajaib # Uh-Oh! Python akan bilang: TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
Pesan `TypeError` ini seperti Piko bilang, "Hmm, aku bingung bagaimana cara menambahkan angka 7 dengan kata 'kucing'. Itu seperti mencoba menambahkan apel dengan sepatu, tidak bisa!" Kita harus mengubah salah satunya dulu agar jenisnya sama.

Jadi, kalau bertemu "Uh-Oh!", jangan panik ya! Baca pesannya baik-baik. Biasanya dia memberi petunjuk apa yang salah. Semua penyihir kode, bahkan yang paling hebat sekalipun, pernah bertemu "Uh-Oh!". Itu bagian dari petualangan belajar sihir kode!

**Singkatnya dari Piko:**

*   **Variabel** itu seperti tas atau kotak ajaib untuk menyimpan semua harta karunmu (bisa tulisan, bisa angka).
*   **Ekspresi** itu Tongkat Pengubah sakti yang bisa menggabungkan atau mengubah isi kotak-kotakmu.
*   **"Uh-Oh!" (Error)** itu teman kita yang memberi tahu kalau ada mantra yang perlu diperbaiki. Jangan takut padanya!

Seru kan petualangan kita hari ini di Kerajaan Kode Python? Besok kita akan belajar mantra-mantra baru yang lebih hebat lagi! Sampai jumpa, jagoan cilik!
