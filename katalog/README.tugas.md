# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

## Ramya Nareswari Wikantiyoso (2106751606)


## Link Aplikasi
https://tugaspbp.herokuapp.com/katalog/

## Bagan Aplikasi Django
![Bagan](https://github.com/ramyanareswari/TUGAS-2-PBP/blob/main/bagan.png)

### Penjelasan
1. Client (user) mengirimkan request ke server, yaitu Django, melalui `urls.py`
2. Request diterima, lalu `views.py` akan query ke Database melalui `models.py`
3. Template HTML lalu dirender dan response dikirim pada client dalam bentuk tampilan website


## Kegunaan *Virtual Environment*
*Virtual environment* tidak terbatas pada Django saja, tetapi juga berlaku untuk seluruh proyek Python.

Dalam membuat sebuah aplikasi berbasis Django, bisa saja *tidak* menggunakan *virtual environment*. Namun, misalkan kita akan membuat dua proyek yang berbeda, yaitu Proyek A dan Proyek B. 

Apabila kedua proyek membutuhkan versi Django yang berbeda, lalu kita tidak menggunakan *virtual environment* saat meng-*install* Django yang terbaru, maka seluruh library Django tsb akan di-*install* pada direktori global. Hal tersebut akan berpengaruh pada Proyek A, yang pada kasus ini tidak membutuhkan versi Django terbaru.

Jadi, sangat direkomendasikan untuk menggunakan *virtual environment* yang dapat mengisolasi setiap proyek. Dengan kata lain, proyek A dan proyek B akan memiliki library yang berbeda dan kedua proyek tidak akan terpengaruh satu sama lain.

## Implementasi Kode
1. Melakukan perintah `git clone` untuk menyalin repositori tugas PBP
2. Menyalakan virtual env dan meng-*install* *dependencies*
3. Pada `views.py`, saya menambahkan sebuah fungsi `show_catalog` yang menerima parameter `request` dan mengembalikan merender katalog.html dengan method `render()`. Fungsi menyimpan data yang diambil dari models.py ke dalam variable `context` yang bertipe dictionary. Variable tersebut akan menyimpan hasil query dari seluruh data pada `CatalogItem`
4. Pada `urls.py`, function `show_catalog` didefinisikan di dalam urlpatterns dengan menambahkan *snippet* sebagai berikut
```
urlpatterns = [
    ...
    path('katalog/', include('katalog.urls')),
]
``` 
5. Daftar katalog ditampilkan dengan melakukan iterasi terhadap `list_data` dengan menambahkan *snippet* berikut pada `katalog.html`
```
  ...
    {% comment %} Add the data below this line {% endcomment %}
    {% for item in catalog_data %}
      <tr>
        <th>{{item.item_name}}</th>
        <th>{{item.item_price}}</th>
        <th>{{item.item_stock}}</th>
        <th>{{item.description}}</th>
        <th>{{item.rating}}</th>
        <th>{{item.item_url}}</th>
      </tr>
    {% endfor %}
  </table>
  ...
```
### Deployment
6. Langkah terakhir adalah men-*deploy* aplikasi ke Heroku dengan menambahkan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` pada Github `Action -> Secrets`


