# Obtem o valor de entrada
packs_iniciais = int(input())

# Calcula a quantidade de packs por vila
packs_por_vila = int( packs_iniciais / 3 )

# Calcula quantos packs sao descartados
packs_descartados = packs_iniciais - packs_por_vila*3

# Informa o resultado
print(int(packs_por_vila))
print(int(packs_descartados))