from io import BytesIO
from pathlib import Path
from typing import List, Union
from PIL import Image
from pypdf import PageRange, PdfReader, PdfWriter, Transformation


def image_to_pdf(stamp_img: Union[Path, str]) -> PdfReader:
    img = Image.open(stamp_img)
    img_as_pdf = BytesIO()
    img.save(img_as_pdf, "pdf")
    return PdfReader(img_as_pdf)


def stamp_img(
    content_pdf: Union[Path, str],
    stamp_img: Union[Path, str],
    pdf_result: Union[Path, str],
    page_indices: Union[PageRange, List[int], None] = None,
):
    # Convert the image to a PDF
    stamp_pdf = image_to_pdf(stamp_img)

    # Then use the same stamp code from above
    stamp_page = stamp_pdf.pages[0]

    writer = PdfWriter()

    reader = PdfReader(content_pdf)
    writer.append(reader, pages=page_indices)
    for content_page in writer.pages:
        content_page.merge_transformed_page(stamp_page,Transformation().scale(0.3).translate(250,0.1),)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)


stamp_img("documento.pdf", "selo.png", "documento_carimbado.pdf")

stamp = PdfReader("documento_carimbado.pdf").pages[0]
writer = PdfWriter(clone_from="data.pdf")
for page in writer.pages:
    page.merge_page(stamp, over=False)  # here set to False for watermarking

writer.write("out.pdf")

stamp_img("documento_carimbado.pdf", "selo.png", "out.pdf")
