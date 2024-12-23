from rembg import remove
from PIL import Image
import os

def removeBg():
    input_path = input("Enter the path of the image: ");
    output_dir = './outputImage/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = os.listdir(output_dir);
    count = len([f for f in files if f.startswith('result') and f.endswith('.png')]);
    output_path = os.path.join(output_dir, f'result{count + 1}.png');
    inp = Image.open(input_path);
    output = remove(inp);
    output.save(output_path)
    print("Background removed successfully");
    

def askForBgRemoval():
    print("Do you want to remove the background of the image? (yes/no): ")
    choice = input()
    if choice == 'yes':
        removeBg();
    else:
        print("Background not removed");

print('---------------------------------');
print("Welcome to the Background Remover");
print('---------------------------------');
print("This program removes the background of the image");
print('---------------------------------');
print("Please provide the path of the image");
print('---------------------------------');

askForBgRemoval();

# end of the code..