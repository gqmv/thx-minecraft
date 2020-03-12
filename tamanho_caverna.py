# Obtem os valores de entrada
lado_caverna = int(input())
altura_caverna = int(input())

# Calcula o tamanho da base
blocos_base = lado_caverna ** 2

# Calcula os blocos totais na caverna
blocos_totais = blocos_base * altura_caverna

# Informa o resultado
print(int(blocos_totais))