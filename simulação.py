while True:
    print("-------------------------------")
    print("  Seja bem-vindo(a) ao Mybank  ")
    print("   SIMULADOR DE INVESTIMENTO   ")
    print("-------------------------------")

#opção de título
    print("Títulos disponíveis:")
    print("1 - Tesouro PREFIXADO 2024")
    print("2 - Tesouro PREFIXADO 2026")

#investimento
    titulo = int(input("Escolha um título: "))
    val_ir = 0
    mes1 = 32
    mes2 = 50
    val1 = float(input("\n Valor que irá inserir inicialmente "))
    valor = float(input("Valor que você irá investir mensalmente: "))

#título 1
    if titulo == 1:
        
        val2 = valor * mes1 + val1

#valor total
        val3 = val2 * 12.38/100
        b3 = val2 * 2.5/100
        valtotal = val2 + val3 + b3
        print(f"\n {valtotal}")

#imposto de 7,5%
        if valtotal > 1903.98 and valtotal < 2826.66:
            ir = valtotal * 7.5/100
            val_ir = valtotal + ir

#imposto de 15%
        elif valtotal> 2826.65 and valtotal < 3751.06:
            ir = valtotal * 15/100
            val_ir = valtotal + ir

        #imposto de 22,5%
        elif valtotal > 3751.05 and valtotal < 4664.69:
            ir = valtotal * 22.5/100
            val_ir = valtotal + ir

        # imposto de 27,5%
        elif valtotal > 4664.68:
            ir = valtotal * 27.5/100
            val_ir = valtotal + ir
#calculo
        valliquido = val_ir - ir - b3
 
#título 2
    else: 
        val1 = valor * mes2 + val1

#valor total
        val3 = val2 * 12.30/100
        b3 = val2 * 2.5/100
        valtotal = val2 + val3 + b3

#imposto de 7,5%
        if valtotal > 1903.98 and valtotal < 2826.66:
            ir = valtotal * 7.5/100
            val_ir = valtotal + ir

#imposto de 15%
        elif valtotal> 2826.65 and valtotal < 3751.06:
            ir = valtotal * 15/100
            val_ir = valtotal + ir

        #imposto de 22,5%
        elif valtotal > 3751.05 and valtotal < 4664.69:
            ir = valtotal * 22.5/100
            val_ir = valtotal + ir

        # imposto de 27,5%
        elif valtotal > 4664.68:
            ir = valtotal * 27.5/100
            val_ir = valtotal + ir
#calculo
        valliquido = val_ir - ir - b3
#resultado da simulação
    print("------------------------------")
    print("    RESULTADO DA SIMULAÇÃO    ")
    print("------------------------------")
    print(f"Valor inicial: {val1}")
    if titulo == 1:
        print(f"Aportes de {valor}  por {mes1} meses")
    else:
        print(f"Aportes de {valor}  por {mes2} meses")
    print(f"Valor total investido {val2}")
    print("------------------------------")
    print(f"Valor total: {val_ir}")
    print(f"I.R.: {ir}")
    print(f"Taxa da B3: {b3}")
    print(f"Valor líquido: {valliquido}")
    print("------------------------------")
    opcao = str(input("\n Deseja continuar a simulação? [s/n]: "))
    if opcao == 'n':
        break