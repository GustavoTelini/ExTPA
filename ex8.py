nome = str(input('Digite seu nome: '))
cont = 1
media = 0
while cont < 4:
    nota = float(input('Digite a nota: '))
    cont = cont + 1
    media = media + nota
media = media /3
if media >= 7:
    print (f'Parabéns {nome}! Você foi aprovado com média de {media}')
elif media < 7 and media >= 5:
    print (f'{nome} sua média foi de {media} e você está de recuperação.')
else:
    print (f'{nome}, você está reprovado.')
    
