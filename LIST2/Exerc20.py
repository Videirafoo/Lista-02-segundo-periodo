def exerc14():
    
    print()
    
    print("20. Problema real — Análise de vendas")
    print("Uma empresa registrou as vendas de uma semana na lista") 
    print("vendas = [1250, 980, 1430, 2100, 1750, 890, 1620]. Desenvolva um programa que calcule") 
    print("o total vendido, a média diária, a maior e a menor venda, quantos dias ficaram acima da média e o percentual de dias acima da média.")
    
    print()
        
    vendas = [1250, 980, 1430, 2100, 1750, 890, 1620]
    total = 0
    maior = vendas[0]
    menor = vendas[0]

    for venda in vendas:
        total += venda
        if venda > maior:
            maior = venda
        if venda < menor:
            menor = venda

    media = total / len(vendas)
    acima = 0

    for venda in vendas:
        if venda > media:
            acima += 1

    percentual = (acima / len(vendas)) * 100

    print("Total:", total)
    print(f"Média diária: {media:.2f}")
    print("Maior venda:", maior)
    print("Menor venda:", menor)
    print("Dias acima da média:", acima)
    print(f"Percentual acima da média: {percentual:.2f}%")

    print()
    
if __name__ == "__main__":
    exerc14()