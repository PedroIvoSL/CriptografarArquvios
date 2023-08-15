import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import hashlib
from colorama import Fore, Back, Style

def encrypt_file(key, input_file):
    backend = default_backend()
    iv = os.urandom(16)  # Gera um IV aleatório

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()

    with open(input_file, 'rb') as f:
        plaintext = f.read()
        ciphertext = iv + encryptor.update(plaintext) + encryptor.finalize()

    encrypted_file = os.path.join("Criptografadas", os.path.basename(input_file) + ".enc")
    with open(encrypted_file, 'wb') as f:
        f.write(ciphertext)

def decrypt_file(key, input_file):
    backend = default_backend()

    with open(input_file, 'rb') as f:  # Abre o arquivo em modo binário
        ciphertext = f.read()
        iv = ciphertext[:16]  # Extrai o IV
        ciphertext = ciphertext[16:]  # Extrai o restante do texto cifrado

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()

    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    decrypted_file_dir = "Descriptografadas"
    if not os.path.exists(decrypted_file_dir):
        os.makedirs(decrypted_file_dir)

    decrypted_file = os.path.join(decrypted_file_dir, os.path.basename(input_file)[:-4])  # Remove a extensão ".enc"
    with open(decrypted_file, 'wb') as f:  # Abre o arquivo em modo binário
        f.write(plaintext)  # Escreve os bytes descriptografados

def main():
    if not os.path.exists("Criptografadas"):
        os.makedirs("Criptografadas")

    while True:
        print(Fore.CYAN + "1 - Criptografar um arquivo")
        print("2 - Descriptografar um arquivo")
        print("3 - Ajuda")
        choice = input("Escolha uma opção: ")
        print(Style.RESET_ALL)

        if choice == '1':
            seed = input(Fore.RED + "Digite a semente para a criptografia (ANOTE ESSA SEMENTE): ")
            print(Style.RESET_ALL)
            key = hashlib.sha256(seed.encode()).digest()  # Usa o hash SHA-256 como chave
            input_file = input(Fore.CYAN +"Cole o caminho completo do arquivo de entrada: ")
            encrypt_file(key, input_file)
            print("Arquivo criptografado com sucesso!")
            print(Style.RESET_ALL)

        elif choice == '2':
            seed = input(Fore.RED + "Digite a semente para a descriptografia: ")
            key = hashlib.sha256(seed.encode()).digest()  # Usa o hash SHA-256 como chave
            input_file = input(Fore.CYAN + "Cole o caminho completo do arquivo criptografado de entrada: ")
            decrypt_file(key, input_file)
            print("Arquivo descriptografado com sucesso!")
            print(Style.RESET_ALL)

        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.CYAN +"Para o funcionamento dessa ferramenta o usuario deve colocar uma 'semente' que sera ultilizada para as duas funções desse codigo!")
            print(Fore.RED + "\nANOTE ESSA CHAVE EM ALGUM LUGAR!")
            print(Style.RESET_ALL)
        
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
    print(Style.RESET_ALL)