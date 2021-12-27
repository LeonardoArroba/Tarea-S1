# ¿Siguiendo la prioridad de operadores, convierta a expresión matemática,resuelva e indique en cuál tipo de variable almacenará 
# el resultado de las siguientes expresiones:
# (5 + 3 * 2) + 9 > 3 * 5 * 14 % 3
# 2 *(4 - 10 + 8)/2* 36 *(1/2)
# 260 / 12 + 54 % 3 - 85 % 7
# (48 < 2 * 3) // (2 * 7 < 12)
# ((8 > 2) // (932 < 23) ) % 4 == 2

ejer1 = (5 + 3 * 2) + 9 > 3 * 5 * 14 % 3
print(ejer1)
print(type(ejer1))

ejer2 = 2 *(4 - 10 + 8)/2* 36 *(1/2)
print(ejer2)
print(type(ejer2))

ejer3 = 260 / 12 + 54 % 3 - 85 % 7
print(ejer3)
print(type(ejer3))

ejer4 = (48 < 2 * 3) | (2 * 7 < 12)
print(ejer4)
print(type(ejer4))

ejer5 = ((8 > 2) | (932 < 23) ) % 4 == 2
print(ejer5)