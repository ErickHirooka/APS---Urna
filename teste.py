# Função para criptografar usando Cifra de César
def criptografar_cesar(texto, chave):
    texto_criptografado = ""
    for char in texto:
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z'): #isalpha
            base = ord('A') if 'A' <= char <= 'Z' else ord('a') #isupper
            texto_criptografado += chr((ord(char) - base + chave) % 26 + base)
        else:
            texto_criptografado += char
    return texto_criptografado

# Função para descriptografar usando Cifra de César
def descriptografar_cesar(texto, chave):
    texto_descriptografado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            texto_descriptografado += chr((ord(char) - base - chave) % 26 + base)
        else:
            texto_descriptografado += char
    return texto_descriptografado

# Função para criar um arquivo
def cria_arquivo(nome_arq):
    with open(nome_arq, 'w') as arquivo:
        pass  # Cria e fecha o arquivo vazio

# Função para acessar (ler) um arquivo
def acessa_arquivo(nome_arq):
    with open(nome_arq, 'r') as arquivo:
        return arquivo.read()

# Função para inserir conteúdo em um arquivo
def insere_conteudo(nome_arq):
    conteudo = input("Digite o conteúdo a ser inserido no arquivo: ")
    with open(nome_arq, 'w') as arquivo:
        arquivo.write(conteudo)

# Função para criptografar conteúdo de um arquivo
def criptografar(nome_arquivo_entrada, nome_arquivo_saida, chave_criptografia):
    conteudo = acessa_arquivo(nome_arquivo_entrada)
    conteudo_criptografado = criptografar_cesar(conteudo, chave_criptografia)
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        arquivo_saida.write(conteudo_criptografado)
    print(f"Conteúdo criptografado com chave {chave_criptografia} e salvo em '{nome_arquivo_saida}'.")

# Função para descriptografar conteúdo de um arquivo
def descriptografar_arquivo(nome_arquivo_criptografado, nome_arquivo_descriptografado, chave_descriptografia):
    conteudo_criptografado = acessa_arquivo(nome_arquivo_criptografado)
    conteudo_descriptografado = descriptografar_cesar(conteudo_criptografado, chave_descriptografia)
    with open(nome_arquivo_descriptografado, 'w') as arquivo_saida:
        arquivo_saida.write(conteudo_descriptografado)
    print(f"Conteúdo descriptografado com chave {chave_descriptografia} e salvo em '{nome_arquivo_descriptografado}'.")

# Execução do programa
nome_arquivo_atual = input("Digite o nome do arquivo a ser criado: ")
cria_arquivo(nome_arquivo_atual)
insere_conteudo(nome_arquivo_atual)

nome_arquivo_entrada = input("Digite o nome do arquivo a ser criptografado: ")
nome_arquivo_saida = input("Digite o nome do arquivo para salvar o texto criptografado: ")
chave_criptografia = int(input("Digite a chave numérica para criptografia (ex: 5): "))
criptografar(nome_arquivo_entrada, nome_arquivo_saida, chave_criptografia)

nome_arquivo_criptografado = input("Digite o nome do arquivo criptografado a ser lido: ")
nome_arquivo_descriptografado = input("Digite o nome do arquivo para salvar o texto descriptografado: ")
chave_descriptografia = int(input("Digite a chave numérica para descriptografia (deve ser a mesma usada na criptografia): "))
descriptografar_arquivo(nome_arquivo_criptografado, nome_arquivo_descriptografado, chave_descriptografia)