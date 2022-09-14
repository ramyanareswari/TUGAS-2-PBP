# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

## Ramya Nareswari Wikantiyoso

## 2106751606


## Link Aplikasi

## Bagan Aplikasi Django

## Kegunaan *Virtual Environment*
*Virtual environment* tidak terbatas pada Django saja, tetapi juga berlaku untuk seluruh proyek Python.

Dalam membuat sebuah aplikasi berbasis Django, bisa saja *tidak* menggunakan *virtual environment*. Namun, misalkan kita akan membuat dua proyek yang berbeda, yaitu Proyek A dan Proyek B. 

Apabila kedua proyek membutuhkan versi Django yang berbeda, lalu kita tidak menggunakan *virtual environment* saat meng-*install* Django yang terbaru, maka seluruh library Django tsb akan di-*install* pada direktori global. Hal tersebut akan berpengaruh pada Proyek A, yang pada kasus ini tidak membutuhkan versi Django terbaru.

Jadi, sangat direkomendasikan untuk menggunakan *virtual environment* yang dapat mengisolasi setiap proyek. Dengan kata lain, proyek A dan proyek B akan memiliki library yang berbeda dan kedua proyek tidak akan terpengaruh satu sama lain.

## Implementasi Kode
1. Melakukan perintah `git clone` untuk menyalin repositori tugas PBP
2. Menyalakan virtual env dan meng-*install* *dependencies*
3. Pada `views.py`, saya menambahkan sebuah fungsi `show_catalog` yang menerima parameter `request` dan mengembalikan merender katalog.html dengan method `render()`. Fungsi menyimpan data yang diambil dari models.py ke dalam dictionary `context`.


Daftar katalog ditampilkan ke dalam tabel dengan melakukan iterasi terhadap `list_data`



