# Tugas 3: Data Delivery Menggunakan Django

## Ramya Nareswari Wikantiyoso (2106751606)


## Link Aplikasi

## Jawaban Pertanyaan ✅

### 1. Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON merupakan singkatan dari JavaScript Object Notation. Oleh karena itu, syntax JSON sebenarnya merupakan turunan dari bahasa pemrograman JavaScript. Data-data yang disimpan pada file dengan format JSON memiliki type. Sehingga kita tidak dapat mendefinisikan type baru untuk suatu object seperti pada file XML. Jika kita lihat dari hasil percobaan lab 2 kali ini, data yang ada di file JSON hanya merupakan list of strings dari apa yang di-input oleh user.
Sedangkan pada file XML, data yang ditampilkan lebih kelihatan bentuknya dan lebih terstruktur. Dan jika kita perhatikan, tampilan XML lebih mirip dengan tampilan code file html. Karena mengandung <> dan </>.

XML sendiri merupakan singkatan dari eXtensible Markup Language. Namun, berbeda dengan JSON, XML tidak menggunakan bahasa pemrograman tertentu. XML dapat dibaca oleh manusia maupun mesin. Hal tersebut yang membuat XML terkenal dengan simplicity, generality, dan usability-nya. Dan jika kita lihat pada hasil percobaan lab 2 (/lab-2/xml), XML hanya menyimpan kumpulan informasi atau data yang dibungkus dengan tag yang tidak pre-defined. Dengan demikian, seorang programmer dapat mendefinisikan tag-nya sendiri.

HTML merupakan singkatan dari Hypertext Markup Languange. Sedangkan XML merupakan singkatan dari eXtensible Markup Languange. Namun, perbedaan yang sangat jelas diantara keduanya adalah dari segi fungsi penggunaannya. HTML berfokus untuk menampilkan data. Sedangkan XML berfokus untuk menyimpan dan mengangkut data tersebut. Maka dapat dikatakan bahwa HTML adalah format-driven dan XML adalah content-driven.
Perbedaan lain antara HTML dan XML dapat dilihat dari segi tags yang tersedia pada masing-masing markup language. Sesuai namanya, eXtensible Markup Language, XML memiliki tags yang extensible. Sedangkan HTML memiliki tags yang terbatas. Karena terbatas, maka tags dari HTML sudah di-define secara automatis. Sedangkan tags XML tidaklah pre-defined. Sehingga kita dapat menuliskan tags baru sesuai dengan kebutuhan kita.

### 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

### 3. Implementasi Kode
1. `cd` ke direktori tempat `TUGAS-2-PBP` berada
2. Menyalakan virtual environment dengan perintah `python -m venv env`, lalu `env\Scripts\activate.bat` dan `pip install -r requirements.txt`
2. Buat aplikasi bernama `mywatchlist` dengan perintah `python manage.py startapp mywatchlist`
3. Melakukan konfigurasi pada `settings.py` di folder `project_django` dengan menambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS`. Hal tersebut dilakukan untuk mendaftarkan aplikasi `mywatchlist` ke dalam proyek Django

5. Menambahkan *code snippet* di bawah ke dalam file `models.py` pada folder `mywatchlist`

6. Lakukan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal.

7. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

8. Membuat folder `fixtures` di dalam folder aplikasi `mywatchlist`, lalu membuat berkas `initial_watchlist_data.json` yang berisi:
```

```
9. Lalu, untuk memasukkan data tersebut ke dalam database Django lokal, menggunakan perintah `python manage.py loaddata initial_watchlist_data.json`

3. Menambahkan file `urls.py` pada folder `mywatchlist` untuk melakukan *routing* terhadap fungsi `views` agar halaman HTML dapat dilihat pada browser. Setelah itu, lakukan konfigurasi dengan menambahkan kode:

4. Melakukan konfigurasi pada `urls.py` yang ada di folder `project_django` dan folder `mywatchlist`
