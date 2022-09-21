# Create your views here.
from django.core import serializers
from django.http import HttpResponse, request
from django.shortcuts import render
from mywatchlist.models import WatchListItem

def show_watchlist(request):
    watchlist_item = WatchListItem.objects.all()
    
    context = {
        'watchlist_item': watchlist_item,
        'name':  'RAMYA NARESWARI',
        'id': '2106751606',
    }

    return render(request, "watchlist.html", context)

def show_html(request):
    data = WatchListItem.objects.all()
    # Display message
    watched_count = data.filter(watched=True).count()
    unwatched_count = data.filter(watched=False).count()

    if watched_count > unwatched_count:
        message = "Selamat, kamu sudah banyak menonton!"

    else:
        message = "Wah, kamu masih sedikit menonton!"

    context = {
        'watchlist_item': data,
        'name':  'RAMYA NARESWARI',
        'id': '2106751606',
        'message': message
    }
    return render(request, "watchlist.html", context)

def show_xml(request):
    data = WatchListItem.objects.all()
    
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json(request):
    data = WatchListItem.objects.all()
    
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_json_id(request, id):
    data = WatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_id(request, id):
    data = WatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")