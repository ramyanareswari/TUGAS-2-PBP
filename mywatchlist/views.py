# Create your views here.
from django.shortcuts import render
from mywatchlist.models import WatchListItem

def show_watchlist(request):
    watchlist_item = WatchListItem.objects.all()
    
    context = {
        'watchlist_item': watchlist_item,
        'name':  'RAMYA NARESWARI',
        'id': '2106751606'
    }

    return render(request, "watchlist.html", context)