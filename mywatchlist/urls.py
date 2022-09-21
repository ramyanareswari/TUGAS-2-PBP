# Implementasi routing terhadap views.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mywatchlist.views import show_watchlist, show_html, show_xml, show_json, show_xml_id, show_json_id


app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>', show_xml_id, name='show_xml_id'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_id, name='show_json_id'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)