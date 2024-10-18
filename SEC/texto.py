from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

# Nome do arquivo PDF
nome_arquivo = "data.pdf"

# Cria um objeto canvas
c = canvas.Canvas(nome_arquivo, pagesize=letter)

# Define a posição do texto
x = 220
y = 20

# Obtém a data e hora atuais
data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Adiciona a data e hora ao PDF
c.drawString(x, y, f"Data e Hora: {data_hora_atual}")

# Salva o PDF
c.save()

print(f"PDF '{nome_arquivo}' criado com sucesso!")
