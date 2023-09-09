from pathlib import Path
import PIL
import openpyxl
import openpyxl.drawing

image_folder = Path("jpegs")
outfilename = 'classlist.xlsx'
row_height = 30
image_height = 40

workbook = openpyxl.Workbook()
sheet = workbook.active
for i, fname in enumerate(image_folder.glob('*.jpg')):
    img = openpyxl.drawing.image.Image(PIL.Image.open(fname))
    img.width,img.height = image_height*img.width/img.height,image_height
    sheet.add_image(img, f'B{i+1}')
    sheet.row_dimensions[i+1].height = row_height
    parts = fname.stem.split()
    sheet.cell(row=i+1, column=1).value = int(parts[0])
    sheet.cell(row=i+1, column=3).value = " ".join(parts[1:])
        
workbook.save(outfilename)