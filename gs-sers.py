import random
import time

LIMITE_TEMPERATURA = 80.0
LIMITE_ENERGIA = 20.0

estacao = {
    "temperatura": 85.0,
    "energia": 10.0,
    "geracao_solar": 5.0,
    "consumo": 3.5,
    "comunicacao": "ESTAVEL",
    "modulos": {
        "Suporte de Vida": "ATIVO",
        "Propulsao": "ATIVO",
        "Pesquisa Cientifica": "ATIVO",
        "Painel Solar": "ATIVO"
    }
}

historico = []


def registrar_evento(texto):
    horario = time.strftime("%H:%M:%S")
    evento = f"[{horario}] {texto}"
    historico.append(evento)
    print(evento)


def atualizar_sensores():

    estacao["temperatura"] += round(
        random.uniform(-3.0, 5.0),
        1
    )

    estacao["geracao_solar"] = round(
        random.uniform(1.0, 8.0),
        1
    )

    saldo = (
        estacao["geracao_solar"]
        - estacao["consumo"]
    )

    estacao["energia"] += round(
        saldo * 1.5,
        1
    )

    estacao["energia"] = max(
        0.0,
        min(100.0, estacao["energia"])
    )

    chance = random.random()

    if chance < 0.02:
        estacao["comunicacao"] = "PERDIDA"

    elif chance < 0.07:
        estacao["comunicacao"] = "INSTAVEL"

    else:
        estacao["comunicacao"] = "ESTAVEL"

    if random.random() < 0.03:

        modulo = random.choice(
            list(estacao["modulos"].keys())
        )

        estacao["modulos"][modulo] = "FALHA"

        registrar_evento(
            f"Falha detectada no módulo {modulo}"
        )


def calcular_risco():

    risco = 0

    if estacao["temperatura"] > 60:
        risco += 30

    if estacao["energia"] < 40:
        risco += 40

    if estacao["comunicacao"] == "INSTAVEL":
        risco += 15

    if estacao["comunicacao"] == "PERDIDA":
        risco += 30

    return min(risco, 100)


def gerenciamento_inteligente():

    if estacao["energia"] < 40:

        estacao["modulos"]["Pesquisa Cientifica"] = "ECONOMIA"

        registrar_evento(
            "Pesquisa Científica colocada em modo economia"
        )

    if estacao["energia"] < 25:

        estacao["modulos"]["Painel Solar"] = "MAXIMA GERACAO"

        registrar_evento(
            "Painel Solar priorizado para geração máxima"
        )


def analisar_operacao():

    alerta = False

    print("\n--- SISTEMA AUTÔNOMO DE DECISÃO ---")

    if estacao["temperatura"] >= LIMITE_TEMPERATURA:

        print(
            f"ALERTA CRÍTICO: Temperatura elevada ({estacao['temperatura']:.1f} °C)"
        )

        print(
            "AÇÃO: Resfriamento automático ativado."
        )

        estacao["modulos"]["Propulsao"] = "RESFRIAMENTO"

        estacao["temperatura"] -= 12

        registrar_evento(
            "Sistema de resfriamento acionado"
        )

        alerta = True

    else:

        if (
            estacao["modulos"]["Propulsao"]
            == "RESFRIAMENTO"
        ):
            estacao["modulos"]["Propulsao"] = "ATIVO"

    if estacao["energia"] <= LIMITE_ENERGIA:

        print(
            f"ALERTA CRÍTICO: Energia baixa ({estacao['energia']:.1f}%)"
        )

        print(
            "AÇÃO: Modo sustentável ativado."
        )

        estacao["modulos"]["Pesquisa Cientifica"] = "ECONOMIA"

        estacao["consumo"] = 1.5

        registrar_evento(
            "Modo de economia energética ativado"
        )

        alerta = True

    else:

        if (
            estacao["modulos"]["Pesquisa Cientifica"]
            == "ECONOMIA"
        ):
            estacao["modulos"]["Pesquisa Cientifica"] = "ATIVO"
            estacao["consumo"] = 3.5

    if estacao["comunicacao"] == "PERDIDA":

        print(
            "ALERTA: Comunicação com a Terra interrompida."
        )

        print(
            "AÇÃO: Busca automática de sinal."
        )

        registrar_evento(
            "Protocolo de recuperação iniciado"
        )

        alerta = True

    if not alerta:

        print(
            "Todos os sistemas operam normalmente."
        )


def exibir_painel():

    eficiencia = (
        estacao["geracao_solar"]
        / estacao["consumo"]
    ) * 100

    risco = calcular_risco()

    if estacao["temperatura"] >= 80:
        nivel = "CRÍTICO"

    elif estacao["temperatura"] >= 60:
        nivel = "ATENÇÃO"

    else:
        nivel = "NORMAL"

    print("\n===================================================")
    print("      CENTRAL DE MONITORAMENTO ESPACIAL")
    print("===================================================")

    print(
        f"Temperatura         : {estacao['temperatura']:.1f} °C"
    )

    print(
        f"Energia             : {estacao['energia']:.1f}%"
    )

    print(
        f"Geração Solar       : {estacao['geracao_solar']:.1f} kW"
    )

    print(
        f"Consumo             : {estacao['consumo']:.1f} kW"
    )

    print(
        f"Eficiência Energética: {eficiencia:.1f}%"
    )

    print(
        f"Comunicação         : {estacao['comunicacao']}"
    )

    print(
        f"Nível de Alerta     : {nivel}"
    )

    print(
        f"Índice de Risco     : {risco}%"
    )

    print("---------------------------------------------------")
    print("STATUS DOS MÓDULOS")

    for modulo, status in estacao["modulos"].items():
        print(f"{modulo}: {status}")

    print("===================================================")


def iniciar_monitoramento():

    print(
        "Inicializando sistema inteligente..."
    )

    time.sleep(2)

    try:

        while True:

            atualizar_sensores()

            gerenciamento_inteligente()

            exibir_painel()

            analisar_operacao()

            print(
                "\nPróxima atualização em 3 segundos..."
            )

            time.sleep(3)

    except KeyboardInterrupt:

        print("\n\nMONITORAMENTO ENCERRADO")

        print("\nRELATÓRIO FINAL")

        print(
            f"Energia Final: {estacao['energia']:.1f}%"
        )

        print(
            f"Temperatura Final: {estacao['temperatura']:.1f} °C"
        )

        print(
            f"Eventos Registrados: {len(historico)}"
        )

        if historico:

            print("\nHISTÓRICO DE EVENTOS")

            for evento in historico:
                print(evento)


if __name__ == "__main__":
    iniciar_monitoramento()