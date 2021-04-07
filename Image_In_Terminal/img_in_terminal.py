# pip install color-it
# pip install pillow

from PIL import Image
from colorit import init_colorit, background

init_colorit()
image = Image.open(input("Enter image path: "))

fixed_height = int(input("Enter height to resize the image: "))
height_percent = (fixed_height / float(image.size[1]))
width_size = int((float(image.size[0]) * float(height_percent)))
image = image.resize((width_size, fixed_height), Image.NEAREST)

for y in range(image.size[1]):
    for x in range(image.size[0]):
        print(background("  ", image.getpixel((x,y))), end='')
    print()