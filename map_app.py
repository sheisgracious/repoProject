import requests
import json
import googlemaps

key = 'AIzaSyCzMX7Dl4ks60vKUms_pQj5EYjBhyYfj4E'
AUTH_URL = 'https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix'
payload = {
  "origin":{
    "location":{
      "latLng":{
        "latitude": 37.419734,
        "longitude": -122.0827784
      }
    }
  },
  "destination":{
    "location":{
      "latLng":{
        "latitude": 37.417670,
        "longitude": -122.079595
      }
    }
  },
  "travelMode": "DRIVE",
  "routingPreference": "TRAFFIC_AWARE",
  "departureTime": "2023-10-15T15:01:23.045123456Z",
  "computeAlternativeRoutes": False,
  "routeModifiers": {
    "avoidTolls": False,
    "avoidHighways": False,
    "avoidFerries": False
  },
  "languageCode": "en-US",
  "units": "IMPERIAL"
}

headers = {
  'Content-Type': 'application/json',
  'X-Goog-Api-Key': key,
  'X-Goog-FieldMask': 'routes.duration, routes.distanceMeters, routes.polyline.encodedPolyline'
}

auth_response = requests.post(AUTH_URL, headers=headers, data=json.dumps(payload))


# r = requests.get()


print(auth_response)

