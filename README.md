# 🌾 CropIQ
### Every Farmer Deserves a Data Scientist

CropIQ is an AI-powered WhatsApp chatbot that provides 
real-time climate risk alerts and personalized crop advice 
to Indian farmers in Marathi and English — completely free.

## 🚀 The Problem
- 15 crore Indian farmers lose ₹12,000 crore annually to climate shocks
- No early warning system exists for small farmers
- Most solutions require smartphones or apps farmers don't have
- No solution speaks to them in their local language

## ✅ Our Solution
Farmer simply sends a WhatsApp message:
Onion, Nashik
And instantly receives:
- ⚠️ Climate risk alert for their specific crop
- ✅ Exact action to take today
- 📅 Day by day advice for the week
- 💰 Money saving tips
- 🌐 All in Marathi + English

## ⚙️ How It Works
Farmer WhatsApps → Weather Fetched → AI Generates Advice → Reply in 10 seconds

## 🛠️ Tech Stack
- Python + Flask
- Twilio WhatsApp API
- Open-Meteo Weather API (Free)
- Groq AI + LLaMA 3.3 70B (Free)
- ngrok (Tunneling)

## 🗺️ Cities Covered
Nashik, Pune, Aurangabad, Nagpur, Solapur,
Kolhapur, Ahmednagar, Latur, Jalgaon, Satara

## 📦 Installation

### 1. Clone the repo
git clone https://github.com/yourusername/CropIQ.git
cd CropIQ

### 2. Install dependencies
pip install flask twilio requests python-dotenv

### 3. Create .env file
GROQ_API_KEY=your_groq_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886

### 4. Create stats.json
{"farmers": 0, "queries": 0, "cities": []}

### 5. Run the app
Terminal 1: python app.py
Terminal 2: python whatsapp.py
Terminal 3: .\ngrok.exe http 5001

## 🌐 Usage
1. Open dashboard: http://127.0.0.1:5000
2. Message +1 415 523 8886 on WhatsApp
3. Send: Hi
4. Then send: Onion, Nashik



## 👨‍💻 Team
CropIQ Team — Predict. Protect. Prosper.
