import speech_recognition as sr
import pyttsx3
import requests
import datetime
import time
import schedule

# personal_assistant initialization
personal_assistant = pyttsx3.init()


# speak function
def pa_speak(text):
    personal_assistant.say(text)
    personal_assistant.runAndWait()


# listen function
def pa_listen():
    pa_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        pa_audio = pa_recognizer.listen(source)

    try:
        pa_command = pa_recognizer.recognize_google(pa_audio)
        print(f"Command: {pa_command}")
        return pa_command.lower()

    except sr.UnknownValueError:
        pa_speak("Sorry, I did not get you. Please repeat.")
        return None
    except sr.RequestError:
        pa_speak("Sorry, there was an error with the speech recognition.")
        return None


# weather function
def pa_weather(p_city):
    weather_api_key = "write-your-api-key"
    weather_city = p_city
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={weather_city}&appid={weather_api_key}&units=metric"

    weather_response = requests.get(weather_url)
    data = weather_response.json()

    if data["cod"] == 200:
        weather_main = data["main"]
        weather_description = data["weather"][0]["description"]
        temp = weather_main["temp"]
        pa_speak(f"The current weather is {weather_description} with a temperature of {temp} degrees Celsius.")
    else:
        pa_speak("Sorry, I am unable to get the weather at this moment.")


# news function
def pa_news():
    news_api_key = "write-your-api-key"
    news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"

    news_response = requests.get(news_url)
    data = news_response.json()

    if data["status"] == "ok":
        news_articles = data["articles"][:5]  # Get top 5 articles
        for news_article in news_articles:
            pa_speak(f"Source: {news_article['source']['name']}")
            pa_speak(f"Title: {news_article['title']}")
            pa_speak(f"Description: {news_article['description']}")
    else:
        pa_speak("Sorry, I am unable to get the news at this moment.")


# reminder function
def pa_reminder():
    pa_speak("What would you like me to remind you about?")
    reminder_task = pa_listen()

    if reminder_task:
        pa_speak("At what time would you like me to set the reminder? Please say the time in 'hour:minute' format.")
        reminder_time_str = pa_listen()

        if reminder_time_str:
            try:
                reminder_time = datetime.datetime.strptime(reminder_time_str, "%H:%M").time()
                schedule.every().day.at(str(reminder_time)).do(pa_speak, f"Reminder: {reminder_task}")
                pa_speak(f"Reminder set for {reminder_task} at {reminder_time_str}.")
            except ValueError:
                pa_speak("Sorry, I am unable to understand the time format. Please try again.")
        else:
            pa_speak("I am unable to understand the time.")
    else:
        pa_speak("I am unable to hear the task. Please try again.")


# Main function
def main():
    pa_speak("Hello, how can I help you today?")

    while True:
        command = pa_listen()

        if command:
            if "weather" in command:
                pa_speak("Please mention the city name.")
                command1 = pa_listen()
                pa_weather(command1)
            elif "news" in command:
                pa_news()
            elif "reminder" in command:
                pa_reminder()
            elif "exit" in command or "quit" in command:
                pa_speak("Goodbye! Have a nice day")
                break
            else:
                pa_speak("Sorry, I am unable to understand that command. Please try again.")

        time.sleep(1)


if __name__ == "__main__":
    main()
