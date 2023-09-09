import fitz
from pathlib import Path

pdf_file = "classlist_from_webuntis.pdf"
image_folder = Path("jpgs")

image_folder.mkdir()
pdf_document = fitz.open(pdf_file)
for page in pdf_document:
    image_infos = {ii['xref']:ii['bbox'] for ii in page.get_image_info(xrefs=True)}
    for xref,(x,y,w,h) in image_infos.items():
        index = page.get_text("text", clip=[0,y,x,h]).strip()
        last_name = page.get_text("text", clip=[x,y,220,h]).strip()
        first_names = page.get_text("text", clip=[220,y,390,h]).strip()
        with open(image_folder/f'{index} {first_names} {last_name}.jpg', "wb") as file:
            file.write(pdf_document.extract_image(xref)["image"])

