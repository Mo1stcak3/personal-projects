import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAXknG66S4qOWyFuKo3xBezFaKZtI0tY4I')

loc = input("Where are you from? ")

try:
    results = gmaps.geocode(loc)
    if results:
        location = results[0]['geometry']['location']
        print(f"\n📍 Location: {loc}")
        print(f"🗺️ Latitude: {location['lat']}")
        print(f"🗺️ Longitude: {location['lng']}")
    else:
        print(" ⚠️ Location not found. Try a more specific name.")
except Exception as e:
    print("❌ Error retrieving location:", e)