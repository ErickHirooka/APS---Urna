# Criar a cifra XOR
def xor_cifra(texto, chave):
    # caso o texto seja uma string, isso vai transformar em bytes
    # "isinstance()" checa se um objeto pertence a um determinado tipo de variavel, nesse caso, se "texto" pertence a "str"
    if isinstance(texto, str):
        texto = texto.encode()
    # Se a chave for uma string, também a codifica para bytes.
    if isinstance(chave, str):
        chave = chave.encode()
        

    # Se a chave for maior que a string, reduzir até o tamanho da string
    if len(chave) < len(texto):
        chave = chave * (len(texto) // len(chave) + 1)
        chave = chave[: len(texto)]

    # Vai ser iterado todos os bytes, fazendo uma operação XOR.
    return bytes([x ^ y for x, y in zip(texto, chave)])


def acessa_arquivo(nome_arq):
    with open(nome_arq, 'r') as arquivo:
        return arquivo.read()
    
def cria_arquivo(nome_arq):
    #Cria e fecha o arquivo vazio
    with open(nome_arq, 'w') as arquivo:
        pass 
    
def insere_conteudo(nome_arq):
    conteudo = input("Digite o conteúdo a ser inserido no arquivo: ")
    #Escreve o conteudo no arquivo novo
    with open(nome_arq, 'w') as arquivo:
        arquivo.write(conteudo)
    
def criptografar(nome_arquivo_entrada, nome_arquivo_saida, chave_criptografia):
    #Lê o conteúdo do arquivo original das urnas
    conteudo = acessa_arquivo(nome_arquivo_entrada)
    
    #Criptografa o conteúdo
    conteudo_criptografado = xor_cifra(conteudo, chave_criptografia)
    
    #Salva o resultado no arquivo de saída
    #O resultado da cifra XOR é bytes. Você deve usar 'wb' para escrever bytes.
    with open(nome_arquivo_saida, 'wb') as arquivo_saida:
        arquivo_saida.write(conteudo_criptografado)
        
    print(f"Conteúdo criptografado com chave (que deveria ser em bytes) e salvo em '{nome_arquivo_saida}'.")


#Lê o NOME do arquivo de entrada.
nome_arquivo_entrada = input("Digite o nome do arquivo a ser criptografado: ")

#Lê o NOME do arquivo de saída.
nome_arquivo_saida = input("Digite o nome do arquivo para salvar o texto criptografado: ")

#Lê a chave de criptografia.
chave_criptografia = input("Digite a string chave para encriptografia: ")

#Chama a função usando os nomes dos arquivos.
criptografar(nome_arquivo_entrada, nome_arquivo_saida, chave_criptografia)