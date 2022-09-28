# Tugas 3: Data Delivery Menggunakan Django

## Ramya Nareswari Wikantiyoso (2106751606)

## Link Aplikasi 🔗
https://tugaspbp.herokuapp.com/todolist

## Jawaban Pertanyaan ✅
Pada urls.py di dalam project_django, saya tambahkan path('todolist/', include('todolist.urls')). Hal ini bertujuan untuk memberikan route pada aplikasi todolist sehingga browser bisa mengaksesnya melalui /todolist. Setelah itu, pada urls.py milik todolist app, saya tambahkan app_name berupa 'todolist' dan saya tambahkan list urlpatterns berisi path('', show_todo, name='show_todo') sehingga ketika browser mengunjungi path /todolist, fungsi show_todo akan dipanggil.