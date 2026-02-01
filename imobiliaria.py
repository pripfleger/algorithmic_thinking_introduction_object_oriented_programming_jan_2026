contrato = 2000

def quartos():
    if opcao_moradia == "apartamento" and qtdade_quartos == "1":
        orcamento = 700
    elif opcao_moradia == "apartamento" and qtdade_quartos == "2":
        orcamento = 700+200
    elif opcao_moradia == "casa" and qtdade_quartos == "1":
        orcamento = 900
    elif opcao_moradia == "casa" and qtdade_quartos == "2":
        orcamento = 900+250
    else:
        print("Erro no processamento, escolha novamente a quantidade de quartos!")

def garagem():
    if garagem == "N":
        orcamento += 0
    elif garagem == "S":
        orcamento += 300
    else:
        print("Erro no processamento, você deseja uma vaga de garagem? (S)sim ou (N)não ")

def garagem_estudio():
    if garagem == "S":
        orcamento += 250
        vaga_extra = int(input("Quantas vagas extras? "))
        if vaga_extra != 0:
            orcamento += vaga_extra * 60
        else:
            print("Erro no processamento, digite novamente a quantidade de vagas desejadas: ")
        
    elif garagem == "N":
        orcamento += 200
    else:
        print("Não identificamos sua escolha, informe sua escolha novamente!")

def criança():
    criança = input("Você tem criança(s)? (S) sim ou (N) não ").upper()
    if criança == "N":

    elif criança == "S":

def valor_orcamento():
    orcamento = 0
    opcao_moradia = input("Você quer apartamento, casa ou estudio? ")
            
    if opcao_moradia == "apartamento" or opcao_moradia == "casa":
        qtdade_quartos = input("Digite a quantidade de quartos desejada (1 ou 2): ")
        garagem = input("Você deseja uma vaga de garagem? (S)sim ou (N)não ").upper()
        quartos()
        garagem()

    elif opcao_moradia == "estudio":
        orcamento = 1200
        garagem = input("Você deseja uma vaga de garagem? (S)sim ou (N)não ").upper()
        garagem_estudio()

    else:
        print("Opção não encontrada, escolha novamente!")

    print(f"Foi escolhido {opcao_moradia} e o orçamento é {orcamento}.")

while True:
    opcao_moradia = ""
    valor_orcamento()
    input("Pressione qualquer tecla para reiniciar!")