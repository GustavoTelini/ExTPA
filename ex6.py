val1 = float(input('Digite o valor do primeiro produto: '))
val2 = float(input('Digite o valor do segundo produto: '))

desc1 = val1 * 8/100
desc2 = val2 * 11/100
vf1 = val1 - desc1 
vf2 = val2 - desc2
print (f'O valor do primeiro produto com desconto de 8% é R${vf1} e o desconto de 11% no segundo é R${vf2}')