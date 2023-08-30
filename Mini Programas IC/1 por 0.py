import os
import re

def change_first_digit_1_to_0(file_path):
    # Abrir o arquivo e ler o conteúdo
    with open(file_path, 'r') as file:
        content = file.read()

    # Alterar o primeiro dígito "1" para "0"
    content = re.sub(r'\b1\b', '0', content, 1)

    # Escrever o conteúdo modificado de volta no arquivo
    with open(file_path, 'w') as file:
        file.write(content)

def main(folder_path):
    # Verificar se o caminho da pasta é válido
    if not os.path.isdir(folder_path):
        print("Caminho inválido. Certifique-se de fornecer um caminho de pasta válido.")
        return

    # Percorrer todos os arquivos na pasta
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            change_first_digit_1_to_0(file_path)
            print(f"Arquivo '{filename}' modificado com sucesso.")

if __name__ == "__main__":
    folder_path = "./test"  # Substitua pelo caminho da sua pasta
    main(folder_path)
