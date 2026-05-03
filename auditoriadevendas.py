# -------------------
# auditoria de vendas semanais
# -------------------

LIMITE_SEGURANCA = 10000.0  # variavel global

vendas1 = float(input("digite o valor da venda 1: "))
vendas2 = float(input("digite o valor da venda 2: "))
vendas3 = float(input("digite o valor da venda 3: "))


def analisar_vendas(venda1, venda2, venda3):
    global LIMITE_SEGURANCA

    # -------------------
    # CALCULO DA MEDIA
    # -------------------
    media = (venda1 + venda2 + venda3) / 3
    print(f"A média de vendas é: {media}")

    # -------------------
    # VERIFICACAO DE QUARENTENA
    # -------------------
    if media > LIMITE_SEGURANCA:
        print("SISTEMA EM QUARENTENA")

    # -------------------
    # DETECCAO DE DISCREPANCIA
    # -------------------
    vendas = [venda1, venda2, venda3]
    suspeito = False

    for venda in vendas:
        if venda > media * 5:
            suspeito = True
            break

    if suspeito:
        print("REVISÃO MANUAL NECESSÁRIA")

    # -------------------
    # ALTERACAO DO LIMITE
    # -------------------
    resposta = input("alterar o LIMITE_DE_SEGURANCA (sim/nao): ")

    if resposta.lower() == "sim":
        novo_limite = float(input("digite o novo limite de segurança: "))
        LIMITE_SEGURANCA = novo_limite
        print(f"novo limite de segurança definido: {LIMITE_SEGURANCA}")

    # -------------------
    # EXIBICAO DOS TIPOS
    # -------------------
    print(f"tipo de venda1: {type(venda1)}")
    print(f"tipo de venda2: {type(venda2)}")
    print(f"tipo de venda3: {type(venda3)}")
    print(f"tipo de LIMITE_SEGURANCA: {type(LIMITE_SEGURANCA)}")
    print(f"tipo de media: {type(media)}")
    print("-" * 40)


analisar_vendas(vendas1, vendas2, vendas3)