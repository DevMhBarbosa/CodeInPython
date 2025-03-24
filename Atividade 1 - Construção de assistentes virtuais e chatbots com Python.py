# Listas com os produtos, preços e quantidades vendidas
produtos = ["Produto A", "Produto B", "Produto C", "Produto D", "Produto E", "Produto F"]
precos = [10.5, 20.0, 15.0, 8.0, 12.0, 25.0]
quantidades = [5, 3, 10, 7, 6, 2]

# Lista vazia para armazenar os valores totais
valores = []

# Preenchendo a lista de valores com as multiplicações de preço e quantidade
for i in range(len(produtos)):
    valor_total = precos[i] * quantidades[i]
    valores.append(valor_total)

# Exibindo os resultados
for i in range(len(produtos)):
    print(f"{produtos[i]}: R${valores[i]:.2f}")