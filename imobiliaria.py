import os

#FUNÇÃO CALCULA ORÇAMENTO DE ACORDO COM A MORADIA ESCOLHIDA E QUANTIDADE DE QUARTOS
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

#FUNÇÃO ADICIONA VALOR AO ORÇAMENTO SE A PESSOA OPTAR POR INCLUIR VAGA DE GARAGEM 
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

#FUNÇÃO ADICIONA VALOR AO ORÇAMENTO SE A PESSOA OPTAR POR INCLUIR VAGA DE GARAGEM
def garagem_estudio(orcamento, garagem):
    while garagem != "S" and garagem != "N":
        print("Não identificamos sua escolha!")
        garagem = input("Digite novamente! Você deseja uma vaga de garagem? (S)sim ou (N)não ").upper()
        
    if garagem == "S":
        orcamento += 250
        quer_vaga_extra = input("Deseja adicionar vaga(s) extra(s)? (S) sim ou (N) não ").upper()
        orcamento, quer_vaga_extra, vaga_extra = vaga_extra_garagem(orcamento, quer_vaga_extra)
        return orcamento, quer_vaga_extra, vaga_extra
    else:
        return orcamento, "N", 0

#FUNÇÃO ADICIONA VALOR AO ORÇAMENTO SE A PESSOA OPTAR POR INCLUIR VAGA EXTRA DE GARAGEM
def vaga_extra_garagem(orcamento, quer_vaga_extra):
    while quer_vaga_extra != "S" and quer_vaga_extra != "N":
        print("Não identificamos sua escolha!")
        quer_vaga_extra = input("Digite novamente! Você deseja vaga(s) extra(s) de garagem? (S)sim ou (N)não ").upper()

    if quer_vaga_extra == "S":
        while True:
            try: 
                vaga_extra = int(input("Quantas vagas extras? "))
                       
                if vaga_extra > 0:
                    return orcamento + (vaga_extra * 60), quer_vaga_extra, vaga_extra
                elif vaga_extra == 0:
                    print("Nenhuma vaga extra será adicionada.")
                    return orcamento, quer_vaga_extra, 0
                else:
                    print("Não identificamos sua escolha! Número não pode ser negativo.")
                    continue
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
    else:
        return orcamento, quer_vaga_extra, 0

#FUNÇÃO APLICA DESCONTO DE 5% NO VALOR DO ORÇAMENTO SE O CLIENTE NÃO TEM CRIANÇAS DE ATÉ 12 ANOS
def desconto_sem_crianca(orcamento):
    print("__________ Crianças __________\n")
    crianca = input("Você tem criança(s) até 12 anos? (S) sim ou (N) não ").upper()
    while crianca != "S" and crianca != "N":
        print("Não identificamos sua escolha!")
        crianca = input("Digite novamente! Tem criança(s) até 12 anos? (S)sim ou (N)não ").upper()

    if crianca == "N":
        return orcamento * 0.95, crianca
    else:
        return orcamento, crianca

#FUNÇÃO CALCULA VALOR E QUANTIDADE DAS PARCELAS DO CONTRATO A PARTIR DA ESCOLHA DO CLIENTE DE ATÉ 5X
def parcelas_contrato():
    contrato = 2000
    print("__________ Quantidade de parcelas __________\n")
    qtdade_parcelas = input("Em quantas vezes você deseja parcelar o valor do contrato? (Máximo de 5x) ")
    while qtdade_parcelas not in ["1", "2", "3", "4", "5"]:
        print("Não identificamos sua escolha!")
        qtdade_parcelas = input("Digite novamente! Em quantas vezes você deseja parcelar o valor do contrato? (Máximo de 5x) ")

    valor_parcela = contrato / int(qtdade_parcelas)
    return qtdade_parcelas, valor_parcela

#FUNÇÃO CALCULA O VALOR DO ORÇAMENTO
def valor_orcamento():
    orcamento = 0
    limpar_tela()
    print("__________ Tipo de moradia __________\n")
    opcao_moradia = input("Você quer apartamento, casa ou estudio? ").lower() #ESCOLHA DO TIPO DE MORADIA
    try:        
        if opcao_moradia == "apartamento" or opcao_moradia == "casa":
            limpar_tela()
            print("__________ Quantidade de quartos __________\n")
            qtdade_quartos = input("Digite a quantidade de quartos desejada (1 ou 2): ") #ESCOLHA DA QUANTIDADE DE QUARTOS
            while qtdade_quartos != "1" and qtdade_quartos != "2":
                print("Quantidade de quartos inválida!")
                qtdade_quartos = input("Digite novamente a quantidade de quartos desejada: ")
            limpar_tela()
            print("__________ Garagem __________\n")
            garagem = input("Você deseja uma vaga de garagem? (S)sim ou (N)não ").upper() #ESCOLHA DE ADIÇÃO DE VAGA DE GARQAGEM
            orcamento = quartos(opcao_moradia, qtdade_quartos) #ADICIONA VALOR AO ORÇAMENTO EXECUTANDO A FUNÇÃO QUARTOS
            orcamento = garagem_geral(orcamento, garagem) #ADICIONA VALOR AO ORÇAMENTO EXECUTANDO A FUNÇÃO GARAGEM_GERAL
            limpar_tela()
            orcamento, crianca = desconto_sem_crianca(orcamento) #CONCEDE DESCONTO DE 5% SE O CLIENTE NÃO TEM CRIANÇAS EXECUTANDO A FUNÇÃO DESCONTO_SEM_CRIANCA
            limpar_tela()
            qtdade_parcelas, valor_parcela = parcelas_contrato() #CLIENTE SELECIONA QUANTIDADE DE PARCELAS E CALCULA PARCELAS EXECUTANDO A FUNÇÃO PARCELAS_CONTRATO
            limpar_tela()
            print("__________ Resumo do Orçamento __________\n")
            print("***Parcelas do contrato***")
            for i in range(1, int(qtdade_parcelas)+1): #MOSTRA AS PARCELAS E RESPECTIVO VALOR DE PARCELA EM LISTA COM DUAS CASAS DECIMAIS
                print(f"{i}ª de R$ {valor_parcela:.2f}")
            print("\n***Critérios escolhidos***")
            print(f" -> Moradia - {opcao_moradia}\n -> Quantidade de quartos - {qtdade_quartos}\n -> Garagem - {garagem}\n -> Criança - {crianca}\n -> Orçamento de aluguel mensal - R${orcamento:.2f}.") #EXIBE AS OPÇÕES ESCOLHIDAS PELO CLIENTE
            input ("\nAperte 'ENTER' para voltar!")

        elif opcao_moradia == "estudio":
            orcamento = 1200
            limpar_tela()
            print("__________ Garagem __________\n")
            garagem = input("Você deseja uma vaga de garagem? (S)sim ou (N)não ").upper() 
            orcamento, quer_vaga_extra, vaga_extra = garagem_estudio(orcamento, garagem) #ADICIONA VALOR AO ORÇAMENTO EXECUTANDO A FUNÇÃO GARAGEM_ESTUDIO E VAGA EXTRA, SE HOUVER, PELA FUNÇÃO VAGA_EXTRA_GARAGEM
            limpar_tela()
            orcamento, crianca = desconto_sem_crianca(orcamento) #CONCEDE DESCONTO DE 5% SE O CLIENTE NÃO TEM CRIANÇAS EXECUTANDO A FUNÇÃO DESCONTO_SEM_CRIANCA
            limpar_tela()
            qtdade_parcelas, valor_parcela = parcelas_contrato() #CLIENTE SELECIONA QUANTIDADE DE PARCELAS E CALCULA PARCELAS EXECUTANDO A FUNÇÃO PARCELAS_CONTRATO
            limpar_tela()
            print("__________ Resumo do Orçamento __________\n")
            print("***Parcelas do contrato***")
            for i in range(1, int(qtdade_parcelas)+1): #MOSTRA AS PARCELAS E RESPECTIVO VALOR DE PARCELA EM LISTA COM DUAS CASAS DECIMAIS
                print(f"{i}ª de R$ {valor_parcela:.2f}")
            print("\n***Critérios escolhidos***")
            if quer_vaga_extra == "N":
                print(f" -> Moradia - {opcao_moradia}\n -> Garagem - {garagem}\n -> Vaga extra - {quer_vaga_extra}\n -> Criança - {crianca}\n -> Orçamento de aluguel mensal - R${orcamento:.2f}.") #EXIBE AS OPÇÕES ESCOLHIDAS PELO CLIENTE
            else:
                print(f" -> Moradia - {opcao_moradia}\n -> Garagem - {garagem}\n -> Vaga extra - {quer_vaga_extra}\n -> Quantidade de vaga extra - {vaga_extra}\n -> Criança - {crianca}\n -> Orçamento de aluguel mensal - R${orcamento:.2f}.") #EXIBE AS OPÇÕES ESCOLHIDAS PELO CLIENTE
            input ("\nAperte 'ENTER' para voltar!")
            
        else:
            print("Opção não encontrada")
            input ("Aperte 'ENTER' para voltar!")
    
    except Exception as e:
        print(f"Erro: {e}")
        print("Opção de moradia não identificada!")
        input ("Aperte 'ENTER' para voltar!")

#FUNÇÃO LIMPA A TELA
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#FUNÇÃO ENCERRA O SISTEMA
def encerrar_sistema():
    input ("Aperte 'ENTER' para encerrar!")

#FUNÇÃO QUE EXECUTA O LOOP PRINCIPAL
def executar_orcamento():
    while True:
        limpar_tela()
        print("---------- R.M. IMOBILIÁRIA ----------\n")
        quer_orcamento = input("Gostaria de fazer um orçamento? (S) sim ou (N) não ").upper() #ESCOLHA DO CLIENTE SE QUER ORÇAR OU NÃO
        if quer_orcamento == "S":
            valor_orcamento()
            
        elif quer_orcamento == "N":
            encerrar_sistema()
            break
        else:
            input("Não entendi! Aperte 'ENTER' para voltar!")

#CHAMADA DA FUNÇÃO PARA EXECUTAR
executar_orcamento()