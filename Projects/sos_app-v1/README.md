# 🚨 SOS App v1 — by Rey Moises Sebastian

**A GUI-based emergency locator built with Python and CustomTkinter, powered by Google Maps API.**

This app helps users instantly find nearby hospitals, police stations, and fire stations—with a bold reminder to call 911 when it matters most. I built this to practice clean backend logic, real-world API integration, and GUI polish. No vibe coding — just working code.

---

## 🧠 Why I Made This
I’m a backend-focused IT student expanding into GUI development. I wanted to build something useful, clean, and technically honest. This app is my first public release that blends API logic with a user-friendly interface — and it works.

---

## 🖼️ Preview

**Initial Interface** ![Initial Interface](sos_app-v1/Preview/ui_1.png)

**Hospital Results Example** ![Hospital Results](sos_app-v1/Preview/ui_2(results).png)

---

## ⚙️ Features
* **🔴 Emergency Alert** – Bold 911 reminder at the top.
* **🏥 Nearby Hospitals** – Auto-detected and listed by proximity.
* **👮 Nearby Police Stations** – Pulled directly from Google Places.
* **🚒 Nearby Fire Stations** – Text search for local results.
* **🧭 Live Location Detection** – Powered by Google Geolocation API.
* **🧊 Clean GUI** – Built with CustomTkinter, light theme, and Helvetica font.

---

## 📦 Tech Stack
* **Python 3.10+**
* **CustomTkinter** – Modern styling and layout.
* **Google Maps API** – Places and Geolocation services.
* **Requests** – For handling HTTP calls.
* **Googlemaps SDK** – Optional for expanded functionality.

---

📂 Project Structure
sos_app v1/
│
├── sos_app.py        # Main GUI application  
├── services.py       # Google Maps API wrapper  
├── requirements.txt  # Dependencies  
├── Preview/          # Screenshots for README  
└── README.md         # Documentation  

---

🚀 How to Run

1. Clone the Repository
git clone https://github.com/yourusername/sos-app.git
cd sos-app


2. Install Dependencies
pip install -r requirements.txt


3. Configure API Key
Open services.py and replace the placeholder with your valid API key:
# In services.py
self.gmaps_key = "YOUR_API_KEY_HERE"


4. Run the Application
python sos_app.py

---

📌 Requirements
Ensure you have the following versions installed:
python >= 3.10
customtkinter == 5.2.1
requests == 2.31.0
googlemaps == 4.10.0

---

🛠️ Future Plans (v2+)
- [ ] Add icons and section styling for better visual hierarchy
- [ ] Export results to PDF or text file
- [ ] Add filters (e.g. ER availability, "Open Now")
- [ ] Improve error handling and fallback messages
- [ ] Add more service types (pharmacies, ambulance, etc.)

---

⚠️ Disclaimer
This app is for educational and demonstration purposes only.
While the app uses real-world data, it should not be relied upon in life-threatening situations.
Always dial your local emergency number (e.g., 911) in case of real danger.

---

Created by Rey Moises Sebastian
