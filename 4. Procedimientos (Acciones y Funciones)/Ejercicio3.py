# Escriba una función que calcule el perímetro del pentágono (siendo el perímetro la
# suma de los lados del polígono).

def perimet_pentagono(n,l):
    perimetro = n * l
    return perimetro

if __name__ == "__main__":
    n = 5
    l = int(input("Ingrese la longitud del poligono: "))
    resultado = perimet_pentagono(n,l)
    print("{}cm".format(resultado))