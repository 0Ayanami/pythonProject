from PIL import Image

# 像素操作
image = Image.open('穆勒.jpg')
for x in range(80, 310):
    for y in range(20, 360):
        image.putpixel((x, y), (128, 128, 128))
image.show()
