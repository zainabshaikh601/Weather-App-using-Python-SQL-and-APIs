# Weather-App-using-Python-SQL-and-APIs

## Overview
This Weather App allows users to fetch and visualize weather data for specific cities and dates. The app utilizes the OpenWeatherMap API to retrieve real-time weather information, and the data is stored in a SQLite database for historical tracking. Users can input a city and date to get the weather details, and the app provides visualization in the form of a bar graph depicting temperature trends by city.

## Features
- Fetch real-time weather data for a specific city and date.
- Store weather data in a SQLite database for historical tracking.
- Visualize temperature trends by city using a bar graph.

## Usage
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   streamlit run weather_app.py
   ```

3. Use the input form to fetch weather data for a city and date.
4. Visualize temperature trends by city in the bar graph.
5. Clear the database or fetch data for additional cities and dates.

## Files
- `weather_app.py`: Main application script.
- `weather_data.db`: SQLite database file to store weather data.
- `requirements.txt`: List of Python dependencies.

## Dependencies
- streamlit
- requests
- pandas
- sqlite3
- matplotlib

## API Key
Ensure you have a valid OpenWeatherMap API key. Replace `"API_HERE"` in the `weather_app.py` file with your actual API key.

## Notes
- Make sure to keep your API key secure and avoid sharing it publicly.
- This app is a basic example and can be extended with additional features and visualizations.
