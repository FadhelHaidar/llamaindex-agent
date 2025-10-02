from math import radians, sin, cos, sqrt, atan2
from llama_index.core.tools import FunctionTool
from src.utils import GAZETTEER

# --- Tool 1: Geocode ---
def local_geocode(city: str) -> dict:
    key = city.strip().lower()
    if key not in GAZETTEER:
        return {"error": f"City '{city}' not found. Try: {', '.join(sorted(GAZETTEER))}"}
    info = GAZETTEER[key]
    return {"city": city.title(), "country": info["country"], "lat": info["lat"], "lon": info["lon"]}

geocode_tool = FunctionTool.from_defaults(
    fn=local_geocode,
    name="local_geocode",
    description="Offline geocoder. Input: city (string). Returns lat/lon and country."
)

# --- Tool 2: Weather simulator ---
def weather_sim(city: str) -> str:
    g = local_geocode(city)
    if "error" in g: 
        return g["error"]
    lat = abs(g["lat"])
    base = 30 - (lat / 90) * 30   # hotter at equator, colder at poles
    tmax = round(base + 2, 1)
    tmin = round(base - 2, 1)
    return f"Weather in {g['city']}, {g['country']}: {tmin}°C–{tmax}°C (simulated)."

weather_tool = FunctionTool.from_defaults(
    fn=weather_sim,
    name="weather_sim",
    description="Offline weather simulation. Input: city (string). Output: min/max °C."
)

# --- Tool 3: Distance in km ---
def distance_km(city_a: str, city_b: str) -> str:
    a = local_geocode(city_a)
    b = local_geocode(city_b)
    if "error" in a: 
        return a["error"]
    if "error" in b: 
        return b["error"]

    R = 6371.0
    lat1, lon1 = radians(a["lat"]), radians(a["lon"])
    lat2, lon2 = radians(b["lat"]), radians(b["lon"])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    h = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    d = 2 * R * atan2(sqrt(h), sqrt(1 - h))
    return f"Distance {a['city']} ↔ {b['city']}: {round(d, 1)} km."

distance_tool = FunctionTool.from_defaults(
    fn=distance_km,
    name="distance_km",
    description="Great-circle distance between two cities in km."
)

# Export all tools
TOOLS = [geocode_tool, weather_tool, distance_tool]