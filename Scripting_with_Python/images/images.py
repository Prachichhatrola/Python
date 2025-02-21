from PIL import Image, ImageFilter

img = Image.open("./images/village.jpg")
filtered_img = img.convert("L")
filtered_img.save("./images/grey.png", "png")
filtered_img.show()
