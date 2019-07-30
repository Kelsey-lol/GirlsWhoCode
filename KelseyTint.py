
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
