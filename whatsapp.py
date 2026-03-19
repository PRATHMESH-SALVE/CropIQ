from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from weather import get_weather, get_coords
from ai_advisor import get_crop_advice
import json

app = Flask(__name__)

farmer_sessions = {}

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

# ─── WhatsApp Bot ───────────────────────────────
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip()
    sender = request.values.get("From", "")

    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg.lower() in ["hi", "hello", "start", "help"]:
        reply = """🌾 *Welcome to CropIQ!*
_Every Farmer Deserves a Data Scientist_

Reply with your crop and city:
*CROP, CITY*

Example:
*Onion, Nashik*
*Sugarcane, Pune*
*Soybean, Aurangabad*"""

    elif "," in incoming_msg:
        parts = incoming_msg.split(",")
        crop = parts[0].strip().title()
        city = parts[1].strip().title()

        farmer_sessions[sender] = {"crop": crop, "city": city}

        lat, lon = get_coords(city)
        weather_summary, _ = get_weather(lat, lon, city)
        reply = get_crop_advice(crop, city, weather_summary)
        reply += "\n\n_Reply MORE for insurance tips or NEW for another crop_"

        # Update shared stats
        stats = load_stats()
        stats["queries"] += 1
        stats["farmers"] += 1
        if city not in stats["cities"]:
            stats["cities"].append(city)
        save_stats(stats)

    elif incoming_msg.lower() == "more":
        if sender in farmer_sessions:
            session = farmer_sessions[sender]
            reply = get_crop_advice(
                session["crop"],
                session["city"],
                "Focus on insurance and financial protection tips"
            )
            # Update stats
            stats = load_stats()
            stats["queries"] += 1
            save_stats(stats)
        else:
            reply = "Please start by sending: CROP, CITY\nExample: Onion, Nashik"

    elif incoming_msg.lower() == "new":
        if sender in farmer_sessions:
            del farmer_sessions[sender]
        reply = "Send your new crop details:\nFormat: CROP, CITY\nExample: Tomato, Pune"

    else:
        reply = """❓ I didn't understand that.

Send your crop and city like:
*Onion, Nashik*

Or type *HELP* to start over."""

    msg.body(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5001)