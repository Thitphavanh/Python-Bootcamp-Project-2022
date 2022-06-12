# ocr.py
import pytesseract
from PIL import Image
import os
path = os.getcwd()

image = Image.open('pantip-post.png')
print(pytesseract.image_to_string(image, lang='tha'))