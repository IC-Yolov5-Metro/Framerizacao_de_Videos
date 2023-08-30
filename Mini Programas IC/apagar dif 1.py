import os

def process_files_in_folder(folder_path):
    # Verificar se a pasta existe
    if not os.path.exists(folder_path):
        print("Pasta não encontrada.")
        return

    # Percorrer todos os arquivos da pasta
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            process_file(file_path)

def process_file(file_path):
    # Abrir o arquivo para leitura
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Filtrar as linhas que começam com "1"
    filtered_lines = [line for line in lines if line.strip().startswith("1")]

    # Abrir o arquivo para escrita, apagando o conteúdo anterior
    with open(file_path, "w") as file:
        file.writelines(filtered_lines)

if __name__ == "__main__":
    folder_path = "./val"  # Substitua pelo caminho da sua pasta
    process_files_in_folder(folder_path)
