# Definicoes
oferta_arthur = 10
oferta_luiz = 30
oferta_pedro = 100

# Obtem o valor de entrada
diamantes_necessarios = int(input())

# Verifica qual das ofertas, sendo essa a minima, supre o requerimento
if diamantes_necessarios <= oferta_arthur:
    escolhido = "Arthur"
elif diamantes_necessarios <= oferta_luiz:
    escolhido = "Luiz"
elif diamantes_necessarios <= oferta_pedro:
    escolhido = "Pedro"
else:
    escolhido = "Nenhum"

# Informa o resultado
print(escolhido)