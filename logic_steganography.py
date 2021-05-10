from PIL import Image

img = Image.open("foto.jpeg")


def text_to_ascii(text):
    text_hex = ''
    for i in text:
        hex = bin(ord (i))[2:]
        while len(hex) < 8:
            hex = '0' + hex;
        text_hex += hex
    return text_hex


def encode(img, text):
    size = img.size
    width = size[0] - 1
    height = size[1] - 1
    for i in range(width):
        for j in range(height):
            pix = img.getpixel((i, j))
            r = bin(pix[0])[2:-1] + '1'
            g = bin(pix[1])[2:-1]
            b = bin(pix[2])[2:-1]
            img.putpixel((i, j),(r, g, b))


