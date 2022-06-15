#Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um
#desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos
#para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
livro = float(24.75)
desconto = float(0.40)
transporte1 = int(3)
transporte2 = float(0.75)
custo = livro*desconto*60 + transporte1 + transporte2*59
print('o valor final de 60 cópias dos livros é de {:.2f} R$'.format(custo))