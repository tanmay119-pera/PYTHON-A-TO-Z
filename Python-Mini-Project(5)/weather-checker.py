'''                             PYTHON-MINI-PROJECT-5 "WEATHER CHECKER"                               '''

import urllib.request # This is a built-in Python library that allows you to make HTTP requests to retrieve data from the web.
import urllib.parse # This library is used to handle URL encoding and decoding, which is necessary when dealing with user input that may contain special characters.
import json # This library is used to parse JSON data, which is the format in which the weather API returns its data.
import ssl # This library is used to handle SSL certificates, which are necessary for secure HTTPS connections. The code below disables SSL certificate verification to avoid issues with self-signed certificates or other SSL-related problems.

# SSL fix so your computer doesn't block the connection

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("☁️  Welcome to Simple Weather! ☀️")

# The 'while True' loop keeps the program running until we tell it to 'break'
while True:
    city = input("\n🏙️Enter a city name: ")

    try:
        # STEP 1: Turn the city name into GPS Coordinates
        safe_city = urllib.parse.quote(city)
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={safe_city}&count=1"
        
        geo_request = urllib.request.urlopen(geo_url, context=ctx)
        geo_data = json.loads(geo_request.read())
        
        # Pull out the exact GPS numbers
        lat = geo_data['results'][0]['latitude']
        lon = geo_data['results'][0]['longitude']
        
        # STEP 2: Use those GPS numbers to find the weather
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        
        weather_request = urllib.request.urlopen(weather_url, context=ctx)
        weather_data = json.loads(weather_request.read())
        
        # Pull out the temperature and wind
        temp = weather_data['current_weather']['temperature']
        wind = weather_data['current_weather']['windspeed']
        
        # STEP 3: Print the results!
        print(f"\n✨ Results for {city.title()}:")
        print(f"🌡️  Temperature: {temp}°C")
        print(f"💨 Wind Speed: {wind} km/h")

    except Exception as e:
        print("\n❌ Oops! Could not find that city. Please try again.")

    # STEP 4: Ask the user what they want to do next
    print("\n--------------------------")
    choice = input("Do you want to check another location? (yes/no): ")
    
    # If they type anything other than 'yes' or 'y', we break the loop and end the program
    if choice.lower() not in ['yes', 'y']:
        print("👋Thanks for using Simple Weather. Goodbye!")
        break  # This is the command that stops the 'while True' loop