"""Vamos fazer um programa que leia 10 numeros reais e os armazene em uma linha
calcule e mostre:
a quantidade de numeros negativos
a soma dos numeros positivos"""

numero = []

for i in range(10):
    numerounitario = float(input("digite a nota ddo aluno: "))
    numero.append(numerounitario)    

soma_positivos = 0
quantidade_negativos = 0

for numerounitario in numero:
    if numerounitario < 0:
        quantidade_negativos += 1
    if numerounitario > 0:
        soma_positivos += numerounitario

print(f"Quantidade de numeros negativos: {quantidade_negativos}, e a soma dos numeros positivos é: {soma_positivos}")



    
