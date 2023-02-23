'''
Problema 3/6:

Realice un programa que genere una lista de listas, que emule a una matriz de orden NxM, con N y M
dados por el usuario. Suponga dicha matriz está llena de la forma zig-zag horizontal según la secuencia que
se muestra en el ejemplo:
                           1   2   3
                           6   5   4
                           7   8   9
                           12  11  10





-Una lista es una estructura de datos que se usa para almacenar conjuntos de información o colecciones
 de elementos, su sintaxis es:
 nombre_de_lista = ["elemento1", "elemento2","elemento3"] , las comillas se usan porque los datos son strings.
 nombre_de_lista = ["elemento1", 45,3.1416, false], debe haber un espacio después de la coma.
 Se pueden tener listas vacías: lista_vacia = []

-Para acceder a los elementos de una lista:
 nombre_de_lista[posición del elemento al que quiero acceder o índice]
 nombre_de_lista[1:3] para que me indique los 2 elementos que hay entre el comienzo de la posición 1
 y el comienzo de la posición 3.
 nombre_de_lista[:3] para indicar el comienzo de la posición 0 hasta el comienzo de la posición 3.
 nombre_de_lista[1:] para indicar el comienzo de la posición 1 hasta el final.
 nombre_de_lista[:] para indicar el comienzo de la posición 0 hasta el final (todos).
 Recordando que las posiciones se cuentan desde 0 (de izquierda a derecha)
 o desde -1 (de derecha a izquierda.

- Nota: recordar que la posición comienza en cero y el número de elemento en 1.

- Una lista de listas es una estructura donde, dentro de cada índice de una lista, se encuentra otra lista.
'''

# Solución del ejercicio:
#   1.- Pido al usuario que ingrese el numéro de filas y columnas que tendrá la matriz (N y M).
#   2.- Creo las listas: fila, columna, matriz.
#   3.- Creo: factor (k)inicializado en cero, invertidor inicializado en 1, nivelador inicializado en 1.
#       El invertidos invierte las filas.
#       El nivelador indica dónde comienza (6, 12..).
#       Factor K.
#   4.- Corroborar que los datos suministrados sean números válidos.
#   5.- Convierto esos valores N y M dados por el usuario en enteros.
#   6.- Creo un ciclo "for" que comenzará en "i" y terminará en "N-1".
#       (n-1) porque los índices comienzan a contabilizar la posición en cero y terminan en (n-1).
#       Crear la matriz: fila es N y columna es M.
#       La función range (rango o intervalo)asociada al ciclo for: for i in range(n):
#           implica que para cada elemento o valor en un intervalo (0,N)...para 0,1,2...(N-1)
#           "i" se manejará en el rango de las filas. 
#           "j" se manejará en el rango de las columnas.
#  

#   1.- Pido al usuario que ingrese el numéro de filas y columnas que tendrá la matriz (N y M).
n=input("Ingrese el número de filas N:")
m=(input("Ingrese el número de columnas M:"))

#   2.- Creo las listas: fila, columna, matriz.
fila=[]
columna=[]
matriz=[]

#   3.- Creo: factor (k), invertidos inicializado en 1, nivelador inicializado en 1.
K=0
invertidor=1
nivelador=1

#   4.- Corroborar que los datos suministrados sean números válidos.
if not n.isnumeric() or not m.isnumeric():
    raise TypeError("ingrese números enteros positivos porfa")

#   5.- Convierto esos valores N y M dados por el usuario en enteros.
n=int(n)
m=int(m)
matriz=[]

#   6.- Creo un ciclo "for" que comenzará en "i" y terminará en "n-1".
#           Crear la matriz: fila es N y columna es M.
for i in range(n):
    fila=[]
    for j in range(m):
        fila.append(0)
    matriz.append(fila)

#proximos dos ciclos for son para recorrer cada elemento de la matriz
for h in range(n):
    for d in range(m):

#este if es para aumentar la fila para luego restarle ya que no supe como voltearla
# es decir no supe usar el ".reversed"
        if K ==m*invertidor:
            K=(m+K)+1
            invertidor+=2

#este if es para compensar el k ya que le reste "m" tantos
        if K ==(m*nivelador)+1:
            K=K+m-1
            nivelador+=2

#cuando h es impar resto
        if h%2!=0:
            K-=1

#cuando h es par sumo
        if h%2==0:
            K+=1

        matriz[h][d]=K

print(matriz)
