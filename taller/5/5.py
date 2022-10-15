print("5. Construir una función que reciba como parámetro una lista de datos numéricos y retorne el promedio de los datos pares")
def promediar_pares (lista):
    suma = 0
    promedio = 0
    cont=0
    for i in lista:
        if i%2==0:
            suma = (suma + i)
            cont=cont+1
    promedio=suma/cont
    return promedio

#lista
lista1=[2,3,4,5,6,7,8,9]
promedio = promediar_pares(lista1)
print(promedio)