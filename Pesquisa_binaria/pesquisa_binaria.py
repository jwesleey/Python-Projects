# Pesquisa Binaria para ser utilizada em lista ordenada para encontrar determinado valor

def pesquisa_binaria(lista, item):     #  declaração da funçÕ
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None       # fim da função

minha_lista = [1, 3, 6, 7, 14]       # lista ordenada

print(pesquisa_binaria(minha_lista, 14))
print(pesquisa_binaria(minha_lista, 5))