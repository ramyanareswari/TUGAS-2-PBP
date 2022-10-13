# Tugas 6

## Ramya Nareswari Wikantiyoso (2106751606)

## Link Aplikasi 🔗
Page yang mengimplementasikan AJAX:
https://tugaspbp.herokuapp.com/todolist/new

## Jawaban Pertanyaan ✅
### 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Code pada sync programming dijalankan baris per baris dan harus mereload keseluruhan laman website untuk mengupdate konten. Code pada asnyc programming dijalankan secara paralel, sehingga jika ingin mengupdate konten laman website tidak perlu mereload keseluruhan page.

### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming adalah paradigma pemrograman dimana algoritma dieksekusi berdasarkan action dari user. Salah satu contohnya pada tugas ini adalah button "Add Task" yang membuka modal atau button "Create" pada modal


### 3. Jelaskan penerapan asynchronous programming pada AJAX.
1. Client (browser) mengirimkan request pada server setelah memanggil AJAX (XMLHttpRequest)
2. Membentuk XMLHttpRequest untuk pertukaran data
3. Data diterima oleh server lalu diproses
4. Server mengembalikan data, lalu data diterima browser dan ditampilkan langsung di page website (halaman tidak direload ulang secara keseluruhan)

## Implementasi Kode
1. Membuat view `get_task_json` untuk mengambil data task dalam bentuk json serta view `add` untuk menambahkan konten form ke dalam card HTML dan untuk menghandle request
2. Membuat function dengan AJAX
3. Routing pada urls.py agar views dapat diakses

## Belum Berhasil Diimplementasi
❎Memunculkan card setelah submit form
❎Tanggal pembuatan task
❎Update status task
❎Delete task
