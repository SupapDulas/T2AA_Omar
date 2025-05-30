import random
import math

# Generar coordenadas aleatorias
def generarCoor(cant):
    coor = []
    for _ in range(cant):
        x = random.randint(-81, 81)
        y = random.randint(-81, 81)
        coor.append([x, y])
    return coor

# Calcular distancia al origen
def distOrigen(p):
    x, y = p
    return math.sqrt(x**2 + y**2)

# Buscar coordenada más alejada con X > 0 e Y < 0
def masLejana(coor):
    if not coor:
        return None
    if len(coor) == 1:
        x, y = coor[0]
        if x > 0 and y < 0:
            return coor[0]
        else:
            return None

    mitad = len(coor) // 2
    izq = masLejana(coor[:mitad])
    der = masLejana(coor[mitad:])

    if izq and der:
        return izq if distOrigen(izq) > distOrigen(der) else der
    elif izq:
        return izq
    else:
        return der

# Programa principal
def main():
    n = int(input("Ingrese la cantidad de coordenadas: "))
    lista = generarCoor(n)

    print("Coordenadas generadas:")
    for p in lista:
        print(p)

    res = masLejana(lista)

    if res:
        print("Coordenada más alejada con X > 0 e Y < 0:", res)
        print("Distancia al origen:", round(distOrigen(res), 2))
    else:
        print("No hay coordenadas con X > 0 e Y < 0.")

# Ejecutar
main()
