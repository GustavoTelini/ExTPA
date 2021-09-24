val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))
cont = 1
if val1 < val2:
    while cont < val2:
        cont = cont + 1
        if cont > val1 and cont < val2:
            print (cont)
elif val2 < val1:
    while cont < val1:
        cont = cont + 1
        if cont > val2 and cont < val1:
            print (cont)