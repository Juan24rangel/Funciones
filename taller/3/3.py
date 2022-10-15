
print("---3. Construir una función que reciba como parámetro una lista de datos numéricos y retorne la suma de dichos datos---")
def sumardatos (lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

#lista
lista1=[2,3,4,5,6,7,8,9]
suma = sumardatos(lista1)
print(suma)
