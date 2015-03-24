from PIL import Image
import os

im = Image.open('adamo_ruggiero.jpg')
im.rotate(45).show()