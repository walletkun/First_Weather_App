from tkinter import Tk  # Import Tk from tkinter
from weather_class import WeatherApp, AnimateGIF# Import the WeatherApp class

if __name__ == "__main__":
    root = Tk()  
    app = WeatherApp(root) 
    root.mainloop() 
    # root = Tk()
    # root.geometry("500x500")
    
    # gif_path = "/Users/ceo/Desktop/Weather_App_Tkinter/images_sun/1f305.gif"

    # animate_path = AnimateGIF(root,gif_path)
    # animate_path.pack()

    # root.mainloop()