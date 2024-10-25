import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import inicio
import base64

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(private_key)
    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(public_key)

    return private_key, public_key

def encrypt_data(public_key, data):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_data = cipher.encrypt(data.encode())
    return base64.b64encode(encrypted_data).decode()

def decrypt_data(private_key, encrypted_data):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_data = cipher.decrypt(base64.b64decode(encrypted_data.encode())).decode()
    return decrypted_data

private_key, public_key = generate_key_pair()
print("Gerando chave privada no diretorio")
print("Private Key:", private_key)
print("Gerando chave Publica no diretorio")
print("Public Key:", public_key)

nome = input("Digite exatamente o nome do seu arquivo, que esta no diretorio do programa:") + '.pdf'
original_data = inicio.mandartxt(nome)
print("Encriptando os dados...")
encrypted_data = encrypt_data(public_key, original_data)

inicio.marcaburro(nome,"selo.png","documento_carimbado.pdf")
inicio.escreve(nome)
print("Dado encriptado:", encrypted_data)

cond = input("\nEscolha uma opção: Y->Desenrolar or N->Não interessa ").upper()

if cond == 'Y':
    decrypted_data = decrypt_data(private_key, encrypted_data)
    print("Decrypted Data:", decrypted_data)
print('Foi criado um novo arquivo, carimbado e assinado no mesmo diretorio do programa.')

os.remove('data.pdf')
os.remove('documento_carimbado.pdf')



