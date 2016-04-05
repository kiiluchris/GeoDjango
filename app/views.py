from django.shortcuts import render

# Create your views here.
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyD0MSmH6-nAgxIeJhO_SBiNjrbKyPHhQ9k')
# def home(request):
# 	# Look up an address with reverse geocoding
# 	reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
# 	# Geocoding an address
# 	geocode_result1 = gmaps.geocode('Korogocho, Kenya')[0]['geometry']['location']['lat']
# 	geocode_result2 = gmaps.geocode('Korogocho, Kenya')[0]['geometry']['location']['lng']

# 	# Request directions via public transit
# 	now = datetime.now()
# 	directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
# 	context = {
# 		"reverse":geocode_result1,
# 		"reverse2":geocode_result2,
# 	}
# 	return render(request, "home.html", context)

def home(request):
	return render(request, "home.html", {"dj":"dj"})
