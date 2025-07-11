def subRetangulos(perimetro_max):
    if perimetro_max % 2 != 0:
        perimetro_max -= 1
    
    canditados_wh = []

    for altura in range(int(perimetro_max/2)):
        for largura in range(int(perimetro_max/2)):
            if altura + largura == (perimetro_max / 2) and largura != altura:      
                canditados_wh.append((largura, altura))
    
    print(canditados_wh)
    return canditados_wh

def testesHorizontais(perimetro_max, qnt_colunas, mapa):
    possibilidades = subRetangulos(perimetro_max)

    tesouros_encontrados = []

    
    for possibilidade in possibilidades:
        for altura in range(possibilidade[1]):
            index = 0
            # if possibilidade[0] > possibilidade[1]:
            while index < qnt_colunas - possibilidade[0]:
                tesouros = 1
                for linha in mapa:
                    for posicao in range(index, possibilidade[0] + index):
                        if linha[posicao] == 'X':
                            tesouros += 1
                    tesouros_encontrados.append(tesouros)
                index += 1
    print(tesouros_encontrados)


        








qnt_linhas = int(input("Quantidade de linhas: "))
qnt_colunas = int(input("Quantidade de colunas: "))

mapa = []

while qnt_linhas:
    linha = input("Insira a linha: ").split()
    if len(linha) == qnt_colunas:
        mapa.append(linha)
        qnt_linhas -= 1
    else:
        print("Erro, tente novamente.")

perimetro_max = int(input("Insira o perimetro máximo: "))

testesHorizontais(perimetro_max, qnt_colunas, mapa)
