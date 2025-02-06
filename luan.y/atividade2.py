import math

numero = int(input("Digite um numero: "))

if numero > 0:
    raiz = math.sqrt(numero)

    print(f" Raiz quadrada de {numero} é {raiz:.2f}")
else:
    print("Não é possível calcular a raiz de um número negativo")