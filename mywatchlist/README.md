# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

## Ramya Nareswari Wikantiyoso (2106751606)


## Link Aplikasi

## Jawaban Pertanyaan ✅

### Jelaskan perbedaan antara JSON, XML, dan HTML!

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

### Implementasi Kode
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
9. Lalu, untuk memasukkan data tersebut ke dalam database Django lokal, menggunakan perintah `c`

3. Menambahkan file `urls.py` pada folder `mywatchlist` untuk melakukan *routing* terhadap fungsi `views` agar halaman HTML dapat dilihat pada browser. Setelah itu, lakukan konfigurasi dengan menambahkan kode:

4. Melakukan konfigurasi pada `urls.py` yang ada di folder `project_django` dan folder `mywatchlist`
