print("---4. Construir una función que reciba como parámetro una lista de datos numéricos y retorne el promedio de dichos datos---")
def promediar (lista):
    suma = 0
    promedio = 0
    cont=0
    for i in lista:
        suma = (suma + i)
        cont=cont+1
        promedio=suma/cont
    return promedio

#lista
lista1=[2,3,4,5,6,7,8,9]
promedio = promediar(lista1)
print(promedio)