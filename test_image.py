from tkinter import Tk, Label
from PIL import Image, ImageTk

def test_image(path):
    try:
        root = Tk()
        root.title("Image Test")
        # Open the image file
        image = Image.open(path)
        # Convert the image to a format Tkinter can use
        photo = ImageTk.PhotoImage(image)
    

        # Create a label to display the image
        label = Label(root, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack()

        # Start the Tkinter main loop
        root.mainloop()

    except Exception as e:
        print(f"Error: {e}")

# Path to your image file
image_path = "images_sun/1f305.gif"

test_image(image_path)
