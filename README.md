# Transparentify

My simple Python script for removing the background of an image using Python.

## Python Packages Used

1. [rembg](https://github.com/danielgatis/rembg)
2. [PIL](https://pypi.org/project/pillow/)

## How to Use the Script

1. Create an `image` folder where you can store the image you want to remove the background.
2. In the same directory, create a Python file `removebg.py` and copy the code.
3. Install the above core packages.
4. Create an `outputImage` folder.
5. Run the code. (Ensure that the name of the image and directory is accurate.)
6. Wait for the execution; sometimes it will take a few seconds or more depending on the device used.
7. Enjoy...

## Example

Here is an example of how to use the script:

```python
from rembg import remove
from PIL import Image

input_path = 'image/input.jpg'
output_path = 'outputImage/output.png'

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you have suggestions for improving this script, please open an issue or submit a pull request.

## Contact

For any inquiries, please contact [christian.barbosa05222001@gmail.com](mailto:christian.barbosa05222001@gmail.com).