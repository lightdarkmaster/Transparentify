import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import io
from rembg import remove

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "rb") as input_file:
            input_image = input_file.read()
            output_image = remove(input_image);
            display_image(output_image);
            
        
def display_image(image_data):
    image = Image.open(io.BytesIO(image_data));
    image.thumbnail((400, 400));
    photo = ImageTk.PhotoImage(image);
    label.config(image=photo);
    label.Image = photo;
    
    
def download_image():
    if hasattr(label, 'Image'):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            label.Image._PhotoImage__photo.write(file_path, format="png")
    
    
    
root = tk.Tk()
root.title("Remove Background")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
frame.pack(pady=20, padx=20, fill="both", expand=True)

title_label = tk.Label(frame, text="Remove Background from Image", font=("Helvetica", 16), bg="#ffffff")
title_label.pack(pady=10)

upload_button = tk.Button(frame, text="Upload Image", command=upload_file, bg="#4CAF50", fg="white", font=("Helvetica", 12))
upload_button.pack(pady=20)

download_button = tk.Button(frame, text="Download Image", command=lambda: download_image(), bg="#008CBA", fg="white", font=("Helvetica", 12))
download_button.pack(pady=20)

label = tk.Label(frame, bg="#ffffff")
label.pack(pady=20)


root.mainloop();