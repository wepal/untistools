import fitz
from pathlib import Path

pdf_file = Path(r"C:\Users\werne\OneDrive - Erich Fried Realgymnasium\2C\Fotos-2C.pdf")
image_folder = pdf_file.parent/pdf_file.stem

image_folder.mkdir(exist_ok=True)
pdf_document = fitz.open(pdf_file)
for page in pdf_document:
    image_infos = {ii['xref']:ii['bbox'] for ii in page.get_image_info(xrefs=True)}
    for i,(xref,(x,y,w,h)) in enumerate(image_infos.items()):
        #index = i
        index = int(page.get_text("text", clip=[0,y,x,h]).strip())
        last_names = page.get_text("text", clip=[x,y,220,h]).strip()
        first_names = page.get_text("text", clip=[220,y,390,h]).strip()
        with open(image_folder/f'{index:02d}_{first_names}_{last_names}.jpg', "wb") as file:
            file.write(pdf_document.extract_image(xref)["image"])

