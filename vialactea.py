import os 
from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

with open("chave.key", "rb") as key:
    secretkey = key.read()

for file in os.listdir():
    if file == "andromeda.py" or file == "chave_key" or file == "vialactea.py":
        continue
    if os.path.isfile(files):
        files.append(files)

for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_decrypted = Fernet(secretkey).decrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_decrypted)