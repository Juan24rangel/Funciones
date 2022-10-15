print("---------------------------------")
print("-BUSCAR EL NUMERO DE UN CONJUNTO-")
print("---------------------------------")

# definicion de la funcion
def buscarDatosLista(datoBuscar , Lista):
    r= False
    for i in Lista:
        if i == datoBuscar:
            r = True
    return r

#entrada
dato = int(input("Numero a buscar: "))

#processing
Lista = [1,2,3,4,5]
if buscarDatosLista (dato, Lista):
    print("lo encontre")
else: 
    print("no lo encontre")