# Sistema de Orçamento - R.M. Imobiliária

Sistema interativo de orçamento de aluguel desenvolvido em Python para facilitar o cálculo de valores mensais baseado nas preferências do cliente.

## Descrição

O sistema permite que usuários calculem o valor do aluguel mensal considerando diferentes tipos de moradia, quantidade de quartos, vagas de garagem e descontos especiais. Além disso, oferece opções de parcelamento do contrato inicial.

## Funcionalidades

- **Tipos de Moradia**: Apartamento, Casa ou Estúdio
- **Configuração de Quartos**: 1 ou 2 quartos (para apartamentos e casas)
- **Garagem**: Opção de vaga simples ou múltiplas vagas e extras (para estúdios)
- **Desconto Especial**: 5% de desconto para locatários sem crianças até 12 anos
- **Parcelamento do Contrato**: Divisão do valor de R$ 2.000,00 em até 5 parcelas
- **Interface Interativa**: Menu intuitivo com limpeza de tela automática

## Tabela de Valores

### Apartamentos
- 1 quarto: R$ 700,00
- 2 quartos: R$ 900,00
- Garagem: +R$ 300,00

### Casas
- 1 quarto: R$ 900,00
- 2 quartos: R$ 1.150,00
- Garagem: +R$ 300,00

### Estúdios
- Valor base: R$ 1.200,00
- Garagem: +R$ 250,00
- Vaga extra: +R$ 60,00 por vaga adicional

## Como Usar

1. Execute o programa:
```bash
python nome_do_arquivo.py
```

2. Siga as instruções no menu interativo:
   - Escolha o tipo de moradia
   - Defina a quantidade de quartos (se aplicável)
   - Selecione as opções de garagem
   - Informe se há crianças no imóvel
   - Escolha a quantidade de parcelas do contrato

3. Visualize o resumo completo com:
   - Parcelas do contrato
   - Critérios selecionados
   - Valor final do aluguel mensal

## Requisitos

- Python 3.x
- Sistema operacional: Windows, Linux ou macOS

## Estrutura do Código

O sistema é organizado em funções modulares:

- `quartos()`: Calcula valores base por tipo e quantidade de quartos
- `garagem_geral()`: Processa vaga de garagem padrão
- `garagem_estudio()`: Gerencia garagem e vagas extras para estúdios
- `vaga_extra_garagem()`: Adiciona vagas extras personalizadas
- `desconto_sem_crianca()`: Aplica desconto de 5%
- `parcelas_contrato()`: Calcula parcelamento do contrato
- `valor_orcamento()`: Função principal de processamento
- `executar_orcamento()`: Loop principal do sistema

## Exemplo de Uso
```
---------- IMOBILIÁRIA PFLEGER ----------

Gostaria de fazer um orçamento? (S) sim ou (N) não S

__________ Tipo de moradia __________

Você quer apartamento, casa ou estudio? casa

__________ Quantidade de quartos __________

Digite a quantidade de quartos desejada (1 ou 2): 2

__________ Garagem __________

Você deseja uma vaga de garagem? (S)sim ou (N)não S

__________ Crianças __________

Você tem criança(s)? (S) sim ou (N) não N

__________ Quantidade de parcelas __________

Em quantas vezes você deseja parcelar o valor do contrato? (Máximo de 5x) 3

__________ Resumo do Orçamento __________

***Parcelas do contrato***
1ª de R$ 666.67
2ª de R$ 666.67
3ª de R$ 666.67

***Critérios escolhidos***
 -> Moradia - casa
 -> Quantidade de quartos - 2
 -> Garagem - S
 -> Criança - N
 -> Orçamento de aluguel mensal - R$1377,50.
```

## Notas

- Todos os valores são calculados automaticamente baseados nas escolhas do usuário
- O sistema valida entradas para evitar erros
- A tela é limpa automaticamente entre as etapas para melhor visualização

## Autor

Imobiliária Pfleger

---

**Desenvolvido com Python**