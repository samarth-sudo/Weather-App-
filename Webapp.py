from flask import Flask, render_template
import requests

app = Flask(__name__)

# Set your ThingSpeak API key and channel ID here
API_KEY = "XQ9G79JHN6FJCCE9"
CHANNEL_ID = "2051273"

# URL to retrieve the latest weather data from ThingSpeak
URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds/last.json?api_key={API_KEY}"

@app.route("/")
def index():
    # Retrieve the latest weather data from ThingSpeak
    response = requests.get(URL)
    data = response.json()

    # Extract the relevant data from the response
    Datapacket = data["field1"]
    Temperature = data["field2"]
    Humidity = data["field3"]
    Pressure = data["field4"]
    RSSI = data["field5"]

    # Render the landing page with the weather data
    return render_template("index.html", Datapacket=Datapacket, Temperature=Temperature, Humidity=Humidity, Pressure=Pressure, RSSI=RSSI)

if __name__ == "__main__":
    app.run(debug=True)
