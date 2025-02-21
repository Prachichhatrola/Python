import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clear_name = os.path.splitext(filename)[0]
    img.save(f"{output_folder}{clear_name}.png", "png")
    print(f"{clear_name} converted")
