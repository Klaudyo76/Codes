import random

def realizar_sorteio():
    numeros_sorteados = []
    while len(numeros_sorteados) < 6:
        numero = random.randint(1, 59)
        if numero not in numeros_sorteados:
            numeros_sorteados.append(numero)
    
    return numeros_sorteados

sorteio = realizar_sorteio()
print("Números sorteados:", sorteio)
