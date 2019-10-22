from PIL import Image

height = 1000
width = 1000

img = Image.new('RGB', (height, width), (255, 255, 255))
img.save("white.jpg")
