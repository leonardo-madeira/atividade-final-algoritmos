def remover(dia, hora_inicio, hora_fim, semana:list):
    hora_inicio = hora_inicio - 8
    hora_fim = hora_fim - 8

    dias_dict = {
        'segunda': 0,
        'terça': 1,
        'quarta': 2,
        'quinta': 3,
        'sexta': 4
    }

    for index, elemento in enumerate(semana):
        if dias_dict[dia] == index:
            for i in range(hora_inicio, hora_fim):
                semana[index][i] = 'Livre'
    
    return semana

def adicionar(atividade, qnt_horas, semana:list):
    possibilidade = False
    for posicao, elemento in enumerate(semana):
        index = 0
        while index < 10:
            verificador = True

            if index > len(elemento) - qnt_horas:
                break

            for compromiso in elemento[index:(qnt_horas + index)]:
                if compromiso != 'Livre':
                    verificador = False
            
            if verificador:
                for momento, horario in enumerate(elemento[index:qnt_horas + index]):
                    semana[posicao][momento + index] = atividade.capitalize()
                possibilidade = True
                break

            index += 1

        if possibilidade:
            break
    
    if not possibilidade:
        return False
    else:
        return semana

segunda = input("Insira a programação de Segunda-Feira: ").split()
terca = input("Insira a programação de Terça-Feira: ").split()
quarta = input("Insira a programação de Quarta-Feira: ").split()
quinta = input("Insira a programação de Quinta-Feira: ").split()
sexta = input("Insira a programação de Sexta-Feira: ").split()

semana = [segunda, terca, quarta, quinta, sexta]
alocamento_indisponivel = []

movimentos = int(input("Insira quantos movimentos serão realizados:"))

while movimentos:
    acao = input(f"Insira o {movimentos}° movimento: ").lower().split()

    if acao[0] == 'remover':
        if len(acao[1:]) == 3:
            semana = remover(acao[1], int(acao[2]), int(acao[3]), semana)
            movimentos -= 1
    elif acao[0] == 'adicionar':
        if len(acao[1:]) == 2:
            verificador = adicionar(acao[1], int(acao[2]), semana)
            if verificador:
                semana = verificador
            else:
                alocamento_indisponivel.append(acao[1])
            movimentos -= 1


horario = ['08-09', '09-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18']

if alocamento_indisponivel:
    for elemento in alocamento_indisponivel:
        print(f"Não foi possível alocar a atividade {elemento.capitalize()}")

print(f"{'Horário':<13}{'Segunda':<13}{'Terça':<13}{'Quarta':<13}{'Quinta':<13}{'Sexta':<13}")

index = 0
while index < 10:
    print(f'{horario[index]:<13}', end="")
    for elemento in semana:
        print(f"{elemento[index]:<13}", end="")
    print()
    index += 1