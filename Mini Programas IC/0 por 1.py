import os

def change_first_digit(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        if content and content[0].isdigit() and content[0] == '0':
            content = '1' + content[1:]
    
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    folder_path = './test'  # Insira o caminho da pasta contendo os arquivos .txt
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            change_first_digit(file_path)
            print(f"Arquivo '{file_name}' processado com sucesso.")

if __name__ == "__main__":
    main()
