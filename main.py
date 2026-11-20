import math




def fazer_palavras(qtd_palavras):
    palavras = []
    for i in range(0,qtd_palavras):
        palavra = f'palavra{i+1}'
        palavras.append(palavra)
    return " ".join(palavras)
    
texto = fazer_palavras(0)

def juntar_texto(texto: list[str]):
    return ' '.join(texto)



def dividir_texto(texto: str, tamanho: int): 
    
    if tamanho <= 0 or texto.strip() == '':
        raise ValueError('tamanho está menor que 0 e/ou texto está vazio') 
    chunks = []
    texto_separado = texto.strip().split()
    repeticoes = math.ceil(len(texto_separado)/tamanho)
    
    for i in range(repeticoes):
        texto_junto=juntar_texto(texto_separado[tamanho*i:tamanho*(i+1)])
        chunks.append(texto_junto)
        
    
    return chunks
    

print(dividir_texto('    ',10))