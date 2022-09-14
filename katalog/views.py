from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(request):
    catalog_item = CatalogItem.objects.all()
    
    context = {
        'catalog_data': catalog_item,
        'name':  'RAMYA NARESWARI',
        'id': '2106751606'
    }

    return render(request, "katalog.html", context)