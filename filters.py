# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
im = Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(img_name):
    im = Image.open(img_name)
    return im
# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(picture):
    picture.show()
# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(img_name, puppy):
    img_name.save(puppy)
# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(pic):

    darkblue = (0, 50, 76)
    red = (217, 26, 33)
    lightblue = (112, 150, 158)
    yellow = (252, 227, 166)
    pixels = list(pic.getdata())
    new_img = []

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_img.append(darkblue)
        elif intensity >= 182 and intensity < 364:
            new_img.append(red)
        elif intensity >= 364 and intensity < 546:
            new_img.append(lightblue)
        elif intensity >= 546:
            new_img.append(yellow)

    new_image = Image.new("RGB",(1000,669), p)
    new_image.putdata(new_img)
    return new_image

def inverse(pic1):

    darkblue = (255, 205, 179)
    red = (38, 229, 222)
    lightblue = (143, 105, 97)
    yellow = (3, 28, 89)
    pixels = list(pic1.getdata())
    new_img1 = []

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_img1.append(darkblue)
        elif intensity >= 182 and intensity < 364:
            new_img1.append(red)
        elif intensity >= 364 and intensity < 546:
            new_img1.append(lightblue)
        elif intensity >= 546:
            new_img1.append(yellow)

    new_image1 = Image.new("RGB",(1000,669), p)
    new_image1.putdata(new_img1)
    return new_image1

def tint(pic2):

    darkblue = (100, 50, 76)
    red = (317, 26, 33)
    lightblue = (212, 150, 158)
    yellow = (352, 227, 166)
    pixels = list(pic2.getdata())
    new_img2 = []

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 282:
            new_img2.append(darkblue)
        elif intensity >= 282 and intensity < 464:
            new_img2.append(red)
        elif intensity >= 464 and intensity < 646:
            new_img2.append(lightblue)
        elif intensity >= 646:
            new_img2.append(yellow)

    new_image2 = Image.new("RGB",(1000,669), p)
    new_image2.putdata(new_img2)
    return new_image2

def inverse2(pic3):

    darkblue = (455, 105, 79)
    red = (238, 129, 122)
    lightblue = (343, 5, -97)
    yellow = (203, -28, -89)
    pixels = list(pic3.getdata())
    new_img3 = []

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_img3.append(darkblue)
        elif intensity >= 182 and intensity < 364:
            new_img3.append(red)
        elif intensity >= 364 and intensity < 546:
            new_img3.append(lightblue)
        elif intensity >= 546:
            new_img3.append(yellow)

    new_image3 = Image.new("RGB",(1000,669), p)
    new_image3.putdata(new_img3)
    return new_image3
