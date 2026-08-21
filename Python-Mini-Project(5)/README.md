<div align="center">

# ☁️ PROJECT 5: "LIVE WEATHER CHECKER" IN PYTHON

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A real-time, zero-dependency command-line weather application in Python: demonstrates REST API integration, URL encoding (<code>urllib.parse</code>), HTTP networking (<code>urllib.request</code>), SSL context handling, nested JSON parsing, and WMO weather code translation without third-party libraries.</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🌐 1. Understanding the Two-Step API Architecture](#-1-understanding-the-two-step-api-architecture)
  - [Step 1: Geocoding (City Name ➔ GPS Coordinates)](#step-1-geocoding-city-name--gps-coordinates)
  - [Step 2: Weather Forecast (GPS Coordinates ➔ Live Data)](#step-2-weather-forecast-gps-coordinates--live-data)
- [🧠 2. Core Python Standard Libraries Used](#-2-core-python-standard-libraries-used)
  - [`urllib.request` (HTTP Requests)](#urllibrequest-http-requests)
  - [`urllib.parse.quote()` (URL Encoding)](#urllibparsequote-url-encoding)
  - [`json.loads()` (JSON Deserialization)](#jsonloads-json-deserialization)
  - [`ssl` (Certificate Contexts)](#ssl-certificate-contexts)
- [🔄 API Request Flowchart](#-api-request-flowchart)
- [🌦️ 3. WMO Weather Code Interpretation](#️-3-wmo-weather-code-interpretation)
- [💻 4. Code Implementations](#-4-code-implementations)
  - [Version 1: Standard Zero-Dependency CLI Script](#version-1-standard-zero-dependency-cli-script)
  - [Version 2: Enhanced Weather App with Conditions & Country Details](#version-2-enhanced-weather-app-with-conditions--country-details)
- [🛡️ 5. Error Handling & Edge Cases](#️-5-error-handling--edge-cases)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Project Overview

The **Live Weather Checker** queries public REST APIs to fetch real-time meteorological data for any city worldwide without requiring paid subscriptions or API keys.

It utilizes the open-access **Open-Meteo API** to retrieve:
- 🌡️ **Current Temperature** (°C / °F)
- 💨 **Wind Speed** (km/h)
- 🧭 **Geographic Coordinates** (Latitude, Longitude)
- ☀️ **Weather Conditions** (Clear, Cloudy, Rainy, Stormy)

---

## 🌐 1. Understanding the Two-Step API Architecture

Weather models operate on geographic grids rather than city strings. Therefore, the application executes a two-phase query pipeline:

```
                      ┌─────────────────────────────────┐
                      │    User Inputs City: "London"   │
                      └────────────────┬────────────────┘
                                       │
                                       ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │ PHASE 1: GEOCODING API                                                 │
  │ https://geocoding-api.open-meteo.com/v1/search?name=London&count=1    │
  │ ➔ Extracts: latitude: 51.5085, longitude: -0.1257                     │
  └────────────────────────────────────┬───────────────────────────────────┘
                                       │
                                       ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │ PHASE 2: WEATHER FORECAST API                                          │
  │ https://api.open-meteo.com/v1/forecast?latitude=51.50&longitude=-0.12  │
  │ ➔ Extracts: temperature: 18.5°C, windspeed: 12.4 km/h, weathercode: 3 │
  └────────────────────────────────────┬───────────────────────────────────┘
                                       │
                                       ▼
                      ┌─────────────────────────────────┐
                      │  Formatted Terminal Dashboard   │
                      └─────────────────────────────────┘
```

---

## 🧠 2. Core Python Standard Libraries Used

### `urllib.request` (HTTP Requests)
Connects to remote web servers and downloads raw network responses:

```python
import urllib.request

response = urllib.request.urlopen("https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true")
raw_bytes = response.read()
```

### `urllib.parse.quote()` (URL Encoding)
Converts special characters and spaces into valid URL query syntax (e.g. `"New York"` becomes `"New%20York"` or `"São Paulo"` becomes `"S%C3%A3o%20Paulo"`):

```python
import urllib.parse

safe_city = urllib.parse.quote("New York")
print(safe_city)  # Output: New%20York
```

### `json.loads()` (JSON Deserialization)
Parses the downloaded JSON string into native Python dictionaries and lists:

```python
import json

data = json.loads('{"temperature": 24.5, "windspeed": 10.2}')
print(data["temperature"])  # Output: 24.5
```

### `ssl` (Certificate Contexts)
Creates a secure SSL context for HTTPS requests, resolving local certificate path issues:

```python
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
```

---

## 🔄 API Request Flowchart

```
           ┌────────────────────────────┐
           │        Start Program       │
           └─────────────┬──────────────┘
                         │
                         ▼
           ┌────────────────────────────┐
           │     Enter City Name        │ ◄──────────┐
           └─────────────┬──────────────┘            │
                         │                           │
                         ▼                           │
           ┌────────────────────────────┐            │
           │  URL Encode City Name      │            │
           │  (urllib.parse.quote)      │            │
           └─────────────┬──────────────┘            │
                         │                           │
                         ▼                           │
           ┌────────────────────────────┐            │
           │  Request Geocoding API     │            │
           └─────────────┬──────────────┘            │
                         │                           │
                  City Found?                        │
                  ┌──────┴──────┐                    │
              Yes ▼          No ▼                    │
           ┌──────────┐  ┌──────────────────┐        │
           │ Extract  │  │ Display "City    │        │
           │ Lat/Lon  │  │ Not Found" Error │────────┤
           └────┬─────┘  └──────────────────┘        │
                │                                    │
                ▼                                    │
           ┌────────────────────────────┐            │
           │  Request Weather API       │            │
           └─────────────┬──────────────┘            │
                         │                           │
                         ▼                           │
           ┌────────────────────────────┐            │
           │ Parse JSON & Show Metrics  │            │
           │ (Temp, Wind, Conditions)   │            │
           └─────────────┬──────────────┘            │
                         │                           │
                         ▼                           │
           ┌────────────────────────────┐            │
           │ Check Another? (yes / no)  │            │
           └─────────────┬──────────────┘            │
                         │                           │
                   User says yes?                    │
                   ┌─────┴─────┐                     │
               Yes ▼        No ▼                     │
               (Loop)    ┌──────────┐                │
                         │ Exit App │                │
                         └──────────┘                │
```

---

## 🌦️ 3. WMO Weather Code Interpretation

The Open-Meteo API returns standard **WMO (World Meteorological Organization)** weather codes. Here is the mapping table:

| WMO Code | Weather Description | Emoji |
| :---: | :--- | :---: |
| `0` | Clear Sky | ☀️ |
| `1, 2, 3` | Mainly Clear, Partly Cloudy, Overcast | ⛅ |
| `45, 48` | Fog and Depositing Rime Fog | 🌫️ |
| `51, 53, 55` | Drizzle (Light, Moderate, Dense) | 🌦️ |
| `61, 63, 65` | Rain (Slight, Moderate, Heavy) | 🌧️ |
| `71, 73, 75` | Snow Fall (Slight, Moderate, Heavy) | ❄️ |
| `80, 81, 82` | Rain Showers | 🌧️ |
| `95, 96, 99` | Thunderstorm | ⛈️ |

---

## 💻 4. Code Implementations

### Version 1: Standard Zero-Dependency CLI Script

```python
"""
Simple Weather Checker — Built-in Standard Library
"""

import json
import ssl
import urllib.parse
import urllib.request

# SSL context configuration
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def simple_weather():
    print("=" * 45)
    print("☁️  WELCOME TO SIMPLE WEATHER CHECKER! ☀️")
    print("=" * 45)

    while True:
        city = input("\n🏙️  Enter a city name: ").strip()
        if not city:
            print("⚠️ Please enter a valid city name.")
            continue

        try:
            # STEP 1: Turn city name into GPS Coordinates
            safe_city = urllib.parse.quote(city)
            geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={safe_city}&count=1"

            geo_request = urllib.request.urlopen(geo_url, context=ctx)
            geo_data = json.loads(geo_request.read().decode('utf-8'))

            if 'results' not in geo_data or not geo_data['results']:
                print(f"❌ Could not find location '{city}'. Please check spelling.")
                continue

            # Extract latitude, longitude, and country
            lat = geo_data['results'][0]['latitude']
            lon = geo_data['results'][0]['longitude']
            country = geo_data['results'][0].get('country', 'Unknown')
            name = geo_data['results'][0].get('name', city)

            # STEP 2: Fetch weather for coordinates
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

            weather_request = urllib.request.urlopen(weather_url, context=ctx)
            weather_data = json.loads(weather_request.read().decode('utf-8'))

            current = weather_data['current_weather']
            temp = current['temperature']
            wind = current['windspeed']

            # STEP 3: Display results
            print("\n" + "-" * 35)
            print(f"📍 Location:    {name}, {country}")
            print(f"🌡️  Temperature: {temp}°C")
            print(f"💨 Wind Speed:  {wind} km/h")
            print("-" * 35)

        except Exception as e:
            print(f"\n❌ Network error or invalid request: {e}")

        # STEP 4: Loop continuation
        choice = input("\nDo you want to check another location? (yes/no): ").strip()
        if choice.lower() not in ['yes', 'y']:
            print("\n👋 Thanks for using Simple Weather. Goodbye!")
            break

if __name__ == "__main__":
    simple_weather()
```

---

### Version 2: Enhanced Weather App with Conditions & Country Details

```python
"""
Enhanced Weather Checker with WMO Condition Codes and Detailed Metrics
"""

import json
import ssl
import urllib.parse
import urllib.request

WMO_CODES = {
    0: ("Clear Sky", "☀️"),
    1: ("Mainly Clear", "🌤️"),
    2: ("Partly Cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Foggy", "🌫️"),
    48: ("Rime Fog", "🌫️"),
    51: ("Light Drizzle", "🌦️"),
    53: ("Moderate Drizzle", "🌦️"),
    55: ("Dense Drizzle", "🌧️"),
    61: ("Slight Rain", "🌧️"),
    63: ("Moderate Rain", "🌧️"),
    65: ("Heavy Rain", "🌧️"),
    71: ("Slight Snow", "🌨️"),
    73: ("Moderate Snow", "❄️"),
    75: ("Heavy Snow", "❄️"),
    80: ("Rain Showers", "🌦️"),
    95: ("Thunderstorm", "⛈️")
}

def get_weather_desc(code):
    return WMO_CODES.get(code, ("Unknown", "🌡️"))
```

---

## 🛡️ 5. Error Handling & Edge Cases

1. **Empty / Whitespace Input**:
   - Checked via `if not city: continue` to avoid sending blank API queries.
2. **City Not Found (`results` key missing)**:
   - Handled cleanly before attempting index access `geo_data['results'][0]`, preventing `KeyError` or `IndexError`.
3. **Special Characters & Spaces**:
   - `urllib.parse.quote()` guarantees valid query strings for inputs like `"San Francisco"`, `"New Delhi"`, or `"München"`.
4. **Network Outages**:
   - Wrapped inside `try...except` to catch connection failures without crashing the program.

---

## 🚀 How to Run

1. **Verify Python Installation**:
   ```bash
   python3 --version
   ```
2. **Execute Weather Checker**:
   ```bash
   python3 project5_weather_checker.py
   ```

---

## 📄 License

This repository is maintained for educational reference and Python mastery. Free to use, adapt, and share!

---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR - ADESH SRIVASTAVA(TANMAY)!

</div>