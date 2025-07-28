#Prince 
#                Task-1 Voice Assistant
import speech_recognition as sr
import pywhatkit
import datetime
import webbrowser
import time
import requests

def speak(text):
    print(f"Assistant: {text}")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not get that.")
    except sr.RequestError:
        speak("Speech service error.")
    return ""

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key=65c0238fc7a64d9d98a142441252707&q={city}"
    response = requests.get(url)
    data = response.json()
    if "current" in data:
        temp = data["current"]["temp_c"]
        desc = data["current"]["condition"]["text"]
        return f"The weather in {city} is {desc} with {temp} degrees celsius."
    else:
        return "Sorry, I couldn't get the weather."


def set_reminder(seconds, message):
    speak(f"Reminder set. I will remind you in {seconds} seconds.")
    time.sleep(seconds)
    speak(f"Reminder: {message}")

def play_music():
    speak("What song should I play?")
    song = get_audio()
    if song:
        speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)
    else:
        speak("I did not catch the song name.")

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=dcdb92a7813c4d1d9031067f46026508"
    response = requests.get(url)
    data = response.json()
    print("News API response:", data)
    if data.get("articles"):
        speak("Here are the top headlines.")
        for i, article in enumerate(data["articles"][:2], start=1):
            title = article["title"]
            speak(f"Headline {i}: {title}")
    else:
        speak("Sorry, I could not fetch the news.")

def main():
    speak("Voice assistant activated.")
    while True:
        text = get_audio()
        if not text:
            continue
        if "hello" in text or "hi" in text:
            speak("Hello! How can I help you?")
        elif "time" in text:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}.")
        elif "date" in text:
            date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {date}.")
        elif "search" in text:
            speak("What should I search for?")
            query = get_audio()
            if query:
                url = f"https://www.google.com/search?q={query}"
                webbrowser.open(url)
                speak(f"Searching for {query} on Google.")
        elif "weather" in text:
            speak("Which city?")
            city = get_audio()
            if city:
                weather_info = get_weather(city)
                speak(weather_info)
        elif "remind me" in text:
            speak("What should I remind you about?")
            message = get_audio()
            speak("In how many seconds?")
            sec_text = get_audio()
            try:
                seconds = int(sec_text)
                set_reminder(seconds, message)
            except ValueError:
                speak("Sorry, I need a number of seconds.")
        elif "play music" in text:
            play_music()
        elif "news" in text:
            get_news()
        elif "exit" in text or "quit" in text:
            speak("Goodbye!")
            break
        else:
            speak("I don't understand that command.")

if __name__ == "__main__":
    main()
