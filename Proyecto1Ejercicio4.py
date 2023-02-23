
'''
Problema 4/6:

Los números cadena son creados al sumar continuamente el cuadrado de cada dígito de un número para formar otro.
Por ejemplo, si se tiene el número 44, se procede a elevar cada uno de sus dígitos al cuadrado
y la suma de ellos resulta en el 32 (4**2 + 4**2 = 16 + 16 = 32), luego se hace lo mismo con el 32,
donde resulta 13 (3*2 + 2*2 = 9 + 4 = 13) y así sucesivamente. Por ejemplo:

44   32   13   10   1   1

85   89   145   42   20   4   16   37   58   89

Una vez que la cadena llegue a 1 u 89, la cadena queda en un ciclo infinito como los mostrados en los ajemplos anteriores.
Es interesante notar que al comenzar con CUALQUIER número entero positivo, eventualmente llegará a 1 u 89.

Se pide que diseñe un programa que permita conocer cuál es el porcentaje de números enteros menor a un valor N (leído como dato),
cuya cadena llega al número 89.
'''



n=(input("ingrese el valor de n:"))
if not n.isnumeric():
    raise TypeError("ingrese un Número entero positivo")
n=int(n)
contador=0
#range es una función que va desde el 1 al n
for i in range(1,n+1):
    numero=i
    while numero != 1 and numero != 89:
        suma=0
        #este for que viene abajo separa en digitos, lo hace volviendo en un stream a numero y así usando un for in paso por todos sus digitos
        for digito in str(numero):
#           print("digito", digito)
            suma+=int(digito)**2
#            print("suma" , suma)
        numero=suma
    if numero==89:
        contador+=1
porcentaje=(contador/n)*100
print("el porcentaje de numeros de la cadena que llega al 89 es de:",porcentaje,"%")
