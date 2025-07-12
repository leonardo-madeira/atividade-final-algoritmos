def subRetangulos(qnt_linhas, qnt_colunas, perimetro_max):
    if perimetro_max % 2 != 0:
        perimetro_max -= 1
    
    canditados_wh = []

    for altura in range(int(perimetro_max/2)):
        for largura in range(int(perimetro_max/2)):
            if altura + largura == (perimetro_max / 2) and largura != altura:
                if altura <= qnt_linhas and largura <= qnt_colunas:      
                    canditados_wh.append((largura, altura))
    
    print(canditados_wh)
    return canditados_wh

def testesHorizontais(perimetro_max, qnt_linhas, qnt_colunas, mapa):
    possibilidades = subRetangulos(qnt_linhas, qnt_colunas, perimetro_max)

    matrizes_possiveis = []
    tesouros_encontrados = []

    
    # for possibilidade in possibilidades:
    #     for altura in range(possibilidade[1]):
    #     # if possibilidade[0] > possibilidade[1]:
    #         index = 0
    #         while index <= qnt_colunas - possibilidade[0]:
    #             for linha in mapa:
    #                 tesouros = 0
    #                 for posicao in range(index, possibilidade[0] + index):
    #                     if linha[posicao] == 'X':
    #                         tesouros += 1
    #                 tesouros_encontrados.append(tesouros)
    #             index += 1
    # print(tesouros_encontrados)

    # for possibilidade in possibilidades:
    #     altura = possibilidade[1]
    #     largura = possibilidade[0]
    #     print("Largura: ", largura)
    #     print("Altura: ", altura)
    #     maximo = (qnt_linhas - (altura - 1))

    #     ##### Horizontal
    #     # if largura > altura:
    #     for y in range(altura):
    #         tesouros = 0

    #         for linha in mapa[y:(maximo + y)]:

    #             ## FAZER MAIS UM LOOP AQUI DENTRO PERCORRENDO O SLICE DA HORIZONTAL AGORA
    #             for posicao in linha:
    #                 if posicao == 'X':
    #                     tesouros += 1
    #         tesouros_encontrados.append(tesouros)
    #     print(tesouros_encontrados)

    # for possibilidade in possibilidades:
    #     altura = possibilidade[1]
    #     largura = possibilidade[0]
    #     maximo_altura = (qnt_linhas - altura)
    #     maximo_largura = (qnt_colunas - largura)

    #     altura_atual = 0
    #     while altura_atual <= maximo_altura:
    #         for y in range(maximo_altura):
    #             for x in range(largura):
    #                 # if mapa[x][y] == "X":
    #                 #     print("X")
    #                 # print(mapa[x][y], end=" ")

    #                 for linha in mapa[altura_atual: (altura + y)]
    #             print()
    #         altura_atual += 1

    for possibilidade in possibilidades:
        altura = possibilidade[1]
        largura = possibilidade[0]
        maximo_altura = (qnt_linhas - altura)
        maximo_largura = (qnt_colunas - largura)
                        
        altura_atual = 0
        while altura_atual <= maximo_altura:
            matrix_temp = []
            for index in range(largura):
                matrix_temp.append(mapa[altura_atual][index: largura + index])
            matrizes_possiveis.append(matrix_temp)
            

            altura_atual += 1
        print(matrizes_possiveis)

        



        # for indexY in range(len(matriz)):
            # for indexX in range(len(matriz)):
                # print(matriz[indexX][indexY], end=" ")
            # print()


qnt_linhas = int(input("Quantidade de linhas: "))
qnt_colunas = int(input("Quantidade de colunas: "))

controle_linhas = qnt_linhas

mapa = []

while controle_linhas:
    linha = input("Insira a linha: ").split()
    if len(linha) == qnt_colunas:
        mapa.append(linha)
        controle_linhas -= 1
    else:
        print("Erro, tente novamente.")

perimetro_max = int(input("Insira o perimetro máximo: "))

testesHorizontais(perimetro_max, qnt_linhas, qnt_colunas, mapa)