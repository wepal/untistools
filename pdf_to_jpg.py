import pymupdf
from pathlib import Path

classname = "3B"
pdf_file = Path(rf"C:\Users\werne\OneDrive - Erich Fried Realgymnasium\{classname}\Fotos-{classname}.pdf")
image_folder = pdf_file.parent/pdf_file.stem

image_folder.mkdir(exist_ok=True)
pdf_document = pymupdf.open(pdf_file)
index = 0
for page in pdf_document:
    image_infos = {ii['xref']:ii['bbox'] for ii in page.get_image_info(xrefs=True)}
    for xref,(x,y,w,h) in image_infos.items():
        index = index + 1
        last_names = page.get_text("text", clip=[x,y,220,h]).strip()
        first_names = page.get_text("text", clip=[220,y,390,h]).strip()
        with open(image_folder/f'{index:02d}_{first_names}_{last_names}.jpg', "wb") as file:
            file.write(pdf_document.extract_image(xref)["image"])

