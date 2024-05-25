from tkinter import Tk  # Import Tk from tkinter
from weather_class import WeatherApp  # Import the WeatherApp class


if __name__ == "__main__":
    root = Tk()  
    app = WeatherApp(root) 
    root.mainloop() 