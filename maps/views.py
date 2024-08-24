
from django.shortcuts import render
import folium

def show_map(request):

    mapObj = folium.Map(location=[23.8316896,90.4120205],zoom_start=14)

    map_html = mapObj._repr_html_()

    return render(request, 'maps/map.html', {'map': map_html, 'location_info': 'Nikunj 1, Joar Sahara, Dhaka, Dhaka Metropolitan, Dhaka District, Dhaka Division, 1229, Bangladesh'})
