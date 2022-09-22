# Tugas 3: Data Delivery Menggunakan Django

## Ramya Nareswari Wikantiyoso (2106751606)


## New Repository Link 🔗
https://github.com/ramyanareswari/DUMMY-TUGAS-PBP

## Link Aplikasi 🔗
https://assignmentpbp.herokuapp.com/mywatchlist/

https://assignmentpbp.herokuapp.com/mywatchlist/html/

## Jawaban Pertanyaan ✅

### 1. Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON (JavaScript Object Notation) merupakan turunan dari bahasa pemrograman JavaScript. Data yang ada di file JSON hanya merupakan list of strings dari apa yang di-input oleh user. Data tersebut tidak memiliki tag yang didefinisikan secara langsung.

XML (eXtensible Markup Language) tidak menggunakan bahasa pemrograman tertentu. XML dapat dibaca dengan musah oleh manusia maupun mesin  karena strukturnya. XML  menyimpan data yang dibungkus dengan tag yang tidak pre-defined, dan tag tersebut dapat didefinisikan secara manual.

HTML (Hypertext Markup Languange) berfokus untuk menampilkan data kepada user, berbeda dengan  XML yang menyimpan data tersebut. HTML biasa disebut format-driven. HTML memiliki tags yang terbatas, sehingga tags-tags yang ada didefinisikan secara otomatis.

### 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena pada implementasi development sebuah platform, dibutuhkan banyak data untuk diambil, diubah, digabungkan, dan dikirimkan ke user.

### 3. Implementasi Kode
1. `cd` ke direktori tempat `dummy-tugas-pbp` berada
2. Menyalakan virtual environment dengan perintah `python -m venv env`, lalu `env\Scripts\activate.bat` dan `pip install -r requirements.txt`
2. Buat aplikasi bernama `mywatchlist` dengan perintah `python manage.py startapp mywatchlist`
3. Melakukan konfigurasi pada `settings.py` di folder `project_django` dengan menambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS`. Hal tersebut dilakukan untuk mendaftarkan aplikasi `mywatchlist` ke dalam proyek Django
4. Menambahkan *code snippet* di bawah ke dalam file `models.py` pada folder `mywatchlist`
5. Melakukan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
6. Melakukan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
7. Membuat folder `fixtures` di dalam folder aplikasi `mywatchlist`, lalu membuat berkas `initial_watchlist_data.json` yang berisi data dari objek
8. Lalu, untuk memasukkan data tersebut ke dalam database Django lokal, menggunakan perintah `python manage.py loaddata initial_watchlist_data.json`
9. Menambahkan file `urls.py` pada folder `mywatchlist` untuk melakukan *routing* terhadap fungsi `views` agar halaman HTML dapat dilihat pada browser. Setelah itu, lakukan konfigurasi dengan menambahkan kode:
10. Melakukan konfigurasi pada `urls.py` yang ada di folder `project_django` dan folder `mywatchlist`
11. Untuk mengembalikan data dalam bentuk XML: buat fungsi yang mereturn function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan ``parameter content_type="application/xml"`` -> lalu tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi dengan menambahkan code berikut pada `urls.py`:
```
path('xml/', show_xml, name=’show_xml’),
```
12. Untuk mengembalikan data dalam bentuk JSON: buat fungsi yang mereturn function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan ``parameter content_type="application/json"`` -> lalu tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi dengan menambahkan code berikut pada `urls.py`:
```
path('json/', show_json, name=’show_json’), 
```
13. Langkah terakhir adalah men-*deploy* aplikasi ke Heroku dengan menambahkan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` pada Github `Action -> Secrets`

### Screenshot Postman
![Postman1](https://github.com/ramyanareswari/dummy-tugas-pbp/blob/main/mywatchlist/screenshot/postman1.png)
![Postman2](https://github.com/ramyanareswari/dummy-tugas-pbp/blob/main/mywatchlist/screenshot/postman2.png)
![Postman3](https://github.com/ramyanareswari/dummy-tugas-pbp/blob/main/mywatchlist/screenshot/postman3.png)