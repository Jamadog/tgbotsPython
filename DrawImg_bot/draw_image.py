from PIL import Image, ImageFilter, ImageOps


def formula(a, b, alpha):
    return min(int(a*255/(256-b*alpha)), 255)


def draw_img(img, blur=25, alpha=1.0):
    img = Image.open(img)
    img1 = img.convert('L')
    img2 = img1.copy()
    img2 = ImageOps.invert(img2)
    for i in range(blur):
        img2 = img2.filter(ImageFilter.BLUR)
    width, height = img1.size
    for x in range(width):
        for y in range(height):
            a = img1.getpixel((x, y))
            b = img2.getpixel((x, y))
            img1.putpixel((x, y), formula(a, b, alpha))

    return img1


