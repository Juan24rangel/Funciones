print("---------------------------------")
print("-BUSCAR EL NUMERO DE UN CONJUNTO-")
print("---------------------------------")

#entrada
b= int(input("Numero a buscar: "))

#processing
a = [1,2,3,4,5]
r=False

for i in a:
    if i==b:
        print("lo encontre")
        r = True
if r==False:
    print("No lo encontre")

#salida
print("\nEso era... ")