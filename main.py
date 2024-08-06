from PIL import Image

# 打开图片
image = Image.open('path_to_your_image.jpg')

# 将图片转换为RGB模式
image = image.convert('RGB')

# 获取图片的宽度和高度
width, height = image.size

# 遍历每个像素并提取RGB值
for x in range(width):
    for y in range(height):
        r, g, b = image.getpixel((x, y))
        print(f"Pixel at ({x}, {y}): R={r}, G={g}, B={b}")