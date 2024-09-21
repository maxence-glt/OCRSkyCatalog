from os import listdir
from os.path import isfile, join

import pytesseract
from PIL import Image

# IMPORTANT: this should end with '...\tesseract.exe'
# pytesseract.pytesseract.tesseract_cmd = 

list_with_many_images = ["Objects/" + f for f in listdir("Objects") if isfile(join("Objects", f))]

def image_to_str(path):
    return pytesseract.image_to_string(Image.open(path))

# with open("out.csv", "w+", encoding="utf-8") as file:
#   file.write("ImagePath, ImageText")
#   for image_path in list_with_many_images:
#     print(image_path)
#     text = image_to_str(image_path)
#     line = f"{image_path}, {text}\n"
#     file.write(line)

print(image_to_str("Objects/SkyCatalog-BrightNebulae-0.png"))
