# Construya una función “Eleva” Que reciba como parámetros una base y un
# exponente y retorne al algoritmo principal el resultado de elevar un numero al otro.

def elevar(base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado
        
print(2**3)
