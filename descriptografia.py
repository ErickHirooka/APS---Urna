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


# --- Função de Criptografia ---
def xor_cifra(texto, chave):
    if isinstance(texto, str):
        texto = texto.encode('latin-1')
    if isinstance(chave, str):
        chave = chave.encode('latin-1')
        
    if len(chave) < len(texto):
        chave = chave * (len(texto) // len(chave) + 1)
        chave = chave[: len(texto)]

    return bytes([x ^ y for x, y in zip(texto, chave)])


def descriptografar_e_verificar(nome_arquivo_entrada, nome_arquivo_saida, chave_criptografia):
    try:
        with open(nome_arquivo_entrada, 'rb') as arquivo_entrada:
            linha_hash_bytes = arquivo_entrada.readline()
            conteudo_criptografado = arquivo_entrada.read()
    
    except FileNotFoundError:
        print(f"Erro: Arquivo de entrada '{nome_arquivo_entrada}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo '{nome_arquivo_entrada}': {e}")
        return

    try:
        hash_salvo = int(linha_hash_bytes.decode('latin-1').strip())
    except (ValueError, UnicodeDecodeError):
        print("Erro: Formato de arquivo inválido ou corrompido.")
        return

    conteudo_descriptografado_bytes = xor_cifra(conteudo_criptografado, chave_criptografia)
    
    hash_calculado = hash_djb2(conteudo_descriptografado_bytes)
    
    if hash_calculado == hash_salvo:
        print("-" * 30)
        print("VERIFICAÇÃO CONCLUÍDA: Sucesso! O arquivo é autêntico.")
        print(f"Hash esperado: {hash_salvo}")
        print(f"Hash calculado: {hash_calculado}")
        
        try:
            conteudo_final_string = conteudo_descriptografado_bytes.decode('latin-1')
            
            with open(nome_arquivo_saida, 'w', encoding='latin-1') as arquivo_saida:
                arquivo_saida.write(conteudo_final_string)
            
            print(f"Arquivo descriptografado salvo em: '{nome_arquivo_saida}'")
            print("-" * 30)
        
        except Exception as e:
            print(f"Erro inesperado ao salvar o arquivo: {e}")
    
    else:
        print("-" * 30)
        print("FALHA NA VERIFICAÇÃO!")
        print("MOTIVO: A senha está incorreta ou o arquivo foi modificado.")
        print(f"Hash esperado (do arquivo): {hash_salvo}")
        print(f"Hash calculado (da tentativa): {hash_calculado}")
        print("Nenhum arquivo de saída foi gerado.")
        print("-" * 30)


if __name__ == "__main__":
    print("\n--- DESCRIPTOGRAFIA E VERIFICAÇÃO ---")
    nome_arquivo_entrada = input("Digite o nome do arquivo criptografado: ")
    nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
    chave_criptografia = input("Digite a senha de descriptografia: ")
    
    descriptografar_e_verificar(nome_arquivo_entrada, nome_arquivo_saida, chave_criptografia)
