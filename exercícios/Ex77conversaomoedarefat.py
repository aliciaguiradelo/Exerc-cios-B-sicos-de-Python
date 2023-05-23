from utils import ApiConversao as ac
while True:
    valor = float ( input ("Digite o valor em R$: "))
    print("Deseja converter para:")
    moeda = input ("Dólar  -  USD  \n" +
                "Euro   -  EUR  \n" +
                "Bitcoin-  BTC  \n").upper()
    dados = ac.obterTaxa(moeda)
    if (dados != ''):
        print(ac.conversaoMoeda())
    else:
        print("MOEDA não encontrada")
    retorno = input ("Deseja realizar uma nova consulta? S/N")
    if retorno == 'n':
        break
print("Obrigada!")