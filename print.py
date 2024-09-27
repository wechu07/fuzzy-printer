import cv2
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import img2pdf

font_path = "AlexBrush-Regular.ttf" # font from canva template
font_size = 100  # fixed font after horsin around

list_of_names = []

def cleanup_data():
    with open("cleaned_volunteer_names.csv") as file:
        for line in file:
            list_of_names.append(line.strip())

def generate_certificates():
    if not os.path.exists('generated-certificates-data'):
        os.makedirs('generated-certificates-data')

    font = ImageFont.truetype(font_path, font_size)

    for name in list_of_names:
        template = cv2.imread('template.jpg')
        template_pil = Image.fromarray(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(template_pil)

        # Split the name into words and count them
        num_words = len(name.split())

        # position = (450, 450)  # This is a fixed position after horsin around

        if num_words == 2:
            position = (570, 450)
        else:
            position = (450, 450)

        color = (0, 0, 0)  # Black color for names

        draw.text(position, name, font=font, fill=color)

        template = cv2.cvtColor(np.array(template_pil), cv2.COLOR_RGB2BGR)
        cv2.imwrite(f'generated-certificates-data/{name}.jpg', template)

def convert_images_to_pdfs():
    for name in list_of_names:
        image_file = f'generated-certificates-data/{name}.jpg'
        pdf_path = f'generated-certificates-data/{name}.pdf'
        
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_file))

# Now we run them
cleanup_data()
generate_certificates()
convert_images_to_pdfs()