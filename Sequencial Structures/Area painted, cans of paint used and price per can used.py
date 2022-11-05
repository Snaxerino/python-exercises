import math

# Valores já definidos no problema
litros_lata = 18
preco_lata = 80

m2 = float(input("Por favor, indique a área em metros quadrados: "))
litros_necessarios = m2 / 3  # cobertura da tinta é de 1 litro para cada 3 metros quadrados

# Quantidade de latas de tinta a serem compradas e o preço total
quantidade_latas = math.ceil(litros_necessarios / litros_lata)
custo_latas = quantidade_latas * preco_lata
print(f'Serão necessários {litros_necessarios} litros de tinta.  ')
print(f'Sendo assim o cliente precisará de comprar {quantidade_latas} latas, cujo o preço será de {custo_latas}€.\n')
