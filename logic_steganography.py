from PIL import Image

img = Image.open("foto.jpeg")


def text_to_ascii(text):
    text_hex = ''
    for i in text:
        hex_ascii = bin(ord(i))[2:]
        while len(hex_ascii) < 8:
            hex_ascii = '0' + hex_ascii
        text_hex += hex_ascii
    return text_hex


def encode(img, text):
    size = img.size
    width = size[0]
    height = size[1]
    i_text = 0
    for i in range(width):
        for j in range(height):

            pix = img.getpixel((i, j))

            try:
                r = int(bin(pix[0])[2:-1] + text[i_text], 2)
                i_text += 1
            except IndexError:
                return img

            try:
                g = int(bin(pix[1])[2:-1] + text[i_text], 2)
                i_text += 1
            except IndexError:
                g = pix[1]
            try:
                b = int(bin(pix[2])[2:-1] + text[i_text], 2)
                i_text += 1
            except IndexError:
                b = pix[2]
            img.putpixel((i, j), (r, g, b))


img1 = encode(img, text_to_ascii('text'))
img1.save("tmp.bmp", "BMP")
