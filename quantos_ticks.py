# Definicoes
ticks_seguros = 12000 # Ticks nos quais TamTam pode construir a cada ciclo
ciclos_por_hora = 3
horas_disponiveis = 3

# Obtem os valores de entrada
dias_construcao = int(input())
quantidade_casas = int(input())

# Calcula quantos ticks a construcao ira durar
ticks_por_dia = ticks_seguros * ciclos_por_hora * horas_disponiveis
ticks_totais = ticks_por_dia * dias_construcao

# Calcula quantos ticks cada casa levara para ser construida
ticks_por_casa = ticks_totais / quantidade_casas

# Informa o resultado
print(int(ticks_por_casa))