from PIL import Image

img = Image.open("foto.png")


def text_to_ascii(text):
    text_hex = ''
    for i in text:
        hex_ascii = bin(ord(i))[2:]
        while len(hex_ascii) < 8:
            hex_ascii = '0' + hex_ascii
        text_hex += hex_ascii
    return text_hex


def encode(img, text):
    print(text)
    size = img.size
    print(size)
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
                return (img, i_text)

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



def decode(img):
    size = img.size
    width = size [0]
    height = size [1]
    symbols = ''
    words=[]
    for i in range (width):
        for j in range (height):
            pix = img.getpixel ((i, j))
            symbols += bin(pix[0])[-1:]
            symbols += bin (pix [1]) [-1:]
            symbols += bin (pix [2]) [-1:]

    start_p = 0
    stop_p = 8
    while True:
        symbol = int(symbols[start_p:stop_p],2)
        if (symbol > 31) and (symbol < 127):
            words.append(chr(symbol))
            start_p += 8
            stop_p += 8
        else:
            result = ''
            for word in words:
                result += word
            return (result)


text="My sister's name is Kitty. She is three. She is a nice funny little girl. I like to play with her. We play hide-and-seek and tag. Kitty has got many toys: dolls, balls, toy animals. We often play with her toys."

img1 = encode(img, text_to_ascii(text))[0]
img1.save("tmp.png")
img2 = Image.open("tmp1.png")
print(decode(img2))
