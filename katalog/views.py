from gettext import Catalog
from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(request):
    catalog_data = CatalogItem.objects.all()
    
    context = {
        'list_data': catalog_data,
        'name':  'RAMYA NARESWARI',
        'id': '2106751606'
    }

    return render(request, "katalog.html", context)