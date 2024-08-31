from pathlib import Path
import PIL
import openpyxl
import openpyxl.drawing

image_folder = Path(r"C:\Users\werne\OneDrive - Erich Fried Realgymnasium\2C\Fotos-2C")
outfilename = image_folder.parent/"Liste-2C.xlsx"
row_height = 30
image_height = 40

workbook = openpyxl.Workbook()
sheet = workbook.active
for i, fname in enumerate(image_folder.glob('*.jpg')):
    img = openpyxl.drawing.image.Image(PIL.Image.open(fname))
    img.width,img.height = image_height*img.width/img.height,image_height
    sheet.add_image(img, f'B{i+1}')
    sheet.row_dimensions[i+1].height = row_height
    parts = fname.stem.split('_')
    sheet.cell(row=i+1, column=1).value = int(parts[0])
    sheet.cell(row=i+1, column=3).value = parts[1]
    sheet.cell(row=i+1, column=4).value = parts[2]
        
workbook.save(outfilename)