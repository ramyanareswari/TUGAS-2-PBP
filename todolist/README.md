# Tugas 3: Implementasi Form dan Autentikasi

## Ramya Nareswari Wikantiyoso (2106751606)

## Link Aplikasi 🔗
https://tugaspbp.herokuapp.com/todolist

## Jawaban Pertanyaan ✅


## Implementasi Kode

### Membuat Aplikasi Baru
`py manage.py startapp todolist`

### Routing
Menambahkan path('todolist/', include('todolist.urls')) pada urls.py di dalam project_django untuk memberikan route pada aplikasi todolist, sehingga app bisa diakses melalui browser di /todolist. 

Setelah itu, , menambahkan app_name berupa 'todolist' pada urls.py milik todolist app dan list urlpatterns berisi path('', show_todo, name='show_todo'), sehingga ketika browser mengunjungi path /todolist, fungsi show_todo akan dipanggil.

## Menambahkan mekanisme registrasi, login, dan logout

## Halaman Utama todolist

## Halaman Form