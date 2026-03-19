import requests

def get_weather(latitude, longitude, city_name):
    url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "windspeed_10m_max"
        ],
        "timezone": "Asia/Kolkata",
        "forecast_days": 7
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    daily = data["daily"]
    summary = f"7-day forecast for {city_name}:\n"
    
    for i in range(7):
        summary += f"""
Day {i+1}: Max {daily['temperature_2m_max'][i]}°C, Min {daily['temperature_2m_min'][i]}°C, Rain {daily['precipitation_sum'][i]}mm, Wind {daily['windspeed_10m_max'][i]} km/h
        """
    
    return summary, daily


# City coordinates for Maharashtra
CITY_COORDS = {
    "nashik": (19.9975, 73.7898),
    "pune": (18.5204, 73.8567),
    "aurangabad": (19.8762, 75.3433),
    "solapur": (17.6599, 75.9064),
    "kolhapur": (16.7050, 74.2433),
    "nagpur": (21.1458, 79.0882),
    "ahmednagar": (19.0948, 74.7480),
    "latur": (18.4088, 76.5604),
    "jalgaon": (21.0077, 75.5626),
    "satara": (17.6805, 74.0183),
}

def get_coords(city):
    city = city.lower().strip()
    if city in CITY_COORDS:
        return CITY_COORDS[city]
    # Default to Pune if city not found
    return CITY_COORDS["pune"]


# Test
if __name__ == "__main__":
    lat, lon = get_coords("nashik")
    summary, raw = get_weather(lat, lon, "Nashik")
    print(summary)