"""
3. faça um programa que recebe tres valores e apresente a soma dos quadrados dos valores lidos.
"""

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
valor3 = int(input('Informe o terceiro valor: '))

soma = (valor1 * valor1) + (valor2 ** valor2) + (valor3 * valor3)

print(f"a soma dos quadrados dos valores {valor1} com {valor2} e {valor3} é {soma}")  # f-string para concaten