import streamlit as st
import requests
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# OpenWeatherMap API Key (Get your own key from OpenWeatherMap)
api_key = "API_HERE"

# SQLite database connection
conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        Date TEXT,
        City TEXT,
        Temperature REAL,
        Humidity REAL
    )
''')
conn.commit()

# Streamlit web app
st.title('Weather App')

# Function to get weather data from OpenWeatherMap API for a given city and date
def get_weather_data(city, date):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&dt={date}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    if 'main' in data:
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        humidity = data['main']['humidity']
        return temperature_celsius, humidity
    else:
        st.error(f"Error fetching weather data for {city} on {date}. Response: {data}")
        return None, None

# Input form for adding weather data
city = st.text_input('Enter City:', 'London')
selected_date = st.date_input('Select Date:', pd.to_datetime('today'))

if st.button(f'Get Weather Data for {city} on {selected_date}'):
    formatted_date = selected_date.strftime('%Y-%m-%d')
    temperature, humidity = get_weather_data(city, formatted_date)
    st.success(f'{city} on {selected_date}: Temperature: {temperature}°C, Humidity: {humidity}%')

    # Insert the new weather data into the SQLite database
    cursor.execute('INSERT INTO weather (Date, City, Temperature, Humidity) VALUES (?, ?, ?, ?)', (formatted_date, city, temperature, humidity))
    conn.commit()
    st.success(f'{city} weather data added successfully!')

# Button to clear the database
if st.button('Clear Database'):
    cursor.execute('DELETE FROM weather')
    conn.commit()
    st.warning('Database cleared. All weather data deleted.')

# Retrieve weather data from the SQLite database
weather_data = pd.read_sql('SELECT * FROM weather', conn)

# Display the weather data
st.subheader('Weather Data')
st.dataframe(weather_data)

# Bar graph for Temperature by City
st.subheader('Temperature Trends by City')
fig, ax = plt.subplots()

for city, data in weather_data.groupby('City'):
    ax.bar(city, data['Temperature'].mean(), label=city)

ax.set(xlabel='City', ylabel='Average Temperature (°C)', title='Temperature Trends by City')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
st.pyplot(fig)

# Close the SQLite connection
conn.close()
