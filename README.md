# Weather Notification Service

This Python script provides weather forecasts and sends SMS notifications if rain is expected. It uses the OpenWeatherMap API for weather data and Twilio for SMS notifications.

## Features
- Fetches a 4-hour weather forecast for a given latitude and longitude.
- Checks for rain in the forecast.
- Sends a text message alert if rain is expected.

## Prerequisites
Before running the script, ensure you have the following:

- **Python** (version 3.x)
- **Twilio Account SID** and **Auth Token** for sending SMS messages
- **OpenWeatherMap API Key** for fetching weather data

### Python Libraries
- `requests` for making HTTP requests.
- `twilio` for sending SMS messages.

You can install the required libraries by running:

```bash
pip install requests twilio
