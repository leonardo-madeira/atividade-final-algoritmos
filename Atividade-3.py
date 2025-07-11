def estrategiaIngeua(influencers, orcamento):
    influecers_ordenados = sorted(influencers, key=lambda x: x[0])
    soma = 0
    index = 0

    for index, elemento in enumerate(influecers_ordenados):
        teste = soma + float(elemento[0])
        if teste <= orcamento:
            soma = teste
        else:
            break
    
    controle = 0
    seguidores = []
    while controle < index:
        seguidores += influecers_ordenados[controle][1:]
        controle += 1
    
    seguidores = len(list(set(seguidores)))

    return [str(soma), str(seguidores)]


def estrategiaAtual(influencers, orcamento):
    custo_beneficio = []
    influencers_selecionados = []

    for index, influenciador in enumerate(influencers):
        razao = float(influenciador[0]) / len(influenciador[1:])
        custo_beneficio.append([index, razao])
    
    custo_beneficio = sorted(custo_beneficio, key=lambda x: x[1])

    for elemento in custo_beneficio:
        for index, influencer in enumerate(influencers):
            if elemento[0] == index:
                influencers_selecionados.append(influencer)
    
    soma = 0
    seguidores = []
    for elemento in influencers_selecionados:
        teste = soma + float(elemento[0])
        if teste <= orcamento:
            soma = teste
            seguidores += elemento[1:]
    
    seguidores = len(list(set(seguidores)))

    return [str(soma), str(seguidores)]


def estrategiaNova(influencers, orcamento):
    
    alcancados = []
    contratados = []

    primeiro_contradado = []
    for index, influenciador in enumerate(influencers):
        custo = float(influenciador[0]) / len(influenciador[1:]) 
        primeiro_contradado.append([index, custo])
    primeiro_contradado = sorted(primeiro_contradado, key= lambda x: x[1])[0][0]

    alcancados = influencers[primeiro_contradado][1:]
    contratados.append([primeiro_contradado, float(influencers[primeiro_contradado][0])])

    soma = 0
    while True:

        menor_custo = []
        for index, influenciador in enumerate(influencers):
            verificador = True
            contador = 0
            for elemento in contratados:
                if index == elemento[0]:
                    verificador = False
            if verificador:
                for seguidor in influenciador[1:]:
                    if not seguidor in alcancados:
                        contador += 1
                if contador > 0:
                    custo = float(influenciador[0]) / contador
                    menor_custo.append([index, custo])


        if menor_custo:
            menor_custo = sorted(menor_custo, key= lambda x: x[1])[0][0]
        

            candidato = float(influencers[menor_custo][0])

            teste = sum(i[1] for i in contratados) + candidato
            if teste <= orcamento:
                soma = teste
            else:
                break

            contratados.append([menor_custo, float(influencers[menor_custo][0])])
            alcancados = alcancados + influencers[menor_custo][1:]

        else:
            break

    seguidores = len(list(set(alcancados)))

    return [str(soma), str(seguidores)]

orcamento = float(input("Insira o orçamento máximo"))
qnt_influencers = int(input("Insira a quantidade de influencers: "))

influencers = []

for i in range(qnt_influencers):
    entrada = [i for i in input("Insira o influenciador: ").split(",")]
    influencers.append(entrada)

ingenua = (", ").join(estrategiaIngeua(influencers, orcamento))
atual =  (", ").join(estrategiaAtual(influencers, orcamento))
nova = (", ").join(estrategiaNova(influencers, orcamento))

print("Estratégia Ingênua: ",ingenua)
print("Estratégia Atual: ", atual)
print("Estratégia Nova: ", nova)
