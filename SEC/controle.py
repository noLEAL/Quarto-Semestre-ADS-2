from pypdf import PdfReader, PdfWriter

stamp = PdfReader("documento_carimbado.pdf").pages[0]
writer = PdfWriter(clone_from="data.pdf")
for page in writer.pages:
    page.merge_page(stamp, over=False)  # here set to False for watermarking

writer.write("documento_final.pdf")