from configparser import ConfigParser 
import requests 
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = f"https://api.openweathermap.org/data/2.5/weather"


#Day images
sun_rise_gif = "/Users/ceo/Desktop/Weather_App_Tkinter/images_sun/1f305.gif"
try:
    open_image = Image.open(sun_rise_gif)
    img = ImageTk.PhotoImage(open_image)
except Exception as e:
    print(f"Error loading image: {e}")
    img = None

#Getting the weather info in given city
def get_weather(city):

    params = {
        'q': city,
        'appid': api_key
    }

    result = requests.get(url, params=params)
    
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        weather1 = json['weather'][0]['main']
        final =  [city, country, temp_kelvin, temp_celsius, weather1]
        return final
    else:
        print("NOTHING WAS FOUND")



#Search for the city 
def search_city():
    city = city_text.get()
    weather = get_weather(city)

    if weather:
        location_lbl['text'] = '{} , {}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3])+ " Degree Celsius"
        weather_label['text'] = weather[4]

    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


#instantiating the TK class 
app = Tk()

#title of the app
app.title("First Weather App")

#adjusting the width and height of the app
app.geometry("300x300")

#add labels, buttons and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text="Search Weather", width=12, command=search_city)
search_btn.pack()

location_lbl =  Label(app, text="Location", font={'bold', 20})
location_lbl.pack()

temperature_label = Label(app, text='')
temperature_label.pack()

weather_label = Label(app, text='')
weather_label.pack()


if img:
    image_label = Label(app, image=img)
    image_label.image = img  # Keep a reference to the image
    image_label.pack()


app.mainloop()

