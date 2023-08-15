# Utilitário de Criptografia e Descriptografia de Arquivos

Este script em Python fornece uma ferramenta básica de linha de comando para criptografar e descriptografar arquivos usando o algoritmo AES (Padrão de Criptografia Avançada) no modo CFB (Cipher Feedback). Ele utiliza a biblioteca `cryptography` para operações criptográficas.

## Pré-requisitos

- Python 3.x
- Biblioteca `cryptography` (instale usando `pip install cryptography`)
- Biblioteca `colorama` (instale usando `pip install colorama`)

## Clone

1. Clone ou faça o download deste repositório.

2. Navegue até o diretório do repositório em seu terminal.

3. Execute o script usando o seguinte comando:

   ```bash
   python crpy.py
## Utilização
1. O script apresentará um menu com as seguintes opções:
   1 - Criptografar um Arquivo: Criptografa um arquivo de entrada especificado.
   2 - Descriptografar um Arquivo: Descriptografa um arquivo criptografado especificado.
   3 - Ajuda: Exibe informações sobre como usar a ferramenta.
   
2. Escolha uma opção digitando o número correspondente.

3. Dependendo da opção escolhida, você será solicitado a fornecer uma semente (usada para derivar a chave de criptografia/descriptografia) e o caminho para o arquivo de entrada.

4. Após a conclusão da operação, uma mensagem de sucesso será exibida.

5. Os arquivos criptografados serão armazenados no diretório "Criptografadas" e os arquivos descriptografados serão armazenados no diretório "Descriptografadas".

## Observação
• Esta é uma implementação básica destinada a fins educacionais. Pode faltar recursos de segurança necessários para um ambiente de produção.

• Certifique-se de manter a semente (chave de derivação de chave) segura e protegida, pois ela é fundamental tanto para a criptografia quanto para a descriptografia.
