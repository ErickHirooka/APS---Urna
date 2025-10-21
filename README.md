## **Introdução**

Este projeto foi desenvolvido como parte do curso de Ciência da Computação e tem como objetivo principal demonstrar a aplicação prática de técnicas fundamentais de criptografia e integridade de dados no contexto de sistemas de votação eletrônica (urnas).

O exercício consiste em processar dados brutos de uma eleição — incluindo informações da urna, dos candidatos e os votos registrados — aplicando mecanismos de segurança para garantir a **confidencialidade** e a **imutabilidade** do conteúdo.

## **🎯 Objetivo**

O principal objetivo desta solução é:

1. **Criptografar** o conteúdo dos arquivos de dados eleitorais para proteger as informações confidenciais contra acesso não autorizado (Confidencialidade).  
2. **Gerar um código hash** único para o arquivo criptografado, permitindo a verificação rápida e eficiente de que o arquivo não foi alterado após o processamento (Integridade).
3. **Não** utilizar nenhuma biblioteca auxiliar no processo.

## **🛠️ Componentes da Solução**

O projeto utiliza o Python para implementar duas funções de segurança:

| Componente | Função | Propósito |
| :---- | :---- | :---- |
| **Cifra XOR** | xor\_cifra() | Usada para criptografar e descriptografar o conteúdo do arquivo. |
| **Hash Simples (DJB2-like)** | simple\_hash() / hash\_file() | Usada para gerar um resumo numérico do arquivo, garantindo sua integridade. |

## **1\. Criptografia (Cifra XOR)**

A Cifra XOR (ou *Exclusive OR*) é um método simétrico e simples de criptografia.

### **Detalhes da Implementação:**

* **Operação:** A função xor\_cifra() realiza a operação binária XOR entre cada *byte* do texto de entrada e cada *byte* de uma chave.  
* **Chave:** A chave é repetida (ou estendida) ciclicamente para cobrir todo o comprimento do arquivo de entrada.  
* **Característica Central:** O método é a sua própria função de descriptografia. Aplicar a Cifra XOR novamente com a **mesma chave** reverte o texto cifrado ao seu estado original: (Texto XOR Chave) XOR Chave \= Texto.  
* **Modo Binário:** A função lê e escreve o conteúdo cifrado em **modo binário ('rb' e 'wb')** para evitar corromper *bytes* que não são caracteres UTF-8 válidos.

## **2\. Geração de Hash (DJB2 \- Hash Não-Criptográfico)**

Para garantir a integridade dos arquivos (prova de que os dados não foram adulterados), um valor de *hash* é calculado.

### **Detalhes da Implementação:**

* **Algoritmo:** Utilizamos uma implementação de *hash* simples inspirada na família de algoritmos **DJB2**, conhecida por sua rapidez e boa distribuição em tabelas *hash* não-criptográficas.  
* **Processamento de Arquivos:** A função hash\_file() é crucial. Ela:  
  * Abre o arquivo em modo binário ('rb').  
  * Lê o arquivo em **blocos (chunks)** de 4KB (4096 bytes).  
  * Atualiza incrementalmente o valor *hash* com cada bloco, garantindo que mesmo arquivos muito grandes possam ser processados sem sobrecarregar a memória.  
* **Integridade:** Qualquer alteração de um único *byte* no arquivo CSV (por exemplo, mudar um voto) resulta em um valor *hash* completamente diferente, denunciando a adulteração.

## **💻 Como Utilizar**

1. **Entrada:** Fornecer o caminho e nome dos arquivos de dados da urna (ex: votos.csv).  
2. **Chave:** Inserir a chave de criptografia (string de texto).  
3. **Processamento:** O programa:  
   * Lê o arquivo de entrada.  
   * Criptografa o conteúdo usando a chave XOR.  
   * Salva o conteúdo criptografado em um novo arquivo (em modo binário).  
   * Calcula o *hash* do **arquivo criptografado** para verificar sua integridade futura.
