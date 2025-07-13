def subRetangulos(qnt_linhas, qnt_colunas, perimetro_max):
    if perimetro_max % 2 != 0:
        perimetro_max -= 1
    
    canditados_wh = []

    for altura in range(int(perimetro_max/2)):
        for largura in range(int(perimetro_max/2)):
            if altura + largura == (perimetro_max / 2) and largura != altura:
                if altura <= qnt_linhas and largura <= qnt_colunas:      
                    canditados_wh.append((largura, altura))
    
    return canditados_wh

def encontrarTesouros(perimetro_max, qnt_linhas, qnt_colunas, mapa):
    possibilidades = subRetangulos(qnt_linhas, qnt_colunas, perimetro_max)    

    max_tesouros = 0

    for largura, altura in possibilidades:
        for linha in range(qnt_linhas - altura + 1):
            for coluna in range(qnt_colunas - largura + 1):  
                tesouros = 0
                for x in range(linha, linha + altura):
                    for y in range(coluna, coluna + largura):
                        if mapa[x][y] == 'X':
                            tesouros += 1
                max_tesouros = max(max_tesouros, tesouros)
    
        
    return max_tesouros

qnt_linhas, qnt_colunas = [int(i) for i in input().split()]

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

print(encontrarTesouros(perimetro_max, qnt_linhas, qnt_colunas, mapa))