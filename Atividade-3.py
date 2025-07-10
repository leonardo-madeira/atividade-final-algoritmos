def estrategiaIngeua(influencers, orcamento):
    influecers_ordenados = sorted(influencers, key=lambda x: x[0])
    print()
    soma = 0
    index = 0

    while index <= len(influecers_ordenados):
        teste = soma + float(influecers_ordenados[index][0]) 
        if teste < orcamento:
            soma = teste
        else:
            break
        index += 1
    
    controle = 0
    seguidores = []
    while controle < index:
        seguidores += influecers_ordenados[controle][1:]
        controle += 1
    
    seguidores = len(list(set(seguidores)))

    return [soma, seguidores]

def estrategiaAtual(influencers, orcamento):
    custo_beneficio = []

    for index, influenciador in enumerate(influencers):
        razao = influenciador[0] / len(influenciador[1:])
        custo_beneficio.append([index, razao])
    
    custo_beneficio = sorted(custo_beneficio, key=lambda x: x[1])



orcamento = float(input("Insira o orçamento máximo"))
qnt_influencers = int(input("Insira a quantidade de influencers: "))

influencers = []

for i in range(qnt_influencers):
    entrada = [i for i in input().split(",")]
    influencers.append(entrada)

# estrategiaIngeua(influencers, orcamento)
estrategiaAtual(influencers, orcamento)

