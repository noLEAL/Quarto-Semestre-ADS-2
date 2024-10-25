import hashlib
from io import BytesIO
from pathlib import Path
from typing import List, Union
from PIL import Image
from pypdf import PageRange, PdfReader, PdfWriter, Transformation
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def mandartxt(namefile):
    """Essa desgraça aqui, faz toda a bruxaria por tras do hash e da encriptação, utilizei como base o proejto desse louco
      https://github.com/VirtusV01/Encryption-with-Python-Encrypting-data-with-key-pairs.git
      """

    # Cria um objeto PdfReader para ler o arquivo PDF "cheio.pdf"
    reader = PdfReader(namefile)
    # Extrai a primeira página do PDF
    page = reader.pages[0]
    # Extrai o texto da primeira página
    textoext = page.extract_text()

    cond = input("\nEscolha uma opção: Y->Exibir o TEXTO or N->Não interessa ").upper()
    if cond == 'Y':
        print(textoext)

    ### Encontrei uma limitação ao encriptar, pois quando o texto é muito longo, encontra uma exeção na func encrypt
    # Cria um objeto hash usando SHA-256 e codifica o texto extraído
    hash_object = hashlib.sha256(textoext.encode())
    # Converte o hash para uma representação hexadecimal
    hash_hex = hash_object.hexdigest()

    # Exibe o resultado
    print(f"O hash SHA-256 do texto é: {hash_hex}")

    return hash_hex

def image_to_pdf(stamp_img: Union[Path, str]) -> PdfReader:

    img = Image.open(stamp_img)
    img_as_pdf = BytesIO()
    img.save(img_as_pdf, "pdf")
    return PdfReader(img_as_pdf)

def marcaburro(content_pdf: Union[Path, str], stamp_img: Union[Path, str], pdf_result: Union[Path, str], page_indices: Union[PageRange, List[int], None] = None,):
    # converte a imagem do carimbo para pdf
    stamp_pdf = image_to_pdf(stamp_img)

    stamp_page = stamp_pdf.pages[0]

    #chama o modulo para escrever
    writer = PdfWriter()

    #coloca o maldito carimbo no documento
    reader = PdfReader(content_pdf)
    writer.append(reader, pages=page_indices)
    for content_page in writer.pages:
        #argumento over=False da func merge_transformed_page ta doidão, não tive saco para resolver por enquanto.
        ##Daria para, pedir para o usuario um a possição, X e Y dentro do plano carteziado. Fazendo assim um
        ##ajuste fino de onde ficaria o carimbo e a data
        content_page.merge_transformed_page(stamp_page,Transformation().scale(0.3).translate(235,15),)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)

    return f"Foi criado um novo arquivo, carimbado e assinado no mesmo diretorio do programa. Com o nome de:{pdf_result}"

def escreve(reciver):
    #Junta pdf data com carimbo e final
    criar_data()
    stamp = PdfReader("documento_carimbado.pdf").pages[0]
    writer = PdfWriter(clone_from="data.pdf")
    for page in writer.pages:
        page.merge_page(stamp, over=False)
    reciver = reciver.removesuffix(".pdf")
    name = reciver + '_final.pdf'
    writer.write(name)

def criar_data():
    # Nome do arquivo PDF
    nome_arquivo = "data.pdf"

    # Cria um objeto canvas
    c = canvas.Canvas(nome_arquivo, pagesize=letter)

    # Define a posição do texto da data
    ##Poderia receber os mesmo argumento de possição do usuario para possicionar
    x = 220
    y = 15

    # Obtém a data e hora atuais
    data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Adiciona a data e hora ao PDF
    c.drawString(x, y, f"Data e Hora: {data_hora_atual}")

    # Salva o PDF
    c.save()







