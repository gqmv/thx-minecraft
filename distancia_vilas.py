# Definicoes e obtencao de entradas

# Coordenadas de cada vila
# Hogsmeade
hogsmeade_x = 34
hogsmeade_z = 220
# Kakariko
kakariko_x = 0
kakariko_z = 0
# Solitude
solitude_x = 140
solitude_z = 456

# Obtem as entradas do The Huxley
tantan_x = int(input())
tantan_z = int(input())

# Fim de definicoes e obtencao de entradas


def calcular_distancia(coord_x,coord_z):
    '''

    :param coord_x: Coordenada X da vila.
    :param coord_z: Coordenada Y da vila
    :return: A distancia entre a vila e a posicao de TanTan, aproximado para duas casas decimais
    '''
    distancia_bruta = ( (coord_x - tantan_x)**2 + (coord_z - tantan_z)**2 )**(1/2)


    return round(distancia_bruta,2)

# Calcula a distancia de cada vila
hogsmeade_distancia = calcular_distancia(hogsmeade_x,hogsmeade_z)
kakariko_distancia = calcular_distancia(kakariko_x,kakariko_z)
solitude_distancia = calcular_distancia(solitude_x,solitude_z)

# Informa as distancias
print(f"Distancia para Hogsmeade: {hogsmeade_distancia:.2f}")
print(f"Distancia para Kakariko: {kakariko_distancia:.2f}")
print(f"Distancia para Solitude: {solitude_distancia:.2f}")