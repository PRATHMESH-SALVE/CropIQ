from flask import Flask, render_template, request, jsonify
from weather import get_weather, get_coords
from ai_advisor import get_crop_advice
import json

app = Flask(__name__)

# ─── Stats Functions ───────────────────────────
def load_stats():
    try:
        with open("stats.json", "r") as f:
            return json.load(f)
    except:
        return {"farmers": 0, "queries": 0, "cities": []}

def save_stats(stats):
    with open("stats.json", "w") as f:
        json.dump(stats, f)

# ─── Dashboard ─────────────────────────────────
@app.route("/")
def dashboard():
    stats = load_stats()
    return render_template("dashboard.html",
        farmers=stats["farmers"],
        queries=stats["queries"],
        cities=len(stats["cities"])
    )

# ─── Advice API ────────────────────────────────
@app.route("/advice")
def advice():
    crop = request.args.get("crop", "Onion")
    city = request.args.get("city", "Pune")

    lat, lon = get_coords(city)
    weather_summary, _ = get_weather(lat, lon, city)
    result = get_crop_advice(crop, city, weather_summary)

    # Update shared stats
    stats = load_stats()
    stats["queries"] += 1
    stats["farmers"] += 1
    if city not in stats["cities"]:
        stats["cities"].append(city)
    save_stats(stats)

    return jsonify({"advice": result})

# ─── Stats API (for live refresh) ──────────────
@app.route("/stats")
def get_stats():
    stats = load_stats()
    return jsonify({
        "farmers": stats["farmers"],
        "queries": stats["queries"],
        "cities": len(stats["cities"])
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)