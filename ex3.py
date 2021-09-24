cont = 1
num = 0
while cont <= 10:
    idade = int(input('Digite o ano de nascimento: '))
    maior = 2021 - idade 
    if maior >= 18: 
        num = num + 1
    cont = cont + 1
print (f'{num} pessoas são maiores de idade.')