import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_crop_advice(crop, location, weather_summary):
    prompt = f"""
    You are CropIQ, an expert agricultural AI advisor for Indian farmers.
    
    Farmer Details:
    - Crop: {crop}
    - Location: {location}
    - Weather Forecast: {weather_summary}
    
    Give advice in simple English AND Marathi.
    Format your response as:
    
    🌾 CROP ALERT for {crop} farmer in {location}:
    
    ⚠️ Risk: [what climate risk they face]
    ✅ Action: [exactly what to do today]
    📅 This Week: [day by day simple tips]
    💰 Money Tip: [how to save cost or avoid loss]
    
    Keep it short, practical, and friendly.
    """

    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=body
    )

    result = response.json()
    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        print("Groq Error:", result)
        return "Error getting advice. Check your API key."

# Test
if __name__ == "__main__":
    advice = get_crop_advice(
        crop="Onion",
        location="Nashik, Maharashtra",
        weather_summary="Heavy rain expected in 2 days, temperature dropping to 12°C"
    )
    print(advice)