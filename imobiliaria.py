contrato = 2000
orcamento = 0

opcao_moradia = input("Você quer apartamento, casa ou estudio? ")
qtdade_quartos = input("Digite a quantidade de quartos desejada (1 ou 2): ")
#criança = input("Você tem criança(s)? (S) sim ou (N) não ").upper()
garagem = input("Você quer garagem? (S) sim ou (N) não ").upper()
vaga_extra = ("Quantas vagas extras? ")

if opcao_moradia == "apartamento":
    orcamento = 700
    if qtdade_quartos == "1":
        orcamento += 0
    elif qtdade_quartos == "2":
        orcamento += 200
    
elif opcao_moradia == "casa":
    orcamento = 900
    if qtdade_quartos == "1":
        orcamento += 0
    elif qtdade_quartos == "2":
        orcamento += 250

elif opcao_moradia == "estudio":
    orcamento = 1200
    if garagem == "S":
        orcamento += 250
        if vaga_extra != 0:
            orcamento += vaga_extra*60
    elif garagem == "N":
        orcamento += 200

else:
    print("Opção não encontrada, escolha novamente!")

print(f"Foi escolhido {opcao_moradia} e o orçamento é {orcamento}.")
