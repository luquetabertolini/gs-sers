import random
import time

TEMPERATURA_CRITICA = 80.0
ENERGIA_MINIMA = 20.0

central_energia = {
    "temperatura": 25.0,
    "energia": 100.0,
    "geracao_solar": 5.0,
    "consumo": 3.5,
    "comunicacao": "ESTAVEL",
    "setores": {
        "Suporte de Vida": "ATIVO",
        "Propulsao": "ATIVO",
        "Pesquisa Cientifica": "ATIVO",
        "Painel Solar": "ATIVO"
    }
}

historico_eventos = []


def registrar_evento(mensagem):
    horario = time.strftime("%H:%M:%S")
    evento = f"[{horario}] {mensagem}"
    historico_eventos.append(evento)
    print(evento)


def atualizar_sensores():
    central_energia["temperatura"] += round(random.uniform(-3.0, 5.0), 1)

    central_energia["geracao_solar"] = round(random.uniform(1.0, 8.0), 1)

    saldo = central_energia["geracao_solar"] - central_energia["consumo"]

    central_energia["energia"] += round(saldo * 1.5, 1)

    central_energia["energia"] = max(
        0.0,
        min(100.0, central_energia["energia"])
    )

    chance = random.random()

    if chance < 0.02:
        central_energia["comunicacao"] = "PERDIDA"
    elif chance < 0.07:
        central_energia["comunicacao"] = "INSTAVEL"
    else:
        central_energia["comunicacao"] = "ESTAVEL"

    if random.random() < 0.03:
        modulo = random.choice(
            list(central_energia["setores"].keys())
        )
        central_energia["setores"][modulo] = "FALHA"
        registrar_evento(
            f"Falha detectada no módulo {modulo}"
        )


def analisar_operacao():
    alerta = False

    print("\n--- SISTEMA AUTONOMO DE DECISAO ---")

    if central_energia["temperatura"] >= TEMPERATURA_CRITICA:
        print(
            f"ALERTA CRITICO: Temperatura elevada ({central_energia['temperatura']:.1f} °C)"
        )
        print(
            "AÇÃO: Resfriamento automático ativado."
        )

        central_energia["setores"]["Propulsao"] = "RESFRIAMENTO"

        central_energia["temperatura"] -= 12

        registrar_evento(
            "Sistema de resfriamento acionado"
        )

        alerta = True

    else:
        if central_energia["setores"]["Propulsao"] == "RESFRIAMENTO":
            central_energia["setores"]["Propulsao"] = "ATIVO"

    if central_energia["energia"] <= ENERGIA_MINIMA:
        print(
            f"ALERTA CRITICO: Energia em nível mínimo ({central_energia['energia']:.1f}%)"
        )

        print(
            "AÇÃO: Modo sustentável ativado."
        )

        central_energia["setores"]["Pesquisa Cientifica"] = "ECONOMIA"

        central_energia["consumo"] = 1.5

        registrar_evento(
            "Modo de economia energética ativado"
        )

        alerta = True

    else:
        if central_energia["setores"]["Pesquisa Cientifica"] == "ECONOMIA":
            central_energia["setores"]["Pesquisa Cientifica"] = "ATIVO"
            central_energia["consumo"] = 3.5

    if central_energia["comunicacao"] == "PERDIDA":
        print(
            "ALERTA: Comunicação com a Terra interrompida."
        )

        print(
            "AÇÃO: Busca automática de sinal."
        )

        registrar_evento(
            "Protocolo de recuperação de comunicação iniciado"
        )

        alerta = True

    if not alerta:
        print(
            "Todos os sistemas operam dentro dos parâmetros ideais."
        )


def exibir_painel():
    eficiencia = (
        central_energia["geracao_solar"]
        / central_energia["consumo"]
    ) * 100

    if central_energia["temperatura"] >= 80:
        nivel_alerta = "CRITICO"
    elif central_energia["temperatura"] >= 60:
        nivel_alerta = "ATENCAO"
    else:
        nivel_alerta = "NORMAL"

    print("\n====================================================")
    print("     CENTRO DE MONITORAMENTO ENERGETICO ESPACIAL")
    print("====================================================")

    print(
        f"Temperatura Interna : {central_energia['temperatura']:.1f} °C"
    )

    print(
        f"Nível de Energia    : {central_energia['energia']:.1f}%"
    )

    print(
        f"Geração Solar       : {central_energia['geracao_solar']:.1f} kW"
    )

    print(
        f"Consumo Atual       : {central_energia['consumo']:.1f} kW"
    )

    print(
        f"Eficiência Energética: {eficiencia:.1f}%"
    )

    print(
        f"Comunicação         : {central_energia['comunicacao']}"
    )

    print(
        f"Nível de Alerta     : {nivel_alerta}"
    )

    print("----------------------------------------------------")
    print("STATUS DOS MÓDULOS")

    for modulo, status in central_energia["setores"].items():
        print(f"{modulo}: {status}")

    print("====================================================")


def iniciar_monitoramento():
    print("Inicializando sistema inteligente de monitoramento...")
    time.sleep(2)

    try:
        while True:
            atualizar_sensores()
            exibir_painel()
            analisar_operacao()

            print("\nPróxima atualização em 3 segundos...")
            time.sleep(3)

    except KeyboardInterrupt:
        print("\n\nMONITORAMENTO ENCERRADO")

        print("\nRELATÓRIO FINAL")
        print(f"Energia Final: {central_energia['energia']:.1f}%")
        print(f"Temperatura Final: {central_energia['temperatura']:.1f} °C")
        print(f"Eventos Registrados: {len(historico_eventos)}")

        if historico_eventos:
            print("\nHISTÓRICO DE EVENTOS")
            for evento in historico_eventos:
                print(evento)


if __name__ == "__main__":
    iniciar_monitoramento()