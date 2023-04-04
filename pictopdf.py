import os
from fpdf import FPDF

# Prompt user for image folder path
image_folder = input("输入图片文件夹地址： ")

# Get all image files in the specified folder
image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(".jpg") or f.endswith(".png")]

# Sort the image paths by filename
image_paths.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))

# Create a PDF object
pdf = FPDF()

# Add each image as a page to the PDF
for image_path in image_paths:
    pdf.add_page()
    pdf.image(image_path, 0, 0, pdf.w, pdf.h)

# Save the PDF file in the same folder as the images with the same name as the folder
pdf_folder = os.path.dirname(image_folder)
pdf_name = os.path.basename(image_folder) + ".pdf"
pdf.output(os.path.join(pdf_folder, pdf_name), "F")
