# --- Função de Hash DJB2 ---
def hash_djb2(texto_bytes):
    # Garante que a entrada sejam bytes
    if isinstance(texto_bytes, str):
        # Usa 'latin-1' para consistência com os arquivos .csv
        texto_bytes = texto_bytes.encode('latin-1')
        
    hash_val = 5381 
    
    for b in texto_bytes:
        # Lógica do hash: (hash * 33) + byte
        hash_val = ((hash_val << 5) + hash_val + b) & 0xFFFFFFFF
        
    return hash_val


# --- Funções de Criptografia e Arquivo ---
def xor_cifra(texto, chave):
    if isinstance(texto, str):
        texto = texto.encode('latin-1')
    if isinstance(chave, str):
        chave = chave.encode('latin-1')
        
    if len(chave) < len(texto):
        chave = chave * (len(texto) // len(chave) + 1)
        chave = chave[: len(texto)]

    return bytes([x ^ y for x, y in zip(texto, chave)])


def acessa_arquivo(nome_arq):
    try:
        with open(nome_arq, 'r', encoding='latin-1') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo de entrada '{nome_arq}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo '{nome_arq}': {e}")
        return None
    
    
def criptografar(nome_arquivo_entrada, nome_arquivo_saida, chave_criptografia):
    conteudo_original = acessa_arquivo(nome_arquivo_entrada)
    if conteudo_original is None:
        print("Operação de criptografia cancelada.")
        return

    # Calcula o HASH do conteúdo ORIGINAL
    hash_original = hash_djb2(conteudo_original)
    
    # Criptografa o conteúdo original
    conteudo_criptografado = xor_cifra(conteudo_original, chave_criptografia)
    
    try:
        with open(nome_arquivo_saida, 'wb') as arquivo_saida:
            linha_hash = f"{hash_original}\n".encode('latin-1')
            
            arquivo_saida.write(linha_hash)
            arquivo_saida.write(conteudo_criptografado)
            
        print("-" * 30)
        print(f"Arquivo criptografado com sucesso!")
        print(f"Hash DJB2 (autenticação): {hash_original}")
        print(f"Salvo em: '{nome_arquivo_saida}'")
        print("-" * 30)
        
    except PermissionError:
        print(f"Erro: Sem permissão para escrever no arquivo '{nome_arquivo_saida}'.")
        print("Verifique se o arquivo está aberto em outro programa.")
    except Exception as e:
        print(f"Erro inesperado ao salvar o arquivo: {e}")


if __name__ == "__main__":
    print("\n--- CRIPTOGRAFIA ---")
    nome_arquivo_entrada = input("Digite o nome do arquivo da urna: ")
    nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
    chave_criptografia = input("Digite a senha para criptografia: ")
    
    criptografar(nome_arquivo_entrada, nome_arquivo_saida, chave_criptografia)
