Weather App:

A clean, glassmorphism-styled weather app built with Flask and the Open-Meteo API.
Search any city and get real-time weather data — actual local time, temperature, and conditions — all served from a lightweight Python backend.
    🔗 Live Demo: https://weather-app-python-1-qxlt.onrender.com/
Note: hosted on Render's free tier, so the first request after inactivity may take 30–50 seconds to wake up.

Features:
-Search weather by city name
-Shows the searched city's actual local time (not server time)
-Current temperature & conditions
-Glassmorphism UI designed on figma

Backend: Flask (Python)
Weather Data: Open-Meteo API (Geocoding + Forecast endpoints)
Frontend: HTML, CSS (glassmorphism design)
Deployment: Render (via Gunicorn)
Version Control: Git & GitHub
search page - <img width="944" height="434" alt="image" src="https://github.com/user-attachments/assets/99c7d4a0-3198-4d5e-adaa-9a297855adb4" />
Result page - <img width="937" height="430" alt="image" src="https://github.com/user-attachments/assets/ce753204-ad41-4be5-83cd-e19369e6c13d" />

Run Locally:
git clone https://github.com/Jananivasudev/weather_app_python.git
cd weather_app_python
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run

What I Learned:
datetime.now() gives server time, not the searched city's time — fixed by passing timezone=auto to Open-Meteo, which returns the correct local time directly.
Flask error-handling routes need consistent return types across all branches.
Debugged a request.method == 'POST' logic issue in form handling.

⭐ If you found this project useful or interesting, feel free to star the repo — and any feedback is welcome!
