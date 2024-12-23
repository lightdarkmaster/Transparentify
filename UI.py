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
    
def download_image(image_data):
    file_path = filedialog.asksaveasfilename(defaultextension=".png");
    if file_path:
        with open(file_path, "wb") as output_file:
            output_file.write(image_data);  
    
    
    
root = tk.Tk()
root.title("Remove Background");
root.geometry("800x600");

frame = tk.Frame(root);
frame.pack(pady=20)

upload_button = tk.Button(frame, text="Upload Image", command=upload_file);
upload_button.pack(pady=20);
download_button = tk.Button(frame, text="Download Image", command=lambda: download_image(label.Image.tobytes()));

label = tk.Label(root);
label.pack(pady=20);

root.mainloop();