cont = 1
maior = 0
num = 0
while cont <= 10:
    num = int(input('Digite um número: '))
    if maior < num:
        maior = num
    cont +=1
print (maior)