def quartos(opcao_moradia, qtdade_quartos):
    try:
        if opcao_moradia == "apartamento" and qtdade_quartos == "1":
            return  700
        elif opcao_moradia == "apartamento" and qtdade_quartos == "2":
            return 700 + 200
        elif opcao_moradia == "casa" and qtdade_quartos == "1":
            return 900
        elif opcao_moradia == "casa" and qtdade_quartos == "2":
            return 900 + 250
        else:
            print("Erro no processamento, escolha novamente a quantidade de quartos!")
    except:
        print("Quantidade de quartos não identificada! Tente novamente!")

def garagem_geral(orcamento, garagem):
    try:
        if garagem == "N":
            return orcamento
        elif garagem == "S":
            return orcamento + 300
        else:
            print("Erro no processamento, você deseja uma vaga de garagem? (S)sim ou (N)não ")
    except:
        print("Opção de garagem não identificada! Tente novamente!")

def garagem_estudio(orcamento, garagem):
    try:
        if garagem == "S":
            orcamento += 250
            vaga_extra = int(input("Quantas vagas extras? "))
            if vaga_extra > 0:
                return orcamento + (vaga_extra * 60)
            else:
                print("Erro no processamento, digite novamente a quantidade de vagas desejadas: ")
            
        elif garagem == "N":
            return orcamento + 200
        else:
            print("Não identificamos sua escolha, informe sua escolha novamente!")
            return orcamento
    except:
        print("Opção de garagem do estúdio não identificada! Tente novamente!")

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
            qtdade_quartos = input("Digite a quantidade de quartos desejada (1 ou 2): ")
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