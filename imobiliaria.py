def quartos(opcao_moradia, qtdade_quartos):
    if opcao_moradia == "apartamento" and qtdade_quartos == 1:
        return  700
    elif opcao_moradia == "apartamento" and qtdade_quartos == 2:
        return 700 + 200
    elif opcao_moradia == "casa" and qtdade_quartos == 1:
        return 900
    elif opcao_moradia == "casa" and qtdade_quartos == 2:
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
        orcamento = vaga_extra_garagem(orcamento, quer_vaga_extra)
    else:
        print("Não identificamos sua escolha!")
        return orcamento

def vaga_extra_garagem(orcamento, quer_vaga_extra):
    while quer_vaga_extra != "S" and quer_vaga_extra != "N":
        print("Não identificamos sua escolha!")
        quer_vaga_extra = input("Digite novamente! Você deseja vaga(s) extra(s) de garagem? (S)sim ou (N)não ").upper()

    if quer_vaga_extra == "S":
        vaga_extra = int(input("Quantas vagas extras? "))
        try:
            if vaga_extra > 0:
                return orcamento + (vaga_extra * 60)
            else:
                print("Erro no processamento!")
        except ValueError:
            print("Valor inválido! Nenhuma vaga extra adicionada.")
            return orcamento

def desconto_crianca(orcamento):
    crianca = input("Você tem criança(s)? (S) sim ou (N) não ").upper()
    
    try:
        if crianca == "N":
            return orcamento * 0.95
        elif crianca == "S":
            return orcamento
        else:
            print("Erro no processamento, digite novamente!")
    except:
        print("Informação de crianças não identificada! Tente novamente!")

def valor_orcamento():
    orcamento = 0
    opcao_moradia = input("Você quer apartamento, casa ou estudio? ")

    try:        
        if opcao_moradia == "apartamento" or opcao_moradia == "casa":
            qtdade_quartos = int(input("Digite a quantidade de quartos desejada (1 ou 2): "))
            try:
                while qtdade_quartos < 1 or qtdade_quartos > 2:
                    print("Quantidade de quartos inválida!")
                    qtdade_quartos = int(input("Digite novamente a quantidade de quartos desejada: "))
            except: exit()
            garagem = input("Você deseja uma vaga de garagem? (S)sim ou (N)não ").upper()
            orcamento = quartos(opcao_moradia, qtdade_quartos)
            orcamento = garagem_geral(orcamento, garagem)
            
            orcamento = desconto_crianca(orcamento)
            print(f"Foi escolhido {opcao_moradia} e o orçamento é de R${orcamento:.2f}.")

        elif opcao_moradia == "estudio":
            orcamento = 1200
            garagem = input("Você deseja uma vaga de garagem? (S)sim ou (N)não ").upper()
            orcamento = garagem_estudio(orcamento, garagem)
            orcamento = desconto_crianca(orcamento)
            print(f"Foi escolhido {opcao_moradia} e o orçamento é de R${orcamento:.2f}.")

        else:
            print("Opção não encontrada, escolha novamente!")
    except:
        print("Opção de moradia não identificada! Tente novamente!")

contrato = 2000

while True:
    valor_orcamento()
    input("Pressione qualquer tecla para reiniciar!")