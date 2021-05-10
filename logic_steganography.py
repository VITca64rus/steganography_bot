from PIL import Image
img = Image.open("foto.jpeg")

text = 'ss ananasz'
text_hex = ''
for i in text:
    hex = bin(ord(i))[2:]
    while len(hex)<7:
        hex = '0' + hex;
    text_hex += hex
print(text_hex)



#print(width,height,'kk')
#img.putpixel((25, 45), (255, 0, 0)) # Изменяем цвет пикселя
#print(img.getpixel((479, 319)))


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

#encode(img,'ddd')

