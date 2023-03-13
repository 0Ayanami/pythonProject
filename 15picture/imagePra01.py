from PIL import Image, ImageFilter
# 滤镜效果
image = Image.open('穆勒.jpg')
image.filter(ImageFilter.DETAIL).show()

