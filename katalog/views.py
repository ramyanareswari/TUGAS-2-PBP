from gettext import Catalog
from django.shortcuts import render
from katalog.models import CatalogItem

# Sebuah fungsi yang menerima parameter request dan mengembalikan render(request, "katalog.html")
def show_catalog(request):
    catalog_data = CatalogItem.objects.all()
    # name_header = Name.objects.all()
    
    context = {
        'list_data': catalog_data,
        'nama':  'Ramya Nareswari',
        'id': '2106751606'
    }

    return render(request, "katalog.html", context)