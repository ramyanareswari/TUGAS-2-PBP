# Tugas 2 PBP 
Oleh:

Ramya Nareswari Wikantiyoso

2106751606

PBP A

## Bagan Aplikasi Django

## Kegunaan *Virtual Environment*
*Virtual environment* tidak terbatas pada Django saja, tetapi juga berlaku untuk seluruh proyek Python.

Dalam membuat sebuah aplikasi berbasis Django, bisa saja *tidak* menggunakan *virtual environment*. Namun, misalkan kita akan membuat dua proyek yang berbeda, yaitu Proyek A dan Proyek B. 

Apabila kedua proyek membutuhkan versi Django yang berbeda, lalu kita tidak menggunakan *virtual environment* saat meng-*install* Django yang terbaru, maka seluruh library Django tsb akan di-*install* pada direktori global. Hal tersebut akan berpengaruh pada Proyek A, yang pada kasus ini tidak membutuhkan versi Django terbaru.

Jadi, sangat direkomendasikan untuk menggunakan *virtual environment* yang dapat mengisolasi setiap proyek. Dengan kata lain, proyek A dan proyek B akan memiliki library yang berbeda dan kedua proyek tidak akan terpengaruh satu sama lain.

## Implementasi Kode



