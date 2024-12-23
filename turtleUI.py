import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import io
from rembg import remove

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'rb') as file:
            input_image = file.read()
            output_image = remove(input_image)
            display_image(output_image)

def display_image(image_data):
    image = Image.open(io.BytesIO(image_data))
    image.thumbnail((500, 500))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

root = tk.Tk()
root.title("Background Remover")
root.geometry("800x600")  # Set the initial size of the window

frame = tk.Frame(root)
frame.pack(pady=20)

upload_button = tk.Button(frame, text="Upload Image", command=upload_file)
upload_button.pack()

label = tk.Label(root)
label.pack(pady=20)

root.mainloop()