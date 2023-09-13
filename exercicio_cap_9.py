import random
import datetime

# Função para calcular o tempo
# - O tempo de carregar cada mercadoria é X minutos
#   X=resto da divisão dos últimos 2 dígitos do seu RM por 3 somado a 1
#   escolha o RM de um dos colegas de seu grupo; anote qual RM foi escolhido
def calculo_tempo_descarregamento_mercadoria():
    rm = 42  # RM93842
    x = (rm % 3) + 1
    return x


# Gera uma ordem de carga aleatória de acordo com o exercício
# - Por questão de acomodação no local, a fila de carga pode conter apenas 15 mercadorias por vez
def gerar_ordem_carga():
    max_mercadorias = 15
    return random.sample(range(1, max_mercadorias + 1), random.randint(1, max_mercadorias))


def carga_mercadorias():
    fila_carga = gerar_ordem_carga()
    motorista = "Motorista"
    ajudante = "Ajudante"
    minutos_acumulados = 1
    dez_iter = 0
    minutos = 1
    hora_inicio = datetime.datetime(2023, 9, 12,20, 10)  # Hora 20:10
    hora_atual = hora_inicio


    print("Início da carga às 20h10")
    while fila_carga:
        dez_iter += 1
        # - Para agilizar o processo de carga, são preparadas 3 mercadorias simultaneamente
        #   (pode ser menos apenas no momento em que a fila tiver menos do que 3 mercadorias);
        if len(fila_carga) >= 3:
            mercadorias_a_carregar = fila_carga[:3]
        elif len(fila_carga) >= 2:
            mercadorias_a_carregar = fila_carga[:2]
        else:
            mercadorias_a_carregar = fila_carga

        print(f"fila atual de mercadoria {fila_carga}")

        if len(fila_carga) > 0:
            for mercadoria in mercadorias_a_carregar:
                tempo_carga = calculo_tempo_descarregamento_mercadoria()
                hora_atual = hora_inicio + datetime.timedelta(minutes=minutos_acumulados)
                hora_formatada = hora_atual.strftime("%H:%M:%S")
                print(f"{motorista} e {ajudante} carregando mercadoria {mercadoria} Horário Atual: {hora_atual}")
                minutos_acumulados += 1

                if minutos >= 2:
                    print("Mercadoria acrescentada!")
                    fila_carga.append(len(fila_carga) + 1)
                    minutos -= 2

                minutos += tempo_carga
                fila_carga.remove(mercadoria)

        # De acordo com o exercício a cada 10 iterações acrescenta 1 minuto!
        if dez_iter == 10:
            dez_iter = 0
            minutos += 1
            print(f"Tempo de espera após a primeira mercadoria: {minutos} min")

    #  tempo_descarregamento = datetime.timedelta(minutes=minutos_acumulados)
    hora_final = hora_inicio + datetime.timedelta(minutes=minutos_acumulados)
    hora_formatada = hora_final.strftime("%H:%M:%S")
    print(f"Final da carga às {hora_formatada}")


# Inicia a simulação
carga_mercadorias()