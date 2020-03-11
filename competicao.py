# Obtem os valores de entrada
diamantes_arthur_hora = int(input())
diamantes_luiz_hora = int(input())
diamantes_pedro_hora = int(input())
duracao = int(input())

# Determina qual a maior quantidade media de diamantes por hora
maior_entre_arthur_luiz = (diamantes_arthur_hora + diamantes_luiz_hora + abs(diamantes_arthur_hora - diamantes_luiz_hora)) / 2
maior_total = (maior_entre_arthur_luiz + diamantes_pedro_hora + abs(maior_entre_arthur_luiz - diamantes_pedro_hora)) / 2

# Calcula qual foi o maximo de diamantes obtidos
maximo_diamantes = maior_total * duracao

# Informa o maximo de diamantes obtidos
print(int(maximo_diamantes))