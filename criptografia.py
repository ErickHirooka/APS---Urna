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


# Criar a cifra XOR
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
  
  # Salva o HASH e o CONTEÚDO CRIPTOGRAFADO
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


def descriptografar(nome_arquivo_entrada, nome_arquivo_saida, chave_criptografia):
  try:
    with open(nome_arquivo_entrada, 'rb') as arquivo_entrada:
      linha_hash_bytes = arquivo_entrada.readline()
      conteudo_criptografado = arquivo_entrada.read()
  
  except FileNotFoundError:
    print(f"Erro: Arquivo de entrada '{nome_arquivo_entrada}' não foi encontrado.")
    return
  except PermissionError:
    print(f"Erro: Sem permissão para ler o arquivo '{nome_arquivo_entrada}'.")
    return
  except Exception as e:
    print(f"Erro inesperado ao ler o arquivo '{nome_arquivo_entrada}': {e}")
    return

  try:
    hash_salvo = int(linha_hash_bytes.decode('latin-1').strip())
  except (ValueError, UnicodeDecodeError):
    print("Erro: Formato de arquivo inválido.")
    print("O arquivo pode estar corrompido ou não é um arquivo .urn válido.")
    return

  conteudo_descriptografado_bytes = xor_cifra(conteudo_criptografado, chave_criptografia)
  
  hash_calculado = hash_djb2(conteudo_descriptografado_bytes)
  
  if hash_calculado == hash_salvo:
    print("-" * 30)
    print("VERIFICAÇÃO CONCLUÍDA: Sucesso!")
    print(f"Hash esperado: {hash_salvo}")
    print(f"Hash calculado: {hash_calculado}")
    
    try:
      conteudo_final_string = conteudo_descriptografado_bytes.decode('latin-1')
      
      with open(nome_arquivo_saida, 'w', encoding='latin-1') as arquivo_saida:
        arquivo_saida.write(conteudo_final_string)
      
      print(f"Arquivo descriptografado salvo em: '{nome_arquivo_saida}'")
      print("-" * 30)
    
    except PermissionError:
      print(f"Erro: Sem permissão para escrever no arquivo '{nome_arquivo_saida}'.")
    except Exception as e:
      print(f"Erro inesperado ao salvar o arquivo: {e}")
  
  else:
    print("-" * 30)
    print("FALHA NA VERIFICAÇÃO!")
    print("MOTIVO: A senha está incorreta ou o arquivo foi corrompido.")
    print(f"Hash esperado (do arquivo): {hash_salvo}")
    print(f"Hash calculado (da tentativa): {hash_calculado}")
    print("-" * 30)


print("\n--- Sistema de Criptografia de Urna ---")
print("1. Criptografar um arquivo")
print("2. Descriptografar um arquivo")
print("-" * 30)
opcao = input("Digite o número da opção: ")

if opcao == '1':
  print("\n--- CRIPTOGRAFIA ---")
  nome_arquivo_entrada = input("Digite o nome do arquivo da urna: ")
  nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
  chave_criptografia = input("Digite a senha para criptografia: ")
  
  criptografar(nome_arquivo_entrada, nome_arquivo_saida, chave_criptografia)

elif opcao == '2':
  print("\n--- DESCRIPTOGRAFIA ---")
  nome_arquivo_entrada = input("Digite o nome do arquivo criptografado: ")
  nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
  chave_criptografia = input("Digite a senha de descriptografia: ")
  
  descriptografar(nome_arquivo_entrada, nome_arquivo_saida, chave_criptografia)

else:
  print("Opção inválida. Encerrando.")