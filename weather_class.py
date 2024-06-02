from configparser import ConfigParser 
import requests 
import json
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image,ImageSequence
import math


#Converting the app into class for easier instantiation
config_file = "/Users/ceo/Desktop/Weather_App_Tkinter/config/config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = "https://api.openweathermap.org/data/2.5/weather"

#image for sun_rise
sun_rise_gif = "images_sun/1f305.gif"
image_list = [sun_rise_gif]

#Gif Movement Image class
class AnimateGIF(Label):
    def __init__(self, master, path, *args, **kwargs):
        Label.__init__(self,master, *args, **kwargs)
        self.path = path
        self._load_gif()
        self._animate()
    
    #Private functions
    def _load_gif(self):
        self.sequence = []
        self.current_frame = 0
        image = Image.open(self.path)
        for frame in ImageSequence.Iterator(image):
            self.sequence.append(ImageTk.PhotoImage(frame))
        self.config(image=self.sequence[0])

    def _animate(self):
        self.current_frame += 1
        if self.current_frame >= len(self.sequence):
            self.current_frame = 0
        self.config(image=self.sequence[self.current_frame])
        self.after(50, self._animate)


class WeatherApp():
    def __init__(self, master) -> None:
        self.master = master
        master.title("First Weather App")
        master.geometry("500x400")


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

        
        self.image_label = None

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
            if "Few clouds" in weather[4]:
                self.update_image(image_list[0])
            else:
                self.hide_image()
        else:
            messagebox.showerror("Error", "Cannot Find {}".format(city))


    def update_image(self, image_path):
        try:
            self.image_label = AnimateGIF(self.master, image_path)
            self.image_label.pack()
        except Exception as e:
            print(f"{image_path} not found in file")


    def hide_image(self):
        if self.image_label:
            self.image_label.pack_forget()
            self.image_label = None