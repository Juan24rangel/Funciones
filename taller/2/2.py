print("---2. Construir una función que reciba una cadena digitada (como parametro) por el usuario y que lo muestre n veces en pantalla.---")

def mostrar_cadena(cadena , n):
    for i in range (n):
        print(cadena)
        
cadena = input("Digite cadena de texto: ")
n = int(input("Numero de veces a mostrar la cadena: "))
mostrar_cadena(cadena,n)