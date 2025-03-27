# Voice Activated Personal Assistant
This is a simple personal assistant built using Python. It can perform tasks like fetching weather information, reading the latest news, setting reminders, and more. The assistant interacts with you through voice commands using speech recognition and responds using text-to-speech (TTS).

## Features:
**Weather Information**: Fetch current weather data based on a city name.

**News**: Get the latest news headlines.

**Reminders**: Set a reminder with a specific task at a given time.

**Voice Commands**: The assistant listens to your voice commands and responds accordingly.

## Requirements:
*Python 3.x*

*pyttsx3* - Text-to-speech conversion library.

*speech_recognition* - For recognizing speech input.

*requests* - For fetching weather and news data.

*schedule* - For scheduling reminders.

You can install the required libraries using pip:

```
bash
pip install pyttsx3 speechrecognition requests schedule
```

## Setup:
**Get API Keys**:

For weather data, sign up at OpenWeatherMap to get an API key.

For news data, sign up at NewsAPI to get an API key.

**Update API Keys**:

Replace the weather_api_key and news_api_key in the script with your API keys.

```
python

weather_api_key = "YOUR_OPENWEATHERMAP_API_KEY"
news_api_key = "YOUR_NEWSAPI_API_KEY"
```

## How to Use:
Run the script by executing python `personal_assistant.py` in the terminal.

The assistant will greet you and ask how it can help you.

You can ask the assistant to perform different tasks:

*Weather*: Ask for the weather of a specific city.

*News*: Ask for the latest news.

*Reminder*: Set a reminder with a task and time.

*Exit*: Close the assistant.

## How it Works:
**Speech Recognition**: The assistant listens to your voice command and processes it using the Google Speech Recognition API.

**Text-to-Speech**: After processing the command, the assistant responds using pyttsx3, which converts text responses to speech.

**Weather**: Fetches the weather using the OpenWeatherMap API and gives you a summary.

**News**: Retrieves the latest news headlines from the NewsAPI.

**Reminder**: Sets a daily reminder using the schedule library.

## Notes:
This assistant works in a loop, so it will keep listening for new commands unless you exit it manually.

Make sure your microphone is working properly for voice recognition to work effectively.

## Future Improvements:
Integrate more services like setting alarms, sending emails, etc.

Add more advanced natural language processing for more complex commands.

Implement a GUI for user interaction.
