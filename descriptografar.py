import os
import pyaes

# Função para descriptografar um arquivo
def descriptografar_arquivo(file_name, key):
    try:
        with open(file_name, "rb") as file:
            file_data = file.read()

        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        os.remove(file_name)
        original_file_name = file_name.replace(".ransomwaretroll", "")
        with open(original_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo {file_name} descriptografado com sucesso para {original_file_name}.")
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo {file_name}: {e}")

# Chave de descriptografia
key = b"testeransomwares"

# Entrada do usuário
if __name__ == "__main__":
    diretorio_alvo = input("Digite o caminho do diretório a ser descriptografado: ")
    for root, dirs, files in os.walk(diretorio_alvo):
        for file in files:
            if file.endswith(".ransomwaretroll"):
                file_path = os.path.join(root, file)
                descriptografar_arquivo(file_path, key)

