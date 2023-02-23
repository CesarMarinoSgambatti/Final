'''
Problema 2/6:

Un caracol cae un pozo de H metros de profundidad. Este caracol durante el día asciende una distancia
Ld metros, pero durante la noche, al quedarse dormido, resbala y desciende Ln metros. Diseñe un programa
que simulando el movimiento del caracol para H, Ld y Ln dados por el usuario. El programa debe arrojar
como resultado en cuantos días el caracol sale del pozo (si es que esto sucede) correctamente.
'''

#Solicitamos al usuario los valores: H, Ld y Ln.

H=(input("ingresa la profundidad del pozo en metros:"))
Ld=(input("ingresa la distancia que el caracol asciende durante el día en metros:"))
Ln=(input("ingrese la cantidad que el caracol desciende durante la noche en metros:"))

#En el punto inicial, no ha transcurrido tiempo (Dias=0)y no se ha recorrido distancia (Distancia_Recorrida=0).

Distancia_Recorrida=0
Dias=0

#Se hace uso de una sentencia condicional if-else (sí-caso contrario):

'''
Si alguno de los 3 parámetros no es un valor válido(se usa OR NOT "si este no es o este no es o este no es), (recordando que .isnumeric permite identificarlo), se ejecuta con raise la excepción
para tipear la solicitud de ingresar un entero positivo.
'''

if not H.isnumeric() or not Ld.isnumeric() or not Ln.isnumeric() :
   raise TypeError("Ingrese un número entero y positivo")
H=int(H)
Ld=int(Ld)
Ln=int(Ln)

'''
Para poder salir, la distancia recorrida de día (Ld) debe ser mayor que la recorrida de noche (Ln).
Haciendo uso de un condicional if-else: Si Ld es mayor que Ln, se desarrolla un proceso que indicará cuándo sale; en caso contrario "el caracol no sale del pozo".
Con un condicional while-if- (mientras-si-), establecemos que mientras no halla salido del pozo (Distancia_Recorrida+=Ld-Ln menor a la profundidad del pozo), se irá sumando un día al tiempo que demora en salir.
Si Distancia_Recorrida>=H, salió (se establecen mensajes distintos si lo logró en uno o varios días).
'''


while Distancia_Recorrida < H:
    Distancia_Recorrida+=Ld
    Dias+=1
    if Distancia_Recorrida < H:
        Distancia_Recorrida-=Ln
if Distancia_Recorrida>=H:
    if Dias==1:
        print("el caracol dura un día en salir")
    else:
        print("Al ", Dias,"días el caracol sale")


