from PIL import Image

filename = 'X3.png'

img = Image.open(filename)
img = img.convert("RGBA")

pixdata = img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        r, g, b, a = pixdata[x, y]
        if (r, g, b) == (0, 0, 0):
            img.putpixel((x, y), (0, 0, 200, a))

#img.save('green_' + filename)
img.save('blue_' + filename)
