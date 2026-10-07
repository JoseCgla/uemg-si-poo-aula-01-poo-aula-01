# Programação Estruturada

nome = "Camiseta"
preco = 50.0

def aplicar_desconto(preco, desconto):
    return preco - (preco * desconto)

# Reatribuição corrigida para o primeiro produto
preco = aplicar_desconto(preco, 0.1)
print(nome, preco)

# Adição do segundo produto
nome2 = "Calça Jeans"
preco2 = 90.0
preco2 = aplicar_desconto(preco2, 0.1)
print(nome2, preco2)
