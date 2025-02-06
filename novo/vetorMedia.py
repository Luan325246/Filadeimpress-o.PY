# faça um programa que vai ler 5 notas de prova e armazenar em uma lista. Imprimir a media geral da turma

#criando um vetor
nota = []

# criando uma esrutura do tipo para que vai receber 5 
# elementos, se quisesse que recebesse mais elementos é so trocar dentro do parenteses
for i in range(5):
    # estamos chamndo aqui o float antes do input pois nossos dados sao do tipo real
    notaUnitario = float(input("digite a nota ddo aluno: "))
    # O append esta incrementando o vtor atras do final da lista, o que 
    # define a estrutura de dados do tipo lista é isso aqui!!
    nota.append(notaUnitario)

#criando a variavel media
media = 0    

# o item no vai ser quem vai passar em todos os itens o vetor,
#  e vai colocalos dentro da media, que ira somando item por item ate finalizar o vetor nota.

for no in nota:
    media = media + no

media = media/5

print(f"media geral dos alunos{media}")
