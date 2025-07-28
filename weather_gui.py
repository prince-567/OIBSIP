#Prince
        # Task NO-4 Weather App (GUI Server)

import requests
from tkinter import *
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    api_key = "84d64cd5bd4fc37c42acaaad34d93bf5"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            result = f"Temperature: {temp}°C\nHumidity: {humidity}%\nCondition: {description.title()}"
            weather_output.config(text=result)
        else:
            messagebox.showerror("Error", "Location not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
win = Tk()
win.title("Weather App")
win.geometry("350x250")
win.configure(bg="#CCE5FF")

Label(win, text="Enter Location:", bg="#CCE5FF").pack(pady=10)
city_entry = Entry(win, width=50)
city_entry.pack(pady=5)

Button(win, text="Get Weather", command=get_weather).pack(pady=10)
weather_output = Label(win, text="", bg="#CCE5FF", font=("Helvetica", 12))
weather_output.pack(pady=10)

win.mainloop()
