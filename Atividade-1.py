def coletorPremios(qnt_premios):
    premios = []
    contador = 1

    while qnt_premios:
        try:
            validador = True
            id, nome = input(f"Insira o {contador}° premio:").split()

            if id.isnumeric():
                for elemento in premios:
                    if id in elemento:
                        validador = False
            else:
                validador = False

            if not validador:
                print("ID inválido, tente novamente.")
            else:
                premios.append([id, nome])
                contador += 1
                qnt_premios -= 1

        except ValueError:
            print("Formato inválido, insira as informações no seguinte formato:")
            print("ID NOME\n EXEMPLO: 201 BICICLETA")
    
    return premios

def sorteio(premios:list, forcas:list):
    premios_sorteados = []
    qnt_premios = len(premios)
    posicao_anterior = []

    for forca in forcas:
        verificador = True
        forca_inicial = forca
        contador = 0

        while verificador:
            
            if forca <= qnt_premios:
                index = forca - 1
            elif forca / 2 == qnt_premios:
                index = qnt_premios - 1
            elif forca % qnt_premios == 0:
                while forca > qnt_premios:
                    resto = forca % qnt_premios
                    forca = forca // qnt_premios
                index = (forca + resto) - 1
            elif forca % qnt_premios != 0:
                index = (forca % qnt_premios) - 1

            if index > 0:
                for i in range(index + 1):
                    premios.append(premios[i])
                for i in range(index + 1):
                    premios.pop(0)
            else:
                premios.append(premios[0])
                premios.pop(0)

            
            if not premios[-1] in premios_sorteados:
                premios_sorteados.append(premios[-1])
                verificador = False
            else:
                if forca >= 1: 
                    contador += 1
                    forca = forca_inicial - contador

    return premios_sorteados
    
qnt_premios = int(input("Insira a quantidade de premios: "))
premios = coletorPremios(qnt_premios)

qnt_sorteios = int(input("Insira a quantidade de sorteios: "))
forcas = [int(i) for i in input("Insira das forças: ").split() if i.isnumeric()]

if len(forcas) == qnt_sorteios:
    resultado = sorteio(premios, forcas)
    for elemento in resultado:
        print(f"{elemento[0]}-{elemento[1]}", end= " ")
else:
    print("Quantidade de forças inválida.")