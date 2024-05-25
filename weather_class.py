from configparser import ConfigParser 
import requests 
import json
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import math


#Converting the app into class for easier instantiation
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = "https://api.openweathermap.org/data/2.5/weather"

#image for sun_rise
sun_rise_gif = "/Users/ceo/Desktop/Weather_App_Tkinter/images_sun/1f305.gif"


class WeatherApp():
    def __init__(self, master) -> None:
        self.master = master
        master.title("First Weather App")
        master.geometry("300x300")


        self.city_text = StringVar()
        self.city_entry = Entry(master, textvariable=self.city_text)
        self.city_entry.pack()

        self.search_btn = Button(master, text="Search Weather", width=12, command=self.search_city)
        self.search_btn.pack()

        self.location_lbl =  Label(master, text="Location", font={'bold', 20})
        self.location_lbl.pack()

        self.temperature_label = Label(master, text='')
        self.temperature_label.pack()

        self.weather_label = Label(master, text='')
        self.weather_label.pack()


        #Try to load and display the image
        try:
            self.open_image = Image.open(sun_rise_gif)
            self.img = ImageTk.PhotoImage(self.open_image)
            self.image_label = Label(master, image=self.img)
            self.image_label.pack()
        except Exception as e:
            print(f"{self.open_image} not found in file")

    def get_weather(self,city):
        params = {
            'q': city,
            'appid': api_key
        }

        result = requests.get(url, params=params)

        if result:
            json_response = result.json()
            print(json.dumps(json_response, indent=4))
            city = json_response['name']
            country = json_response['sys']['country']
            temp_kelvin = json_response['main']['temp']
            temp_fahrenheit = ((temp_kelvin - 273.15) * 9/5) + 32
            weather1 = json_response['weather'][0]['description']
            final = [city, country, temp_kelvin, math.floor(temp_fahrenheit), weather1.capitalize()]
            return final
        else:
            print("NOTHING WAS FOUND")
            return None

    def search_city(self):
        city = self.city_text.get()
        weather = self.get_weather(city)

        if weather:
            self.location_lbl['text'] = "{}, {}".format(weather[0], weather[1])
            self.temperature_label['text'] = str(weather[3]) + "° Fahrenheit"
            self.weather_label['text'] = weather[4]

        else:
            messagebox.showerror("Error", "Cannot Find {}".format(city))



if __name__ == "__main__":
    root = Tk()
    weather_app = WeatherApp(root)
    root.mainloop()
