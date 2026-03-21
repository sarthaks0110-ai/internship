import streamlit as st
import requests

# ---------------- CONFIG ----------------
API_KEY = "Your_API_here"  # Replace this
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# ---------------- FUNCTION ----------------
def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            st.error("❌ Invalid API Key. Please check your key or wait for activation.")
        else:
            st.error(response.json())  # shows real error
            return None
    except Exception as e:
        st.error(f"Error: {e}")
        return None


# ---------------- UI ----------------
st.set_page_config(page_title="Weather App", layout="centered")

st.title("🌤 Real-Time Weather App")
st.write("Enter a city name to get current weather data")

city = st.text_input("🏙 Enter City Name")

if st.button("Get Weather"):
    if city.strip() == "":
        st.warning("⚠ Please enter a city name")
    else:
        data = get_weather(city)

        if data:
            st.subheader(f"📍 {data['name']}, {data['sys']['country']}")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("🌡 Temperature", f"{data['main']['temp']} °C")

            with col2:
                st.metric("💧 Humidity", f"{data['main']['humidity']}%")

            with col3:
                st.metric("🌬 Wind Speed", f"{data['wind']['speed']} m/s")

            st.write(f"☁ Condition: {data['weather'][0]['description'].title()}")

        else:
            st.error("❌ City not found or API issue")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built with using Streamlit")
