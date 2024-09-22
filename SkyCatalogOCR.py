from os import listdir
from os.path import isfile, join
import csv, re
import cv2

import pytesseract
from PIL import Image

unsorted_objects = ["Objects/" + f for f in listdir("Objects")]
sorted_objects = sorted(unsorted_objects, key=lambda x: int(x[33:35].replace('.', '')))


def image_to_str(path):
    return pytesseract.image_to_string(Image.open(path))

def split_line(line):
	line = re.sub(r'\s+', ' ', line)
	fields = line.split(' ')
	formatted_fields = []

	for field in fields:
		field.replace(",", " ", 1)
		formatted_fields.append(field.replace('°', '').replace("'", '').replace("’", ''))
        
	while len(formatted_fields) < 15:
		formatted_fields.append('')

	return formatted_fields

with open("out.csv", "a", newline='') as file:
	writer = csv.writer(file)

	image = cv2.imread(sorted_objects[11])
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

	text = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6').splitlines()
	for line in text:
		fields = split_line(line)
		fields[0:2] = [' '.join(fields[0:2])]
		if (fields[0] == ' '):
			continue

		writer.writerow(fields)
	

# Name,RA,Dec,Const,Type,DimMax,DimMin,Vis,Brightness,Color,Shape,Structure,HD,*Mag,*Spec,Notes
# NGC 7822,0036,+6837,Cep,E,60,30,eeF,3,R, , , , , ,Arc of nebulosity n of Ced 214
