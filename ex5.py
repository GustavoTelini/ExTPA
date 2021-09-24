val = int(input('Digite um valor: '))
cont = 1
num = val
while cont < val:
    num = cont * num
    cont = cont + 1
print (f'{val}! é igual a {num}.')