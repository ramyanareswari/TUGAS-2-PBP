# Tugas 4: Implementasi Form dan Autentikasi

## Ramya Nareswari Wikantiyoso (2106751606)

## Link Aplikasi 🔗
https://tugaspbp.herokuapp.com/todolist

## Jawaban Pertanyaan ✅
### Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Tag `{% csrf_token %}` berguna untuk menghindari serangan CSRF (Cross-Site Request Forgery). Serangan CSRF adalah ketika penyerang dapat dengan mudah mengajukan request pada aplikasi web yang telah dilakukan autentikasi oleh pengguna (pengguna sudah login). Token CSRF digenerate secara unik saat proses rendering HTML, yang berarti tidak ada token yang sama antar website. 

Apabila tidak ada tag `{% csrf_token %}` di dalam elemen form, maka akan muncul error (tepatnya ketika pengguna melakukan submit pada form), karena tidak adanya tag tersebut sama artinya dengan tidak adanya validasi untuk kredibilitas data yang dikirim ke server.

### Apakah kita dapat membuat elemen secara manual (tanpa menggunakan generator seperti  `{{ form.as_table }})`? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.
Bisa. Caranya yaitu:
1. Membuat suatu model dummy, misal `Judul`
2. Membuat dua template html, `form.html` untuk form dan `home.html` untuk menampilkan data hasil submit form. Lalu, untuk membuat form yaitu dengan tag <form> dan jangan lupa ditambahkan method `POST`. Pada baris di bawahnya, tambahkan tag {% csrf_token %}. Contoh mplementasinya seperti di bawah:
```html
    <form action="" method="POST">
        {% csrf_token %}
        <label for="title">Title: </label>
        <input id="title" type="text" name="title" required>
    </form>
```
3. Membuat suatu function dalam `views.py` agar mekanisme form dapat bekerja
```python
 def foo(request):
        if request.method == "POST":
            title = request.POST.get("title")
            add_title = Judul(title=title)
            add.title.save()
            return HttpResponseRedirect("/home.html/")
        else:
            return render(request, "home.html")
```


### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML `form`, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
1. Browser akan mengirimkan request data ketika user selesai mengisi form dengan metode POST. 
2. Hasil request data akan diterima oleh server (urls.py) dan data di dalam database akan berubah
3. Server akan mengecek validitas request yang dikirimkan
4. `urls.py` akan menelusuri `views.py` untuk mencari method yang tepat untuk handle request
5. Server mengirim HTTP Response berupa file .html (user akan diarahkan ke page lain)

![Bagan](https://github.com/ramyanareswari/TUGAS-2-PBP/blob/main/todolist/Form.png)

Sumber: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

## Implementasi Kode
### Membuat Aplikasi Baru
`py manage.py startapp todolist`

### Routing
Menambahkan path('todolist/', include('todolist.urls')) pada urls.py di dalam project_django untuk memberikan route pada aplikasi todolist, sehingga app bisa diakses melalui browser di /todolist. 

Setelah itu, , menambahkan app_name berupa 'todolist' pada urls.py milik todolist app dan list urlpatterns berisi path('', show_todo, name='show_todo'), sehingga ketika browser mengunjungi path /todolist, fungsi show_todo akan dipanggil.

### Migrasi skema model ke database
1. Membuat file models.py
2. Melakukan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
3. Melakukan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

### Menambahkan mekanisme `registrasi`, `login`, dan `logout`
1. Menambahkan snippet kode berikut pada `views.py`
```python
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
```
2. Setelah itu, melakukan konfigurasi kembali pada `urls.py` dalam `project_django` dan `urls.py` dalam `todolist`

### Halaman Utama `todolist`
1. Membuat file `todolist.html` pada `templates`
2. Menambahkan seluruh url yang dibutuhkan untuk melakukan behaviour seperti Add Task, Update Task, dan Delete Task sudah ada di file tersebut
3. Menambahkan urls pada `urls.py`

### Halaman Form
1. Membuat file forms.py yang berfungsi untuk membuat form
2. Membuat file html `create_task.html` untuk memunculkan tabel form yang berisi tag `<form>..</form>`
3. Memastikan tag `{% csrf_token %}` sudah ada di dalam tag <form>
4. Menambahkan urls pada `urls.py`

### Deployment
Menambahkan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` pada Github `Action -> Secrets`

### Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
Akun 1: luluspbp

Password: aamiin12

![Bagan1](https://github.com/ramyanareswari/TUGAS-2-PBP/blob/main/todolist/Akun1.png)

Akun 2: pengenlulus

Password: lulussemuamatkulyu

![Bagan2](https://github.com/ramyanareswari/TUGAS-2-PBP/blob/main/todolist/Akun2.png)

# Tugas 5: Web Design dengan HTML, CSS, dan CSS Framework

## Jawaban Pertanyaan ✅
### 1. Apa perbedaan Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan masing-masing style?
1. Inline CSS digunakan untuk styling elemen HTML yang spesifik. Penerapan Inline CSS adalah dengan menambahkan atribut `style` ke setiap tag HTML  tanpa menggunakan selector.
Kelebihan: efektif untuk styling website single-page
Kekurangan: terlalu menghabiskan banyak waktu, sehingga kurang efektif untuk styling website dengan lebih dari satu page

2. Internal CSS. Penerapan Internal CSS yaitu dengan menambahkan tag <style> pada section `<head>`.
Kelebihan: efektif untuk styling website single-page
Kekurangan: karena code untuk style ditambahkan ke file HTML, maka waktu loading page website akan bertambah

3. External CSS adalah CSS file yang terpisah dari file HTML. File tersebut memiliki ekstensi `.css`. Penerapan External CSS yaitu menghubungkan file `.css` dengan file HTML, dengan cara menambahkan elemen `<link>` pada section `<head>`
Kelebihan:
a. Satu file `.css` dapat dihubungkan dengan beberapa file HTML
b. File HTML akan lebih rapi serta loading page website akan lebih cepat
Kekurangan:
a. Page website yang dibuat tidak akan ter-render dengan baik sebelum file CSS external diload

### 2. Jelaskan tag HTML5 yang kamu ketahui
1. `<p>` dan `</p>`. Tag tersebut merupakan tag untuk membuat paragraph
2. <title>. Tag tersebut berguna untuk menampilkan judul halaman website pada tab browser
3. <a>. Tag tersebut adalah tag anchor, yang berfungsi sebagai hyperlink untuk mengarahkan pengguna ke tempat lain seperti URL di luar website
4. <h1>, <h2>, <h3>, dst merupakan heading tags. Tag tersebut berfungsi untuk menampilkan heading dengan berbagai ukuran
5. <br> tag berfungsi untuk membuat line break
6. <html> tag berfungsi untuk membuat sebuah HTML document
7. <div> tag berfungsi untuk mengelompokkan elemen atau tag menjadi suatu grup berisi blok konten. Tag ini juga berfungsi mendefinisikan class dan ID pada CSS sehingga blok konten ini nantinya dapat distyling menggunakan external CSS
8.  <form> tag berfungsi untuk membuat sebuah form dari input pengguna

### 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui
CSS Selector digunakan untuk memilih elemen HTML yang akan diberikan style, berdasarkan elemen tags, id, kelas, attribute, dll.

Contoh CSS selector:
1. Element Selector

2. Class Selector

3. Id Selector

4. Type Selector, berfungsi untuk me

## Implementasi Kode
### 1. Kustomisasi templat untuk halaman `login`, `register`, `create_task`
1. Konfigurasi `base.html`
Sebelum bisa memanfaatkan Bootstrap, harus menghubungkan proyek yang dibuat dan framework Bootstrap dengan cara menambahkan CDN Bootstrap pada elemen `<head>` dan elemen `<body>` pada `base.html`. Pada aplikasi `todolist` ini juga menggunakan external CSS, sehingga harus menambahkan link file CSS pada elemen `<head>`. Selain itu, ditambahkan juga link font external agar font default Bootstrap dapat tertimpa. Implementasinya adalah sebagai berikut:
```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
  {% block meta %}
  {% endblock meta %}
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <link href='https://fonts.googleapis.com/css?family=Rubik' rel='stylesheet'>
</head>
```

2. Membuat Navbar
 

3. Halaman login
Agar navbar dapat muncul pada halaman login, 

4. Halaman registrasi


### 2. Kustomisasi templat halaman `todolist` dengan card

### 3. Membuat page maenjadi responsive
Webpage Todolist ini memanfaatkan framework Bootstrap agar tampilan menjadi responsive. 