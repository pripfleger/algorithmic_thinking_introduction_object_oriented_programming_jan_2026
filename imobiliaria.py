import os

def quartos(opcao_moradia, qtdade_quartos):
    if opcao_moradia == "apartamento" and qtdade_quartos == "1":
        return  700
    elif opcao_moradia == "apartamento" and qtdade_quartos == "2":
        return 700 + 200
    elif opcao_moradia == "casa" and qtdade_quartos == "1":
        return 900
    elif opcao_moradia == "casa" and qtdade_quartos == "2":
        return 900 + 250
    else:
        print("Erro no processamento!")

def garagem_geral(orcamento, garagem):
    while garagem != "S" and garagem != "N":
        print("Não identificamos sua escolha!")
        garagem = input("Digite novamente! Você deseja uma vaga de garagem? (S)sim ou (N)não ").upper()
        
    if garagem == "N":
        return orcamento
    elif garagem == "S":
        return orcamento + 300
    else:
        print("Erro no processamento!")

def garagem_estudio(orcamento, garagem):
    while garagem != "S" and garagem != "N":
        print("Não identificamos sua escolha!")
        garagem = input("Digite novamente! Você deseja uma vaga de garagem? (S)sim ou (N)não ").upper()
        
    if garagem == "S":
        orcamento += 250
        quer_vaga_extra = input("Deseja adicionar vaga(s) extra(s)? (S) sim ou (N) não ").upper()
        orcamento, vaga_extra = vaga_extra_garagem(orcamento, quer_vaga_extra)
        return orcamento, vaga_extra
    else:
        return orcamento

def vaga_extra_garagem(orcamento, quer_vaga_extra):
    while quer_vaga_extra != "S" and quer_vaga_extra != "N":
        print("Não identificamos sua escolha!")
        quer_vaga_extra = input("Digite novamente! Você deseja vaga(s) extra(s) de garagem? (S)sim ou (N)não ").upper()

    if quer_vaga_extra == "S":
        while True:
            try: 
                vaga_extra = int(input("Quantas vagas extras? "))
                       
                if vaga_extra > 0:
                    return orcamento + (vaga_extra * 60), quer_vaga_extra
                elif vaga_extra == 0:
                    print("Nenhuma vaga extra será adicionada.")
                    return orcamento, quer_vaga_extra
                else:
                    print("Não identificamos sua escolha! Número não pode ser negativo.")
                    continue
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
    else:
        return orcamento, quer_vaga_extra

def desconto_sem_crianca(orcamento):
    print("__________ Crianças __________\n")
    crianca = input("Você tem criança(s)? (S) sim ou (N) não ").upper()
    while crianca != "S" and crianca != "N":
        print("Não identificamos sua escolha!")
        crianca = input("Digite novamente! Tem criança(s)? (S)sim ou (N)não ").upper()

    if crianca == "N":
        return orcamento * 0.95, crianca
    else:
        return orcamento, crianca

def parcelas_contrato():
    contrato = 2000
    print("__________ Quantidade de parcelas __________\n")
    qtdade_parcelas = input("Em quantas vezes você deseja parcelar o valor do contrato? (Máximo de 5x) ")
    while qtdade_parcelas not in ["1", "2", "3", "4", "5"]:
        print("Não identificamos sua escolha!")
        qtdade_parcelas = input("Digite novamente! Em quantas vezes você deseja parcelar o valor do contrato? (Máximo de 5x) ")

    valor_parcela = contrato / int(qtdade_parcelas)
    return qtdade_parcelas, valor_parcela

def valor_orcamento():
    orcamento = 0
    limpar_tela()
    print("__________ Tipo de moradia __________\n")
    opcao_moradia = input("Você quer apartamento, casa ou estudio? ").lower()
    try:        
        if opcao_moradia == "apartamento" or opcao_moradia == "casa":
            limpar_tela()
            print("__________ Quantidade de quartos __________\n")
            qtdade_quartos = input("Digite a quantidade de quartos desejada (1 ou 2): ")
            while qtdade_quartos != "1" and qtdade_quartos != "2":
                print("Quantidade de quartos inválida!")
                qtdade_quartos = input("Digite novamente a quantidade de quartos desejada: ")
            limpar_tela()
            print("__________ Garagem __________\n")
            garagem = input("Você deseja uma vaga de garagem? (S)sim ou (N)não ").upper()
            orcamento = quartos(opcao_moradia, qtdade_quartos)
            orcamento = garagem_geral(orcamento, garagem)
            limpar_tela()
            orcamento, crianca = desconto_sem_crianca(orcamento)
            limpar_tela()
            qtdade_parcelas, valor_parcela = parcelas_contrato()
            limpar_tela()
            print("__________ Resumo do Orçamento __________\n")
            print("***Parcelas do contrato***")
            for i in range(1, int(qtdade_parcelas)+1):
                print(f"{i}ª de R$ {valor_parcela:.2f}")
            print("\n***Critérios escolhidos***")
            print(f" -> Moradia - {opcao_moradia}\n -> Quantidade de quartos - {qtdade_quartos}\n -> Garagem - {garagem}\n -> Criança - {crianca}\n -> Orçamento de aluguel mensal - R${orcamento:.2f}.")
            input ("\nAperte 'ENTER' para voltar!")

        elif opcao_moradia == "estudio":
            orcamento = 1200
            limpar_tela()
            print("__________ Garagem __________\n")
            garagem = input("Você deseja uma vaga de garagem? (S)sim ou (N)não ").upper()
            orcamento, quer_vaga_extra = garagem_estudio(orcamento, garagem)
            limpar_tela()
            orcamento, crianca = desconto_sem_crianca(orcamento)
            limpar_tela()
            qtdade_parcelas, valor_parcela = parcelas_contrato()
            limpar_tela()
            print("__________ Resumo do Orçamento __________\n")
            print("***Parcelas do contrato***")
            for i in range(1, int(qtdade_parcelas)+1):
                print(f"{i}ª de R$ {valor_parcela:.2f}")
            print("\n***Critérios escolhidos***")
            print(f" -> Moradia - {opcao_moradia}\n -> Garagem - {garagem}\n -> Vaga extra - {quer_vaga_extra}\n -> Criança - {crianca}\n -> Orçamento de aluguel mensal - R${orcamento:.2f}.")
            input ("\nAperte 'ENTER' para voltar!")
            
        else:
            print("Opção não encontrada")
            input ("Aperte 'ENTER' para voltar!")
    
    except:
        print("Opção de moradia não identificada!")
        input ("Aperte 'ENTER' para voltar!")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def encerrar_sistema():
    input ("Aperte 'ENTER' para encerrar!")

def executar_orcamento():
    while True:
        limpar_tela()
        print("---------- IMOBILIÁRIA PFLEGER ----------\n")
        quer_orcamento = input("Gostaria de fazer um orçamento? (S) sim ou (N) não ").upper()
        if quer_orcamento == "S":
            valor_orcamento()
            
        elif quer_orcamento == "N":
            encerrar_sistema()
            break
        else:
            input("Não entendi! Aperte 'ENTER' para voltar!")

executar_orcamento()