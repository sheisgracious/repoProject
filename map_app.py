import requests
import json
import googlemaps
import os
import pprint

AUTH_URL = 'https://maps.googleapis.com/maps/'\
          'api/timezone/json?location=39.6034810%'\
          '2C-119.6822510&timestamp=1331161200&key=?'\

# headers = {
#   'Content-Type': 'application/json',
#   'X-Goog-Api-Key': key,
#   'X-Goog-FieldMask': 'routes.duration,
#                     routes.distanceMeters, 
#                     routes.polyline.encodedPolyline'
# }

auth_response = requests.get(AUTH_URL)
# r = requests.get()
pprint.pprint(auth_response.json())
