#listas

"""lista1 =[1, "hola", 1.25, True, False] #1 esta en la posicion 0
#len: longitud
longitud = len(lista1)
print("cantidad de elementos: ",longitud)
#aregagar elementos append()
lista1.append("colecciones")
insertar_elemento = lista1.insert(2, 4)
#print(lista1)

#acceder a los elementos de tu lista
#elemento = lista1[2]
#print(elemento)

#ELEMINAR ELEMENTOS: pop(posicion), remove(elemento)
lista1.pop(1)
lista1.remove("coleciones")
print(lista1)

#conoce el indice o posicion del elemento: index(elemento)
lista = [1, "true",3,4,5]
posicion = lista.index(True)
print(posicion)
#Extender lista
animales = ["perro", "gato", "caballo", "gallina"]
animales_acuaticos = ["delfin", "ballena", "tiburon", "pez"]
animales.extend(animales_acuaticos)
print(animales)
animales.extend(lista)
print(animales)
#eliminar los elementos de la lista: clear()
animales.clear()
print(animales)
#RECORRER UNA LISTA
Lenguajes_PR = ["python", "html", "css", "c++"]
for dato in Lenguajes_PR:
    print(dato)
#recorrer teniendo en cuenta la posicion
for indice in range(len(Lenguajes_PR)):
    print(Lenguajes_PR[indice], "estas en la posicion", indice)"""

#crear dos listas vacias llamadas par e impar
#pedir al usuario que ingrese 2 numeros
#while: si el numero 1 es menor que el numero 2: (determian el rango)
#e impares en la lista correspondiente.
#for: numero1 es inicio del rango,numero2 el final,los datos
#se almacenan en la lista correspondiente
num_inicio = int(input("inicie el numero inicial del rango: "))
num_fin = int(input("ingrese el numero final del rango: "))
par =[]
impar =[]

for num in range(num_inicio, num_fin + 1 ):
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print("lista de pares:", par)
print("lista impares:", impar )        




